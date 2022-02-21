#该文件主要用与与充电站表（table_charge_station）进行数据交互作用
from Common import get_db_connection, execute_inquiry, show_information_message

class ChargeMapper():
    def __init__(self):
        self.connection, self.cursor = get_db_connection()

    #查找所有充电桩以及该充电桩数量
    def find_chargeName_and_pidCount(self):
        all_name = self.find_all_charge_name()
        all_pid = list([])
        sql = "select count(pid) from table_pile_display_info where sid = %s"
        for c_name in all_name:
            sid = self.find_sid_by_charge_name(c_name)
            *_, data = execute_inquiry(sql, arg=[sid], connection=self.connection, cursor=self.cursor)
            all_pid.append(data[0][0])
        return all_name, all_pid


    #查找所有的充电站名称
    def find_all_charge_name(self) -> list:
        sql = "select station_name from table_charge_station where s_flag = 1"
        data = []
        all_sid = list([])
        *_, data = execute_inquiry(sql, arg=None, connection=self.connection, cursor=self.cursor)
        if data is None:
            return all_sid
        for i in range(0, len(data)):
            all_sid.append(data[i][0])
        return all_sid

    #通过充电站名称查找充电站序列sid  updated
    def find_sid_by_charge_name(self, charge_name: str) -> int:
        sql = "select sid from table_charge_station where station_name = %s"
        data = []
        #注意了，data类型一般就是[[sid,]]类型
        *_, data = execute_inquiry(sql, charge_name, connection=self.connection, cursor=self.cursor)
        return int(data[0][0])

    #通过充电站名称查找充电桩所有数据
    def find_all_pid_by_charge_name(self, charge_name: str) -> list:
        #首先找到该充电桩的sid
        sid = self.find_sid_by_charge_name(charge_name=charge_name)
        #再根据sid查找所有pid
        all_pid = list([])
        data = []
        sql = "select pid from table_charge_pile where sid = %s group by pid"
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        for i in range(0, len(data)):
            all_pid.append(data[i][0])
        return all_pid

    # 通过充电站名称查找该充电站所有时间段
    def find_all_period_by_charge_name(self, charge_name):
        # 首先找到该充电桩的sid
        sid = self.find_sid_by_charge_name(charge_name=charge_name)
        all_period = list([])
        data = []
        sql = "select begin_time, end_time from table_pile_display_info where sid = %s group by begin_time"
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        for i in range(0, len(data)):
            all_period.append(str(data[i][0]) + '~' + str(data[i][1]))
        return all_period

    ######################################画图的主要与数据库交互的函数###########################################
    #根据sid，pid查询表中列（该列为变量）数据 ,将data数据获取，处理成横纵坐标就留给其他地方处理
    def find_plot_attr_by_sid_and_pid_and_period(self, table_line_attr: str, sid: int, pid: int, begin_time: str, end_time: str):
        data = []
        sql = "select " + table_line_attr + ", start_time, end_time from table_charge_pile where sid = %s and pid = %s and start_time >= %s and end_time <= %s"  #拼接字符串会产生sql注入问题？  按理说应该不会，因为在from前面
        *_, data = execute_inquiry(sql, [sid, pid, begin_time, end_time], connection=self.connection, cursor=self.cursor)
        if data == -1:
            show_information_message("查询结果为空")
            return
        #数据处理，直接返回，横轴坐标，统一在这边处理
        values = list([])  # 纵轴
        x = list([])  # 横轴
        for i in range(0, len(data)):
            values.append(data[i][0])
            #x.append(str(data[i][1]) + "-" + str(data[i][2])) #这样写法 横坐标填满了，不好看
            x.append(str(i))
        return x, values

    # 根据sid，pid查询表table_pile_display_info中列（该列为变量）数据 ,将data数据获取，处理成横纵坐标就留给其他地方处理  纵坐标为 error 横坐标为 次数吧 （显示时间段太难看）
    def find_error_by_sid_and_pid_and_period(self, table_line_attr: str, sid: int, pid: int):
        data = []
        sql = "select " + table_line_attr + " from table_pile_display_info where sid = %s and pid = %s order by begin_time"
        *_, data = execute_inquiry(sql, [sid, pid], connection=self.connection, cursor=self.cursor)
        if data == -1:
            show_information_message("查询结果为空")
            return
        # 数据处理，直接返回，横轴坐标，统一在这边处理
        values = list([])  # 纵轴
        x = list([])  # 横轴
        for i in range(0, len(data)):
            values.append(data[i][0])
            x.append(str((i+1)*10.1))
        return x, values
    ######################################画图的主要与数据库交互的函数###########################################


    #根据充电站sid获得经纬度数据
    def find_longitude_and_latitude_by_charge_name(self, sid: int):
        sql = "select longitude, latitude from table_charge_station where sid = %s"
        data = []
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        return data[0] #[[1141,111111, [1221.222222]],]data这是个二维数组形式，注意一下

    #根据充电站sid获取该充电桩的所有pid以及相应的风险等级，返回字典类型
    def find_pid_risk_level_by_sid(self, sid: int):
        sql = "select pid, risk_level from table_charge_pile where sid = %s order by pid"
        data = []
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        #将二维数组转换为字典类型{x:y, m:n}
        res = {}
        for i in range(0, len(data)):
            res[data[i][0]] = data[i][1]
        return res

    ###########################################矩阵计算##############################################
    #根据根据数据库sid,begin_time,end_time查找“北工大充电桩”的pid的总数  待完善 ->已完善
    '''
    def find_count_pid_by_sid_and_period(self, sid: int, begin_time: str, end_time: str) -> int:
        sql = "select count(1) FROM (SELECT DISTINCT pid FROM table_pile_display_info WHERE sid = %s and begin_time = %s and end_time = %s) AS p;"
        data = []
        *_, data = execute_inquiry(sql, [sid, begin_time, end_time], connection=self.connection, cursor=self.cursor)
        return data[0][0]
    '''
    # 根据根据数据库sid,begin_time,end_time查找“北工大充电桩”的pid的总数  待完善 ->已完善  updated
    def find_count_pid_by_sid_and_period(self, sid: int) -> int:
        sql = "select s_num from table_charge_station where sid = %s"
        data = []
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        return data[0][0]

    #查找充电桩表中的每个充电桩在一个时间段内的能量数据  充电桩 在时段 的电能计量数据  但是现在是取出所有  有dataProcess类去处理形成二维矩阵
    #按照时间顺序 以及pid序号的顺序返回  updated
    def find_station_all_energy_by_sid_and_period(self, sid: int, begin_time: str, limit_num: int):
        sql = "SELECT energy FROM table_pile_period WHERE sid = %s AND start_time >= %s ORDER BY start_time, pid LIMIT %s"
        list_energy = []
        *_, list_energy = execute_inquiry(sql, [sid, begin_time, limit_num], connection=self.connection, cursor=self.cursor)
        return list_energy

    #根据sid查找table_station_period表中的total_energy返回一个数组 按照时段排序  E1,E2…Et为充电站所有充电桩不同时段 的总电能数据 updated
    def find_total_energy_by_sid_and_period(self, sid, begin_time, limit_period):
        sql = "select total_energy from table_station_period where sid = %s and start_time >= %s order by start_time limit %s"
        data = []
        *_, data = execute_inquiry(sql, [sid, begin_time, limit_period], connection=self.connection, cursor=self.cursor)
        return data

    #根据sid查找充电桩的损耗能量数据，返回一个数组  再从table_charge_pile表中查找充电桩损耗能量E0应该是代表该时段所有充电桩的的损耗数据总和（求E0）  暂时这么理解
    #根据sid查找table_station_period表中的loss_energy返回一个数组 按照时段排序 updated
    def find_loss_energy_by_sid_and_period(self, sid, begin_time, limit_period):
        #sql = "SELECT SUM(loss_energy) FROM table_charge_pile WHERE sid = %s and start_time >= %s GROUP BY start_time"
        sql = "select loss_energy from table_station_period where sid = %s and start_time >= %s order by start_time limit %s"
        data = []
        *_, data = execute_inquiry(sql, [sid, begin_time, limit_period], connection=self.connection, cursor=self.cursor)
        return data
    ###########################################矩阵计算##############################################


    #根据pid和sid从数据库中查找误差数据、充电桩安装时长、使用频率、环境温度、环境湿度、运营商维护次数等等, 返回一个一维数组   注意：目前数据库中差一个环境湿度的列..2021/12/5
    def find_risk_factors_by_pid_and_sid(self, sid, pid):
        sql = "select measurement_error, use_freq, env_temper, maintain_freq from table_charge_pile where sid = %s and pid = %s"
        data = []
        *_, data = execute_inquiry(sql, [sid, pid], connection=self.connection, cursor=self.cursor)
        return data[0]


    ##########################################图形展示页面与数据库交互的代码 2022/02/21 peipan##################################################
    #安装时长与风险等级指数的关系，返回x轴参数、最低指数、平均指数、最高指数
    def find_install_span_and_risk_index(self, sid: int):
        sql = "select install_time_span, min(risk_level), avg(risk_level), max(risk_level) from table_charge_pile where sid = %s group by install_time_span"
        data = []
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        return data[0], data[1], data[2], data[3]

    #运营商与风险等级指数的关系，返回x轴参数、最低指数、平均指数、最高指数
    def find_carrieroperator_and_risk_index(self, sid: int):
        sql = "select carrieroperator, min(risk_level), avg(risk_level), max(risk_level) from table_charge_pile where sid = %s group by carrieroperator"
        data = []
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        return data[0], data[1], data[2], data[3]

    #生产厂家与风险等级指数的关系，返回x轴参数、最低指数、平均指数、最高指数
    def find_manufacturer_and_risk_index(self, sid: int):
        sql = "select manufacturer, min(risk_level), avg(risk_level), max(risk_level) from table_charge_pile where sid = %s group by manufacturer"
        data = []
        *_, data = execute_inquiry(sql, sid, connection=self.connection, cursor=self.cursor)
        return data[0], data[1], data[2], data[3]

    #使用频率与风险等级指数的关系，返回x轴参数、最低指数、平均指数、最高指数
    def find_use_freq_and_risk_index(self, sid: int):
        sql = ""

    ####################################################################################################################