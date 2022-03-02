from Common import get_plot_type, get_db_connection, close_db, get_logger, show_information_message, execute_inquiry, \
    get_row_model, init_tableview

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QHeaderView, QFileDialog

from PyQt5.QtGui import QStandardItem, QStandardItemModel

from PyQt5.QtCore import pyqtSlot, QItemSelectionModel, QModelIndex

from PlotSubWindow import PlotSubWindow

from UI.Ui_PlotWindow import Ui_PlotWindow

from mapper.ChargeMapper import ChargeMapper

from MapDisplay import MapDisplay

from graphyWindow import visual_all

from PyQt5.QtCore import Qt, pyqtSignal


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

        '''
        #add 利用信号的方式
        self.UI.comboBox_type_station.currentTextChanged.connect(self.setValue)
        self.sense_station_change.connect(self.getValue)
        #
        '''

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
        new_sid = 0  #todo： 这个得取出来，也就是先取最新的sid数据，还得判断s刚插入的sid是否矩阵运算有唯一值，如果没有唯一值 就显示不了呀，或者就显示前一次的数据，这种直接在表中加一个标记位就可以
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        '''
        row, line1, line2, line3 = self.chargeMapper.find_manufacturer_and_risk_index(sid = new_sid)  # row：表示横坐标，line1-2-3：列坐标，分别表示高中低
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
        line = list([])
        line.append(line1)
        line.append(line2)
        line.append(line3)
        '''
        row = None
        plot_type = 0  # 0代表是折线图 1代表柱状图
        type_label = "生产厂家"
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

    # 使用频率展示按钮
    @pyqtSlot()
    def on_btn_frequency_clicked(self):
        # todo: 从数据库取出使用频率与风险等级标量的关系

        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
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

    # 环境温度展示按钮
    @pyqtSlot()
    def on_btn_tem_clicked(self):
        # todo: 从数据库取出生产厂家与风险等级标量的关系

        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
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

    # 运营商展示按钮
    @pyqtSlot()
    def on_btn_temp_clicked(self):
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
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

    # 安装时长展示按钮
    @pyqtSlot()
    def on_btn_time_clicked(self):
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
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

    # 其他因素展示按钮
    @pyqtSlot()
    def on_btn_other_clicked(self):
        # todo: 从数据库取出生产厂家与风险等级标量的关系
        # 按照之前的做法，已经封装了一个专门的PlotSubWindow,在这里可以传数据进这个类然后在这个Tab内中进行展示
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

    # 下载导出高风险等级充电桩的数据文件 .txt (huang)
    @pyqtSlot()
    def on_btn_load_clicked(self):
        file_path = QFileDialog.getSaveFileName(self, "save file", "E:/", "Txt files(*.txt)")  # 这里的file_name是tuple型
        # todo: 也就是从数据库取出相应的数据，然后保存至txt文件中

        lists = [[1, 2, 3, 4], [45, 23, 456, 23, 54, 23], [12, 23, 23, 345, 23, 12]]
        self.Save_list(lists, file_path[0])  # 取tuple第一个元素即为地址
        print('high_risk')

    # 地图风险等级展示按钮
    @pyqtSlot()
    def on_btn_risk_graphy_display_clicked(self):
        '''
        charge_name = self.UI.comboBox_type_station.currentText()
        sid = self.chargeMapper.find_sid_by_charge_name(charge_name)
        # 先获得经纬度数据,是一个数组类型，可能需要将数据强转float
        longitude_and_latitude = self.chargeMapper.find_longitude_and_latitude_by_charge_name(sid)
        #获取该充电站下的pid以及对应的风险等级数据，返回一个字典类型
        pid_and_risk_level_dict = self.chargeMapper.find_pid_risk_level_by_sid(sid)
        '''
        # todo:外弹框 显示地图就ok，我需要把经纬度数据填入
        add = [[39.873079, 116.481913], [39.913904, 116.39728], [39.885987, 116.480132]]
        level = [[10, 30, 50, 70, 90], [10, 10, 10, 10, 10], [90, 90, 90, 90, 90]]
        data = visual_all(add, *level)

        # mapDisplay = MapDisplay(data)
        self.mapDisplay.trans_data(data)
        # self.mapDisplay.setAttribute(Qt.WA_DeleteOnClose)  # 设置关闭删除实例  应该是这句话一直出现了bug
        self.mapDisplay.setWindowFlag(Qt.Window, True)  # 指示该窗口是一个独立的窗口
        # mapDisplay.exec()  #Qwidths没有模态窗口选项
        self.mapDisplay.show()

    @pyqtSlot(str)
    def recive_station_change(self, station_name):
        pass

    # 获取画图的类型
    def get_plot_type(self):
        return self.UI.comboBox_type_pie.currentText()

    # 获取画图的类型（折线/柱状， 横纵坐标：row, line）
    def get_plot_type_and_row_and_line(self):
        plot_type = self.get_plot_line_or_pie()
        type_label, row, line = self.get_plot_row_and_line()

        return plot_type, row, line, type_label

    # 获得画图的类型 是否是折线图或者是饼状图
    def get_plot_line_or_pie(self):
        if self.UI.pieCheckBox.isChecked() is True or self.UI.lineCheckBox_2.isChecked() is False:
            return 1  # 代表说折线图
        elif self.UI.pieCheckBox.isChecked() is False or self.UI.lineCheckBox_2.isChecked() is True:
            return 0  # 代表是饼状图
        else:
            # todo: 提示只能选择一项
            pass

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
