from Common import get_plot_type, get_db_connection, close_db, get_logger, show_information_message, execute_inquiry

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout

from PyQt5.QtCore import pyqtSlot

from Util.Plot import Myplot2D

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

        # add 利用信号的方式
        self.UI.comboBox_type_station.currentTextChanged.connect(self.setValue)
        self.sense_station_change.connect(self.getValue)
        #

        self.mapDisplay = MapDisplay(
            self)  # 为什么放在这，这就是解决点击按钮  弹框一下就关了的bug......... https://blog.csdn.net/veloi/article/details/115027549这里面的方法二
        self.mapDisplay.close()

        self.chargeMapper = ChargeMapper()  # 注入操作数据库类

        self.fig_line = None
        self.fig_pie = None
        self.plot_type = None
        self.logger = get_logger("plot")

        self.init_plot_frame()
        self.init_plot_type()
        self.connection, self.cursor = get_db_connection()

    # add
    def setValue(self):
        self.sense_station_change.emit(str(self.UI.comboBox_type_station.currentText()))

    def getValue(self, station_name):
        pid_type = self.chargeMapper.find_all_pid_by_charge_name(station_name)
        period_type = self.chargeMapper.find_all_period_by_charge_name(station_name)
        # 需要将pid_type转成str
        for i in range(0, len(pid_type)):
            pid_type[i] = str(pid_type[i])
        # 先清空 在add
        self.UI.comboBox_type_pile.clear()
        self.UI.comboBox_type_pile.addItems(pid_type)

        # 先清空 在add
        self.UI.comboBox_type_times.clear()
        self.UI.comboBox_type_times.addItems(period_type)

    #

    # 初始化画图区域
    def init_plot_frame(self):
        self.fig_line = Myplot2D()
        tool1 = NavigationToolbar(self.fig_line, self.UI.frame_5)
        layout = QGridLayout()
        layout.addWidget(self.fig_line)
        layout.addWidget(tool1)
        self.UI.frame_5.setLayout(layout)

        self.fig_pie = Myplot2D()
        tool2 = NavigationToolbar(self.fig_pie, self.UI.frame_6)
        layout = QGridLayout()
        layout.addWidget(self.fig_pie)
        layout.addWidget(tool2)
        self.UI.frame_6.setLayout(layout)

    # 初始化画图参数
    def init_plot_type(self):
        type_dict = get_plot_type()
        self.plot_type = [(key.split('_')[0] if '_' in key else key, type_dict.get(key))
                          for key in type_dict]
        type = [i[1] for i in self.plot_type]

        self.UI.comboBox_type_pie.addItems(type)
        self.UI.comboBox_type_line.addItems(type)

        # 充电站与对应的充电桩需要从数据库读取，动态的读取，并且充电桩的comboBox随着充电站的变化而变化
        # 重构代码的时候考虑采用MVC模式，不然代码写的非常杂
        station = list([])
        station_type = self.chargeMapper.find_all_charge_name()
        if len(station_type) == 0:
            return
        self.UI.comboBox_type_station.addItems(station_type)

        # 根据充电站 确定pid的comboBox
        # 这块可能存在一个bug，就是这个函数就是初始化调用的，那如果我们改变了充电站，选择充电桩的box里面的数据也得随着变化，
        # 解决思路：1：可以再封装一个函数，做只要充电站变化，充电桩box随着改变
        #         2：或者固定最大的16，然后写逻辑判断即可  待解决：2021/12/3 15:55  以解决 利用信号传递的方式
        '''
        station_name = self.UI.comboBox_type_station.currentText()
        pid_type = self.chargeMapper.find_all_pid_by_charge_name(station_name)
        #需要将pid_type转成str
        for i in range(0, len(pid_type)):
            pid_type[i] = str(pid_type[i])
        self.UI.comboBox_type_pile.addItems(pid_type)
        '''

    # 绘制全部
    @pyqtSlot()
    def on_btn_plot_all_clicked(self):
        self.on_btn_plot_line_clicked()
        self.on_btn_plot_pie_clicked()

    # 绘制折线图
    @pyqtSlot()
    def on_btn_plot_line_clicked(self):
        plot_type = self.get_plot_type(0)
        # todo: 需要根据充电站还有充电桩确定，所以先得到充电站sid，再次得到充电桩cid，然后就是画出该充电桩的数据画图了
        sid, pid, begin_time, end_time = self.get_plot_sid_and_pid_and_period()
        x = None
        values = None
        # todo:添加一个字典直接根据type获取SQL语句
        map = {'使用频率': 'use_freq', '风险等级': 'risk_level', '计量误差-时间': 'Measurement_error'}
        table_line_attr = map[plot_type]

        if table_line_attr == 'use_freq':
            x, values = self.chargeMapper.find_plot_attr_by_sid_and_pid_and_period(table_line_attr=table_line_attr,
                                                                                   sid=sid, pid=pid,
                                                                                   begin_time=begin_time,
                                                                                   end_time=end_time)
        elif table_line_attr == 'Measurement_error':
            x, values = self.chargeMapper.find_error_by_sid_and_pid_and_period(table_line_attr=table_line_attr, sid=sid,
                                                                               pid=pid)
        if x:
            self.plot_line(x, values, plot_type)

    # 绘制饼状图
    @pyqtSlot()
    def on_btn_plot_pie_clicked(self):
        plot_type = self.get_plot_type(1)
        sid, pid, begin_time, end_time = self.get_plot_sid_and_pid_and_period()
        x = None
        values = None
        map = {'使用频率': 'use_freq', '风险等级': 'risk_level', '计量误差-时间': 'Measurement_error'}
        table_line_attr = map[plot_type]
        # todo:添加一个字典直接根据type获取SQL语句
        if table_line_attr == 'use_freq':
            x, values = self.chargeMapper.find_plot_attr_by_sid_and_pid_and_period(table_line_attr=table_line_attr,
                                                                                   sid=sid, pid=pid,
                                                                                   begin_time=begin_time,
                                                                                   end_time=end_time)
        elif table_line_attr == 'Measurement_error':
            x, values = self.chargeMapper.find_error_by_sid_and_pid_and_period(table_line_attr=table_line_attr, sid=sid,
                                                                               pid=pid)
        if x:
            self.plot_pie(x, values, plot_type)

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
    def get_plot_type(self, index):
        if index == 0:
            return self.UI.comboBox_type_line.currentText()
        elif index == 1:
            return self.UI.comboBox_type_pie.currentText()

    # 获取数据可视化的对象：充电站与充电桩 返回sid 和 pid
    def get_plot_sid_and_pid_and_period(self):
        station_name = self.UI.comboBox_type_station.currentText()
        sid = self.chargeMapper.find_sid_by_charge_name(station_name)
        pid = int(self.UI.comboBox_type_pile.currentText())
        period = self.UI.comboBox_type_times.currentText()
        begin_time = period.split('~')[0]
        end_time = period.split('~')[1]
        return sid, pid, begin_time, end_time

    # 获取数据
    def get_data(self, sql, arg=None):
        connection, cursor = get_db_connection()

        data = execute_inquiry(sql, arg, connection=connection, cursor=cursor)

        if data == -1:
            show_information_message("查询结果为空")
            return

        return data

    # 获取查询结果
    '''
    def get_inquire(self, sql: str, connection, cursor):
        res_row = 0

        try:
            res_row = cursor.execute(sql)

        except Exception as e:
            self.logger.warning("执行语句失败，失败原因:" + str(e))

        data = cursor.fetchall()
        close_db(connection, cursor)

        return data if res_row != 0 else -1
    '''

    # 获取画图参数 x代表横轴， y代表纵轴
    def get_plot_param(self, x: list, values: list, index: int):
        # 折线图
        if index == 0:
            return x, values
        # 饼状图
        elif index == 1:
            '''
            values = list([])  # 纵轴
            labels = list([])  # lables
            for i in range(0, len(data)):
                values.append(data[i][0])
                labels.append(str(data[i][1]) + "-" + str(data[i][2]))
            '''
            return x, values

    # 绘制饼状图
    def plot_pie(self, x: list, values: list, type: str, grid=False):
        labels, values = self.get_plot_param(x, values, 1)
        self.fig_pie.axes.pie(values,
                              labels=labels,
                              autopct='%1.1f%%',
                              shadow=True,
                              startangle=150)

        self.fig_pie.axes.set_title(type + "饼状图")
        if grid:
            self.fig_pie.axes.grid(True)
        self.fig_pie.axes.legend()
        self.fig_pie.draw()

    # 绘制折线图
    def plot_line(self, x: list, values: list, type: str, grid=True):
        x, values = self.get_plot_param(x, values, 0)

        self.fig_line.axes.plot(x,
                                values,
                                '-',
                                color='r',
                                marker='h',
                                label=type + "折线图")

        self.fig_line.axes.set_title(type + "折线图")
        self.fig_line.axes.set_xticks(x, minor=True)
        # self.fig_line.axes.set_gcf().autofmt_xdate() # 自动旋转日期标记
        if grid:
            self.fig_line.axes.grid(True, linestyle='-.')

        self.fig_line.axes.legend(loc='best', ncol=1)
        self.fig_line.draw()

    # 清屏all
    @pyqtSlot()
    def on_btn_clear_all_clicked(self):
        self.fig_line.axes.cla()
        self.fig_pie.axes.cla()
        self.fig_line.draw()
        self.fig_pie.draw()

    # 清屏left
    @pyqtSlot()
    def on_btn_clear_right_clicked(self):
        self.fig_line.axes.cla()
        self.fig_line.draw()

    # 清屏right
    @pyqtSlot()
    def on_btn_clear_left_clicked(self):
        self.fig_pie.axes.cla()
        self.fig_pie.draw()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = PlotWindow()
    win.show()
    sys.exit(app.exec())