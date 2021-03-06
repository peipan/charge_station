from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import pyqtSlot, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication

from Common import get_db_connection, get_logger, show_information_message, execute_inquiry, \
    get_row_model
from MapDisplay import MapDisplay
from PlotSubWindow import PlotSubWindow
from UI.Ui_PlotWindow import Ui_PlotWindow
from mapper.ChargeMapper import ChargeMapper


class PlotWindow(QMainWindow):
    sense_station_change = pyqtSignal(str)  # 定义一个信号槽 用于感知充电站的变化  充电桩的列表野随着变化

    def __init__(self, parent=None):
        super(PlotWindow, self).__init__(parent)
        self.UI = Ui_PlotWindow()
        self.UI.setupUi(self)

        #########################网页便签页格式展示####################

        # self.setCentralWidget(self.UI.tabWidget)  # 将 tabwidget 设为中心控件
        self.UI.tabWidget.setVisible(False)  # 线隐藏 tabwidget 控件
        self.UI.tabWidget.clear()  # 清除所有的页
        self.UI.tabWidget.setTabsClosable(True)  # Page有关闭按钮
        self.UI.tabWidget.setDocumentMode(True)  # 设置文档模式

        ###########################################################

        self.mapDisplay = MapDisplay(self)  # 为什么放在这，这就是解决点击按钮  弹框一下就关了的bug......... https://blog.csdn.net/veloi/article/details/115027549这里面的方法二
        self.mapDisplay.close()

        self.chargeMapper = ChargeMapper()  # 注入操作数据库类

        self.logger = get_logger("plot")

        # 初始化左边表格栏参数
        # self.init_plot_type()

        '''
        ##################################加tableView功能######################
        self.init_model = None
        init_tableview(self.UI.tableView, hor_size=25, ver_size=25)
        self.get_initial_model()
        data_model = self.init_model
        selection_model = QItemSelectionModel(data_model)

        self.UI.tableView.setModel(data_model)
        self.UI.tableView.setSelectionModel(selection_model)
        # 设置表格充满这个布局QHeaderView
        self.UI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.UI.tableView.selectionModel().currentRowChanged.connect(self.do_cur_row_change)
        #####################################################################
        '''

        self.connection, self.cursor = get_db_connection()

    # 接收行切换
    @pyqtSlot(QModelIndex, QModelIndex)
    def do_cur_row_change(self, cur: QModelIndex, pre: QModelIndex):
        self.cur_row = cur.row()

    '''
    #add
    def setValue(self):
        self.sense_station_change.emit(str(self.UI.comboBox_type_station.currentText()))

    def getValue(self, station_name):
        pid_type = self.chargeMapper.find_all_pid_by_charge_name(station_name)
        period_type = self.chargeMapper.find_all_period_by_charge_name(station_name)
        # 需要将pid_type转成str
        for i in range(0, len(pid_type)):
            pid_type[i] = str(pid_type[i])
        #先清空 在add
        self.UI.comboBox_type_pile.clear()
        self.UI.comboBox_type_pile.addItems(pid_type)

        # 先清空 在add
        self.UI.comboBox_type_time.clear()
        self.UI.comboBox_type_time.addItems(period_type)
    '''

    #
    # 生产厂家展示按钮
    @pyqtSlot()
    def on_btn_factory_clicked(self):
        new_sid = self.chargeMapper.find_newest_sid() #todo： 这个得取出来，也就是先取最新的sid数据，还得判断s刚插入的sid是否矩阵运算有唯一值，如果没有唯一值 就显示不了呀，或者就显示前一次的数据，这种直接在表中加一个标记位就可以
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        data = self.chargeMapper.find_manufacturer_and_risk_index(sid = new_sid)  # row：表示横坐标，line1-2-3：列坐标，分别表示高中低
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        line = list([])
        row = list([])
        line1 = list([])
        line2 = list([])
        line3 = list([])
        for i in range(0, len(data)):
            row.append(data[i][0])
            line1.append(data[i][1])
            line2.append(data[i][2])
            line3.append(data[i][3])

        line.append(line1)
        line.append(line2)
        line.append(line3)

        plot_type = 0  # 1代表是折线图 0代表柱状图
        type_label = "生产厂家"

        ##########################表格显示，数据转换，数据库取出格式->tableView表格形式######################################
        #################manufacturer	risk_level	count(risk_level)                      最高      平均      最低 ###
        ########北京华商三优科技有限公司	33	1 ########     ########  北京华商三优科技有限公司        0        1        0  ###
        ########智充科技有限公司	34	1     ########  -> ########  智充科技有限公司              0        1        0  ###
        ########特来电	35	1             ########     ########  特来电                      0        1        0  ###
        ret_data = self.chargeMapper.find_manufacturer_and_nums(new_sid)
        data0 = list([])
        manufacturer = ""
        highest = 0
        avg = 0
        lowest = 0
        for i in range(0, len(ret_data)):
            temp = list([])
            risk_index = ret_data[i][1]
            count_risk = ret_data[i][2]
            if manufacturer == ret_data[i][0]:         # 判断相邻俩行生产厂家是否是同一个，是同一个直接在那一个的基础上加数量就行
                if risk_index > 80:
                    highest = highest + count_risk
                elif risk_index < 30:
                    lowest = lowest + count_risk
                else:
                    avg = avg + count_risk
            else:                                  ## 判断相邻俩行生产厂家是否是同一个，不是的话  就把前面的装进data0，然后重新再开始一个生产厂家的统计
                if manufacturer != "":
                    temp.append(manufacturer)
                    temp.append(highest)
                    temp.append(avg)
                    temp.append(lowest)
                    data0.append(temp)
                highest = 0
                avg = 0
                lowest = 0
                if risk_index > 80:
                    highest = count_risk
                elif risk_index < 30:
                    lowest = count_risk
                else:
                    avg = count_risk
            if i == len(ret_data) - 1:  # 最后一行数据的处理，有两种情况：1.最后一行就是单独的一个生产厂家  2.最后一行与之前是一个生产厂家
                temp = list([])
                temp.append(ret_data[i][0])
                temp.append(highest)
                temp.append(avg)
                temp.append(lowest)
                data0.append(temp)
            manufacturer = ret_data[i][0]
        ##########################表格显示，数据转换，数据库取出格式->tableView表格形式######################################

        window = None
        if row is None:
            window = PlotSubWindow()
            curindex = self.UI.tabWidget.addTab(window, "没有数据404")
        else:
            window = PlotSubWindow(plot_type=plot_type, row=row, line=line, data=data0, type_label=type_label)
            curindex = self.UI.tabWidget.addTab(window, type_label)
        window.setAttribute(Qt.WA_DeleteOnClose)
        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)

    # 使用频率展示按钮
    @pyqtSlot()
    def on_btn_frequency_clicked(self):
        new_sid = self.chargeMapper.find_newest_sid()
        # todo: 从数据库取出使用频率与风险等级标量的关系
        data = self.chargeMapper.find_use_freq_and_risk_index(new_sid)
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        plot_type = 1

        line = list([])
        row = list([])
        line1 = list([])
        line2 = list([])
        line3 = list([])
        for i in range(0, len(data)):
            row.append(data[i][0])
            line1.append(data[i][1])
            line2.append(data[i][2])
            line3.append(data[i][3])

        line.append(line1)
        line.append(line2)
        line.append(line3)

        type_label = "使用频率"

        window = None
        if row is None:
            window = PlotSubWindow()
            curindex = self.UI.tabWidget.addTab(window, "没有数据404")
        else:
            window = PlotSubWindow(plot_type=plot_type, row=row, line=line, data=None, type_label=type_label)
            curindex = self.UI.tabWidget.addTab(window, type_label)
        window.setAttribute(Qt.WA_DeleteOnClose)

        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)

    # 环境温度展示按钮
    @pyqtSlot()
    def on_btn_tem_clicked(self):
        new_sid = self.chargeMapper.find_newest_sid()  # todo： 这个得取出来，也就是先取最新的sid数据，还得判断s刚插入的sid是否矩阵运算有唯一值，如果没有唯一值 就显示不了呀，或者就显示前一次的数据，这种直接在表中加一个标记位就可以
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        data = self.chargeMapper.find_env_temper_and_risk_index(new_sid)
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        plot_type = 1

        line = list([])
        row = list([])
        line1 = list([])
        line2 = list([])
        line3 = list([])
        for i in range(0, len(data)):
            row.append(data[i][0])
            line1.append(data[i][1])
            line2.append(data[i][2])
            line3.append(data[i][3])

        line.append(line1)
        line.append(line2)
        line.append(line3)

        type_label = "温度"
        window = None
        if row is None:
            window = PlotSubWindow()
            curindex = self.UI.tabWidget.addTab(window, "没有数据404")
        else:
            window = PlotSubWindow(plot_type=plot_type, row=row, line=line, data=None, type_label=type_label)
            curindex = self.UI.tabWidget.addTab(window, type_label)
        window.setAttribute(Qt.WA_DeleteOnClose)

        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)

    # 运营商展示按钮
    @pyqtSlot()
    def on_btn_temp_clicked(self):
        new_sid = self.chargeMapper.find_newest_sid()  # todo： 这个得取出来，也就是先取最新的sid数据，还得判断s刚插入的sid是否矩阵运算有唯一值，如果没有唯一值 就显示不了呀，或者就显示前一次的数据，这种直接在表中加一个标记位就可以
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        data = self.chargeMapper.find_carrieroperator_and_risk_index(new_sid)
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        plot_type = 0
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        line = list([])
        row = list([])
        line1 = list([])
        line2 = list([])
        line3 = list([])
        for i in range(0, len(data)):
            row.append(data[i][0])
            line1.append(data[i][1])
            line2.append(data[i][2])
            line3.append(data[i][3])

        line.append(line1)
        line.append(line2)
        line.append(line3)
        type_label = "运营商"

        ##########################表格显示，数据转换，数据库取出格式->tableView表格形式######################################
        ret_data = self.chargeMapper.find_carrieroperator_and_nums(new_sid)
        data0 = list([])
        carrieroperator = ""
        highest = 0
        avg = 0
        lowest = 0
        for i in range(0, len(ret_data)):
            temp = list([])
            risk_index = ret_data[i][1]
            count_risk = ret_data[i][2]
            if carrieroperator == ret_data[i][0]:
                if risk_index > 80:
                    highest = highest + count_risk
                elif risk_index < 30:
                    lowest = lowest + count_risk
                else:
                    avg = avg + count_risk
            else:
                if carrieroperator != "":
                    temp.append(carrieroperator)
                    temp.append(highest)
                    temp.append(avg)
                    temp.append(lowest)
                    data0.append(temp)
                highest = 0
                avg = 0
                lowest = 0
                if risk_index > 80:
                    highest = count_risk
                elif risk_index < 30:
                    lowest = count_risk
                else:
                    avg = count_risk
            if i == len(ret_data) - 1:
                temp = list([])
                temp.append(ret_data[i][0])
                temp.append(highest)
                temp.append(avg)
                temp.append(lowest)
                data0.append(temp)
            carrieroperator = ret_data[i][0]
        ##########################表格显示，数据转换，数据库取出格式->tableView表格形式######################################

        window = None
        if row is None:
            window = PlotSubWindow()
            curindex = self.UI.tabWidget.addTab(window, "没有数据404")
        else:
            window = PlotSubWindow(plot_type=plot_type, row=row, line=line, data=data0, type_label=type_label)
            curindex = self.UI.tabWidget.addTab(window, type_label)
        window.setAttribute(Qt.WA_DeleteOnClose)

        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)

    # 安装时长展示按钮
    @pyqtSlot()
    def on_btn_time_clicked(self):
        new_sid = self.chargeMapper.find_newest_sid()  # todo： 这个得取出来，也就是先取最新的sid数据，还得判断s刚插入的sid是否矩阵运算有唯一值，如果没有唯一值 就显示不了呀，或者就显示前一次的数据，这种直接在表中加一个标记位就可以
        # todo: 从数据库取出安装时长与风险等级标量的关系
        data = self.chargeMapper.find_install_span_and_risk_index(new_sid)
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        plot_type = 1
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        line = list([])
        row = list([])
        line1 = list([])
        line2 = list([])
        line3 = list([])
        for i in range(0, len(data)):
            row.append(data[i][0])
            line1.append(data[i][1])
            line2.append(data[i][2])
            line3.append(data[i][3])

        line.append(line1)
        line.append(line2)
        line.append(line3)

        type_label = "安装时长"
        ##########################表格显示，数据转换，数据库取出格式->tableView表格形式######################################
        ret_data = self.chargeMapper.find_install_span_and_nums(new_sid)
        data0 = list([])
        install_time = -1
        highest = 0
        avg = 0
        lowest = 0
        for i in range(0, len(ret_data)):
            temp = list([])
            risk_index = ret_data[i][1]
            count_risk = ret_data[i][2]
            if install_time == ret_data[i][0]:
                if risk_index > 80:
                    highest = highest + count_risk
                elif risk_index < 30:
                    lowest = lowest + count_risk
                else:
                    avg = avg + count_risk
            else:
                if install_time != -1:
                    temp.append(install_time)
                    temp.append(highest)
                    temp.append(avg)
                    temp.append(lowest)
                    data0.append(temp)
                highest = 0
                avg = 0
                lowest = 0
                if risk_index > 80:
                    highest = count_risk
                elif risk_index < 30:
                    lowest = count_risk
                else:
                    avg = count_risk
            if i == len(ret_data) - 1:
                temp = list([])
                temp.append(ret_data[i][0])
                temp.append(highest)
                temp.append(avg)
                temp.append(lowest)
                data0.append(temp)
            install_time = ret_data[i][0]
        ##########################表格显示，数据转换，数据库取出格式->tableView表格形式######################################
        window = None
        if row is None:
            window = PlotSubWindow()
            curindex = self.UI.tabWidget.addTab(window, "没有数据404")
        else:
            window = PlotSubWindow(plot_type=plot_type, row=row, line=line, data=data0, type_label=type_label)
            curindex = self.UI.tabWidget.addTab(window, type_label)
        window.setAttribute(Qt.WA_DeleteOnClose)

        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)




    # 获取画图的类型（折线/柱状， 横纵坐标：row, line）
    def get_plot_type_and_row_and_line(self):
        plot_type = self.get_plot_line_or_pie()
        type_label, row, line = self.get_plot_row_and_line()

        return plot_type, row, line, type_label


    # 获取横纵坐标值返回list类型
    def get_plot_row_and_line(self):
        type_label = self.get_plot_type().split('-')[0]

        # todo: 需要根据充电站还有充电桩确定，所以先得到充电站sid，再次得到充电桩pid，然后就是画出该充电桩的数据画图了
        sid, pid, begin_time, end_time = self.get_plot_sid_and_pid_and_period()
        if sid == -1:
            return None, None, None
        x = None
        values = None
        # todo:添加一个字典直接根据type获取SQL语句
        map = {'安装时长': 'use_freq', '风险等级': 'risk_level', '环境温度': 'Measurement_error'}
        table_line_attr = map[type_label]
        if table_line_attr == 'use_freq':
            x, values = self.chargeMapper.find_plot_attr_by_sid_and_pid_and_period(table_line_attr=table_line_attr,
                                                                                   sid=sid, pid=pid,
                                                                                   begin_time=begin_time,
                                                                                   end_time=end_time)
        elif table_line_attr == 'Measurement_error':
            x, values = self.chargeMapper.find_error_by_sid_and_pid_and_period(table_line_attr=table_line_attr, sid=sid,
                                                                               pid=pid)

        return type_label, x, values

    # 获取数据可视化的对象：充电站与充电桩 返回sid 和 pid
    '''
    def get_plot_sid_and_pid_and_period(self):
        station_name = self.UI.comboBox_type_station.currentText()
        if station_name == '':
            #todo: waring 请先导入数据
            return -1, -1, None, None
        sid = self.chargeMapper.find_sid_by_charge_name(station_name)
        pid = int(self.UI.comboBox_type_pile.currentText())
        period = self.UI.comboBox_type_time.currentText()
        begin_time = period.split('~')[0]
        end_time = period.split('~')[1]
        return sid, pid, begin_time, end_time
    '''

    # 获取数据
    def get_data(self, sql, arg=None):
        connection, cursor = get_db_connection()
        data = execute_inquiry(sql, arg, connection=connection, cursor=cursor)
        if data == -1:
            show_information_message("查询结果为空")
            return

        return data

    # 单击画图按钮
    @pyqtSlot()
    def on_btn_plot_clicked(self):
        # todo: 获取此时的列表数据，有plot_type: int, row: list, line: list, type_label: str,
        plot_type, row, line, type_label = self.get_plot_type_and_row_and_line()
        window = None
        if row is None:
            window = PlotSubWindow()
            curindex = self.UI.tabWidget.addTab(window, "没有数据404")
        else:
            window = PlotSubWindow(plot_type=plot_type, row=row, line=line, type_label=type_label)
            curindex = self.UI.tabWidget.addTab(window, type_label)
        window.setAttribute(Qt.WA_DeleteOnClose)

        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)

    # 初始化画图参数
    '''
    def init_plot_type(self):
        type_dict = get_plot_type()
        self.plot_type = [(key.split('_')[0] if '_' in key else key, type_dict.get(key))
                            for key in type_dict]
        type = [i[1] for i in self.plot_type]

        self.UI.comboBox_type_pie.addItems(type)
        # 充电站与对应的充电桩需要从数据库读取，动态的读取，并且充电桩的comboBox随着充电站的变化而变化
        # 重构代码的时候考虑采用MVC模式，不然代码写的非常杂
        station = list([])
        station_type = self.chargeMapper.find_all_charge_name()
        if len(station_type) == 0:
            return
        self.UI.comboBox_type_station.addItems(station_type)
    '''

    # 关闭分页请求函数
    @pyqtSlot(int)
    def on_tabWidget_tabCloseRequested(self, index):
        if index < 0:
            return
        else:
            # 获取关闭的页面
            page = self.UI.tabWidget.widget(index)
            # 关闭该页面
            page.close()

    # 获取最初的数据模型
    def get_initial_model(self):
        head = list(['充电站名称', '充电桩数量'])
        model = get_row_model(2, header=head)
        all_name, all_pid = self.chargeMapper.find_chargeName_and_pidCount()
        row = list([])
        line = list([])
        data = [row, line]
        for i in range(0, len(all_name)):
            data[i].append(all_name[i])
            data[i].append(all_pid[i])

        self.init_model = self.add_data(model, data)

"""    # 向模型添加数据
    def add_data(self, model: QStandardItemModel, data) -> QStandardItemModel:
        for i in data:
            row = []
            for j in range(len(i)):
                item = QStandardItem(str(i[j]))
                row.append(item)
            model.appendRow(row)
        return model
"""


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = PlotWindow()
    win.show()
    sys.exit(app.exec())
