from PyQt5.Qt import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from Common import get_db_connection, close_db
from PyQt5.QtWidgets import QFileDialog
from dataProcess import DataProcess
import time

class ShowInfo:
    def __init__(self, info: int):
        self.info = info

class Thread_import_data_from_excel(QThread): #导入数据线程
    show_info_signal = pyqtSignal(ShowInfo) #自定义信号

    def __init__(self, data_df):
        super().__init__()
        self.data_df = data_df
        self.connection, self.cursor = get_db_connection()

    def run(self):
        self.import_data_from_excel(self.data_df)

    def import_data_from_excel(self, data_df):
        data = []
        i = 0
        # 开启事务
        self.connection.begin()
        index = 0  # 记录索引 判断是哪一行出错 提示用户！！！
        # recode1 = ["北工大充电站", str(1111.121212), str(1221.122121)
        ################导入充电站名称与经纬度#######################
        try:
            record = data_df.values[0]
            # record[0]: 充电站名称
            station_name = record[7]
            record[10] = str(record[10])  # 经度
            record[11] = str(record[11])  # 维度
            # 解决导入数据重复问题
            record[0] = str(record[0])  # 测量开始时间
            record[8] = record[8]  # 所属区/县
            record[9] = record[9] # 详细地址


            record[1] = str(record[1])  # 测量结束时间

            record[5] = str(record[5])  # 充电桩出厂编号
            record[6] = str(record[6])  # 充电桩生产厂家
            record[12] = str(record[12])  # 运营商


            record[30] = str(record[30])  # 相对湿度  40可能不用str转换
            record[32] = str(record[32])  # 充电站表累计电量
            record[33] = str(record[33])  # 充电桩损耗数据
            record[35] = str(record[35])  # 充电桩n在时段t的电能计量数据

            # todo：直接按照充电站名称、开始时间、查询是否已经有一致数据 用于判断重复！！！
            # 直接查询该充电站的sid
            sql = "select sid from table_charge_station where station_name = %s"
            self.cursor.execute(sql, record[7])
            data = self.cursor.fetchall()
            sid = 0
            if len(data) != 0:
                sid = data[0][0]
                sql = "select sid from table_station_period where sid = %s and start_time = %s"
                self.cursor.execute(sql, [sid, record[0]])
                data = self.cursor.fetchall()
                if len(data) != 0:
                    self.send_info(-1)  # 发射信号
                    return
            if sid == 0: #防止充电站名称重复，在数据库里面
                # 插入一些直接能从excel表中直接获取的（名称，地址，经纬度，起始时间，），需要统计出来的（充电转中充电桩数量、交流充电桩数量、直流充电桩数量）等，就后面统计完再update进去表中
                sql = "insert into table_charge_station (station_name, station_addr, longitude, latitude, s_local, start_time) values (%s, %s, %s, %s, %s, %s)"
                list_station_fixed = [record[7], record[9], record[10], record[11], record[8], record[0]]
                self.cursor.execute(sql, list(list_station_fixed))
            self.connection.commit()
        except Exception as e:
            print("##########" + str(e) + "###########")
            self.send_info(1)  # 发射信号
            self.connection.rollback()
            return

        ##################################插入其余的数据######################################
        self.connection.begin()
        try:
            record_begin_time = ""  # 本次测量起始时间
            #record_end_time = ""  # 本次测量终止时间
            pid_count = 0  # 记录充电桩的数量
            period_count = 1  # 记录时间段的数量
            s_zhiliu_num = 0  # 直流充电桩数量
            s_jiaoliu_num = 0  # 交流充电桩数量
            tmp_pid = 0
            for record in list(data_df.values):
                time.sleep(0.05)  # 休眠时间 可调 -> 意思就是该线程放出cpu的时间，越小导入的数据的时长就越短！！！
                sql = "select sid from table_charge_station where station_name = %s"
                self.cursor.execute(sql, station_name)
                data = self.cursor.fetchall()
                sid = data[0][0]


                if type(record[6]) == str:
                    pid_count = pid_count + 1
                    period_count = 1
                    manufacturer = str(record[6])  # 生产厂家
                    factory_num = str(record[5])  # 出厂编号
                    model_type = str(record[4])  # 型号

                    pid_name = str(record[3])  # 充电桩名称
                    pid_addr = str(record[9])  # 充电桩地址

                    nomial_level = str(record[28])  # 标称等级
                    install_time_span = str(record[14])  # 安装时长
                    charge_pile_type = str(record[16])  # 充电桩种类
                    if charge_pile_type.split("充")[0] == "直流":
                        s_zhiliu_num = s_zhiliu_num + 1

                    else:
                        s_jiaoliu_num = s_jiaoliu_num + 1


                    carrieroperator = str(record[12])  # 运营商
                    start_time = str(record[0])  # 开始时间
                    record_begin_time = str(record[0]) # 开始时间
                    sql = "insert into table_charge_pile (sid, pid, pid_name, pid_addr, model_type, factory_num, nomial_level, install_time_span, carrieroperator, manufacturer, start_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(sql, list([sid, pid_count, pid_name, pid_addr, model_type, factory_num, nomial_level, install_time_span, carrieroperator, manufacturer, start_time]))
                else:
                    period_count = period_count + 1


                start_time = str(record[0])  # 测量开始时间
                end_time = str(record[1])  # 测量结束时间
                use_freq = str(record[46]) # 使用频率

                energy = None
                if str(record[35]) != 'nan':
                    energy = str(record[35])
                else:
                    energy = str(record[36])


                sql = "insert into table_pile_period (sid, pid, start_time, end_time, use_freq, energy) values (%s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql, list([sid, pid_count, start_time, end_time, use_freq, energy]))

                if pid_count == 1:
                    env_temper = str(record[29])  # 温度
                    env_shidu = str(record[30])  # 相对湿度
                    loss_energy = str(record[33])  # 损耗能量
                    total_energy = str(record[32])  # 总能量
                    sql = "insert into table_station_period (sid, start_time, end_time, env_temper, env_shidu, loss_energy, total_energy) values (%s, %s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(sql, list([sid, start_time, end_time, env_temper, env_shidu, loss_energy, total_energy]))
            #todo: 将得到的pid_count，s_jiaoliu_num，s_zhiliu_num以update的方式插入到表table_charge_station
            sql = "update table_charge_station set s_num = %s, s_zhiliu_num = %s, s_jiaoliu_num = %s  where sid = %s"
            self.cursor.execute(sql, list([pid_count, s_zhiliu_num, s_jiaoliu_num, sid]))

            #数据插入完 才将table_charge_station表中的s_flag至为1，其余时间都为0
            #sql = "update table_charge_station set s_flag = 1 where sid = %s"
            #cursor.execute(sql, sid)

            self.connection.commit()
            #self.send_info(0)  # 发射信号,这个信号就代表数据插入成功！

        except Exception as e:
            print("这是一个：" + str(e) + "的错误，请认真查看！")
            message = "第" + str(index + 2) + "行数据插入失败！请检查，然后重新导入"
            self.send_info(index + 2)  # 发射信号
            self.connection.rollback()
            return

        ##################################插入计算的计量误差与风险等级######################################
        # todo:加载数据之后开始计算测量误差和风险等级(尚未做)等参数并插入至数据库
        self.update_risk_level(station_name, record_begin_time, period_count)




    def update_risk_level(self, station_name, record_begin_time, period_count):
        dataProcess = DataProcess()
        list_A, list_B, sid = dataProcess.compute_energy_matrix(station_name, record_begin_time, period_count)
        result, isOnlyJie = dataProcess.compute_matrix(list_A, list_B)  # 充电桩计量误差数据，该数据需要被插入至 数据库table_pile_display_info表中  result为列表类型, isOnlyJie代表矩阵是否唯一解

        if not isOnlyJie:
            try:
                self.connection.begin()
                sql = "update table_charge_station set is_validity = 1 where sid = %s"
                self.cursor.execute(sql, [sid])
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                print("这是一个" + str(e) + "错误!")
            self.send_info(-2)  # 代表矩阵不是唯一解 发送给主页展示
            return
        risk_level = dataProcess.compute_risk_level(sid, result)
        try:
            self.connection.begin()
            #todo: 根据测量误差，计算出风险等级指数，然后一起推送至数据库
            pid = 1 # 给每个充电桩推送测量误差，
            for measure_error in list(result):
                measure_error_str = str(round(measure_error, 2))  # 只保留两位小数
                # insert不能插入一个属性， 必须插入多个属性， 用update语句更新一个属性的值 代表插入
                sql = "update table_charge_pile set measurement_error = %s, risk_level = %s where start_time = %s and sid = %s and pid = %s"
                self.cursor.execute(sql, [measure_error_str, risk_level[pid - 1], record_begin_time, sid, pid])
                pid = pid + 1
            self.connection.commit()
            self.send_info(0)  # 发射信号,这个信号就代表数据插入成功！

        except Exception as e:
            self.connection.rollback()
            print("这是一个" + str(e) + "错误!")
        finally:
            # 关闭数据库连接和钩子
            close_db(self.connection, self.cursor)



    def send_info(self, info):
        show_info = ShowInfo(info)
        self.show_info_signal.emit(show_info)


