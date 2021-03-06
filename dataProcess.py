from datetime import datetime
from mapper.ChargeMapper import ChargeMapper

import numpy as np
import numpy.linalg as la

from PyQt5.QtCore import pyqtSlot

from ParamsSetWindow import ParamsSetWindow

class DataProcess():
    def __init__(self):
        self.chargeMapper = ChargeMapper() #注入数据库交互文件
        self.paramsSetWindow = ParamsSetWindow()
        #self.paramsSetWindow.sig.connect(self.do_receive_config)  # 注意这个类不是pyqt的带有窗口的类，我估计就实现不了信号接收的功能！！！  故改变思路 保存到数据库把
        #self.weight_values = None  # 权值数组  记录的

    #根据时间段至数据库取出某个充电站中所有充电桩电能计量数据#
    def compute_energy(self, station_name, start_time, end_time):
        '''
        根据时间段至数据库取出某个充电站中所有充电桩电能计量数据
        :param charge_station: 字符串类型，充电站名称
        :param start_time: 字符串类型，指定起时时间
        :param end_time: 字符串类型，指定终止时间    end_time - start_time = 时间段
        :return: 充电站中所有充电桩的电能计量数据  数组格式[E11, E12, ..., E13]
        '''
        start_time = start_time.split("\r")[0] #'2021-10-11 20:30:10\r\n' 一般字符串正确输出就是这个形式，所以需要对‘\r’进行分割取第一块0
        end_time = end_time.split("\r")[0]
        dt_start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        dt_end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        try:
            self.connectCursor.execute("SELECT energy  from table_charge_pile where "
                                       "sid = (select sid from table_charge_station where station_name = '%s')and "
                                       "start_time = '%s' and "
                                       "end_time = '%s'"
                                       %(station_name, dt_start_time, dt_end_time))
            self.data = self.connectCursor.fetchall()
        except:
            print("数据库获取失败") #按理是抛异常的

        self.dbConnect.commit()  # 提交更改

        return self.data

    # 根据充电桩名称、测量起始时间、时间段数量  至数据库取出某个充电站中所有充电桩电能计量数据#  测试ok，2021/11/29 21:42   updated 2022/2/19
    def compute_energy_matrix(self, station_name, begin_time, limit_period):
        '''
        # 根据一整段时间（需要在这个总时间段内，计算误差）至数据库取出某个充电站中所有充电桩电能计量数据#
        :param charge_station: 字符串类型，充电站名称
        :param start_time: 字符串类型，指定起时时间
        :param end_time: 字符串类型，指定终止时间    end_time - start_time = 时间段
        :return: 充电站中所有充电桩的电能计量数据  数组格式[[E11, E12, ..., E1n],[E21, E22, ..., E2n], ...]
        '''
        '''
        start_time = start_time.split("\r")[0]  # '2021-10-11 20:30:10\r\n' 一般字符串正确输出就是这个形式，所以需要对‘\r’进行分割取第一块0
        end_time = end_time.split("\r")[0]
        dt_start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        dt_end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        '''
        ######################求list_B#############################
        #根据充电站名称查询sid
        sid = self.chargeMapper.find_sid_by_charge_name(station_name)
        #sid 需要根据数据库查找“北工大充电桩”的pid的总数  待完善 ->已完善
        count_pid = self.chargeMapper.find_count_pid_by_sid_and_period(sid)

        list_energy = self.chargeMapper.find_station_all_energy_by_sid_and_period(sid, begin_time, limit_period * count_pid)
        #二维数组纵坐标
        line = limit_period
        list_A = list([])
        #将data数组数据换成二维数组，根据pid的数量#
        for i in range(0, line):
            temp = list([])
            for j in range(0, count_pid):
                temp.append(list_energy[j + i * count_pid][0])
            list_A.append(temp)
            #list_A.append(list_energy[i * count_pid: (i + 1) * count_pid])
        result_A = np.array(list_A)

        ##########################################################

        ######################求list_B############################
        #list_B = [[E1 - E0 - (E11 + E12 + E13 +....)], [E2 - E0 - (E21 + E22 + E23 + ....)], ...]
        #首先从充电站时间段数据表 table_station_period表中取出充电站总的能量消耗数据、按时间排序(求E1)
        tot_en = self.chargeMapper.find_total_energy_by_sid_and_period(sid, begin_time, limit_period)
        #再从table_charge_pile表中查找充电桩损耗能量E0应该是代表该时段所有充电桩的的损耗数据总和（求E0）  暂时这么理解
        loss_en = self.chargeMapper.find_loss_energy_by_sid_and_period(sid, begin_time, limit_period)
        result_B = list([])
        #最后根据已经获得的矩阵result_A计算(E11 + E12 + E13 + ....)
        tot_period_en = list([])
        for i in range(0, line):
            tot_period_en.append(sum(result_A[i]))
            result_B_num = tot_en[i][0] - loss_en[i][0] - tot_period_en[i]
            result_B.append(result_B_num)
        ##########################################################
        return result_A, result_B, sid

    #根据矩阵，求解
    #出现的问题，A不是方阵的话就会报错，这是numpy的一个小bug  LinAlgError: Last 2 dimensions of the array must be square
    #我查阅了一下，numpy.linalg.solve()在计算上采用的是高斯消去法，要求左边的A是方阵  2021/11/29 22:07
    #使用矩阵OR分解？？？ 最小二乘问题 https://andreask.cs.illinois.edu/cs357-s15/public/demos/06-qr-applications/Solving%20Least-Squares%20Problems.html
    #
    def compute_matrix(self, list_A, list_B):
        '''
        根据矩阵，求解
        :param list_A: 矩阵变量参数 [[4, 3], [-5, 9]]
        :param list_B: 矩阵求解参数[20, 26]
        :4△1  + 3△2 = 20
        :-5△1 + 9△2 = 26
        :return: 充电站中所有充电桩的电能计量数据  数组格式[△1, △2, ..., △n]
        '''
        A = np.array(list_A, dtype='float')
        B = np.array(list_B, dtype='float')

        if np.linalg.det(A) == 0:  # 用于判断矩阵是否有唯一解，唯一解的判断依据就是   ？？？？？2022/02/24
            return None, False
        #list = np.linalg.inv(A).dot(B)
        #最小二乘法能解决 2021/11/28 22:20
        list = la.solve(A.T.dot(A), A.T.dot(B))
        #list = np.linalg.solve(A, B)
        return list, True


    #计算充电桩n的风险评估量化数据，将整体计量性能分为“高、较高、较低、低“四种风险等级
    #weight_values：代表[k1, k2, k3,..., km]
    #返回：每个充电桩的风险等级指数，返回一个列表
    def compute_risk_level(self, sid, error_list):
        #根据pid和sid从数据库中查找误差数据、充电桩安装时长、使用频率、环境温度、环境湿度、运营商维护次数等等
        data = self.chargeMapper.find_risk_factors_by_pid_and_sid(sid)
        if data is None:
            return
        data_weights = self.chargeMapper.find_weights_param()
        Q = 0
        list_Q = list([])
        if data_weights is None:
            for i in range(0, len(data)):
                error = round(error_list[i], 3)
                level = data[i][0]
                install_time = data[i][1]
                use_freq = float(data[i][2])
                env_temper = float(data[i][3])
                Q = (0.9195 * (error / level) * (error / level) + 0.1195) * 0.8 + \
                    (0.0024 * (install_time * install_time) + 0.0745 * install_time + 0.0203) * 0.04 + \
                    (0.4348 * (use_freq * use_freq) + 0.0715 * use_freq + 0.0321) * 0.01 + \
                    (-0.0002 * (env_temper) * (env_temper) + 0.0114 * env_temper + 0.0667)
                list_Q.append(Q*100)
        else:  # 这种情况作为手动输入了权值的情况，待做
            weight_values = list([])
            for i in range(0, len(data_weights[0])):     # 将数据库中的权值系数取出
                weight_values.append(float(data_weights[0][i]))

            for i in range(0, len(data)):
                error = round(error_list[i], 3)
                level = data[i][0]
                install_time = data[i][1]
                use_freq = float(data[i][2])
                env_temper = float(data[i][3])
                Q = (0.9195 * (error / level) * (error / level) + 0.1195) * weight_values[0] + \
                    (0.0024 * (install_time * install_time) + 0.0745 * install_time + 0.0203) * weight_values[1] + \
                    (0.4348 * (use_freq * use_freq) + 0.0715 * use_freq + 0.0321) * weight_values[2] + \
                    (-0.0002 * (env_temper) * (env_temper) + 0.0114 * env_temper + 0.0667 * weight_values[3])
                list_Q.append(Q * 100)
        return list_Q

if __name__ == "__main__":
    dataProcess = DataProcess()
    #list_A, list_B = dataProcess.compute_energy_matrix("星星充电", "2021-10-02 09:02:02", 7)
    #list_V = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #result = dataProcess.compute_matrix(list_A, list_B)
    #print(result)
    result = dataProcess.compute_risk_level(sid=21)
    print(result)

    list_A = [[4, 3], [-5, 9]]
    list_B = [20, 26]
    #result, isOnlyJie = dataProcess.compute_matrix(list_A, list_B)
    #print(result)
    #print(isOnlyJie)
    #print(sum(list_B))



