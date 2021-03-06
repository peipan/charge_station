
import numpy as np
from PyQt5.QtCore import pyqtSlot, Qt, QItemSelectionModel, QModelIndex

from Common import show_information_message, show_error_message, init_tableview, get_row_model


from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView, QGridLayout

from PyQt5.QtGui import QPainter, QPaintEvent, QPixmap, QStandardItem, QStandardItemModel

from ParamsSetWindow import ParamsSetWindow
from PlotWindow import PlotWindow
from SigninWindow import SigninWindow
from UI.Ui_MainWindow import Ui_MainWindow
from UserManageWindow import ManageWindow

from MapDisplay import MapDisplay

from ImportDateFromExcel import Thread_import_data_from_excel, ShowInfo
from ImportDatatoExcel import ImportDatatoExcel

from Util.Grade import Grade

from call_mainbar import ProgressBar
from graphyWindow import visual_all
from loginWindow import LoginWindow, User
from mapper.ChargeMapper import ChargeMapper
from mapper.ChargeMapper_test import ChargeMapper_test
from decimal import Decimal

from Util.Plot import Myplot2D

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)

        self.user = None

        self.setCentralWidget(self.UI.tabWidget)  # 将tabwidget设为中心控件
        self.UI.tabWidget.setVisible(True)  # 线隐藏tabwidget控件
        #self.UI.tabWidget.clear()  # 清除所有的页
        self.UI.tabWidget.setTabsClosable(True)  # Page有关闭按钮
        self.UI.tabWidget.setDocumentMode(True)  # 设置文档模式

        self.setWindowState(Qt.WindowMaximized)  # 窗口最大化显示
        self.setAutoFillBackground(False)  # 自动绘制背景
        self.setMinimumSize(1680, 1000)

        self.backgroundPix = QPixmap("Icon/00.png")
        self.pb = None #进度条窗口

        self.head = list(['充电站', '总数', '交流桩', '占比', '直流桩', '占比'])
        self.model = get_row_model(6, header=self.head)
        ###########################################################

        # add 利用信号的方式 （tableView的设置）
        # self.sense_station_change.connect(self.getValue)

        self.mapDisplay = MapDisplay(self)  # 为什么放在这，这就是解决点击按钮  弹框一下就关了的bug......... https://blog.csdn.net/veloi/article/details/115027549这里面的方法二
        self.mapDisplay.close()

        self.chargeMapper = ChargeMapper()  # 注入操作数据库类
        self.chargeMapper_test = ChargeMapper_test()  # 注入操作数据库类
        ##########################################################

        self.importdatatoexcel = ImportDatatoExcel()

        ##################################hyd  加tableView功能  huang######################
        self.init_model = None
        init_tableview(self.UI.tableView, hor_size=50, ver_size=50)
        self.get_initial_model(shuaxinchaxun=0)
        data_model = self.init_model
        selection_model = QItemSelectionModel(data_model)

        self.UI.tableView.setModel(data_model)
        self.UI.tableView.setSelectionModel(selection_model)
        # 设置表格充满这个布局QHeaderView
        self.UI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面


        self.UI.tableView.horizontalHeader().setStyleSheet("QHeaderView::section{border-color: #142c58};")
        self.UI.tableView.verticalHeader().setStyleSheet("QHeaderView::section{border-color: #142c58};")

        #self.UI.tableView.horizontalHeader().setStyleSheet("QHeaderView::section{border-color: #142c58};")
        #self.UI.tableView.verticalHeader().setStyleSheet("QHeaderView::section{border-color: #142c58};")


        self.UI.tableView.selectionModel().currentRowChanged.connect(self.do_cur_row_change)
        ###########################hyd 设置主页面的饼状图显示##########################################
        self.fig_line = None
        self.fig_pie = None
        self.plot_type = None
        self.init_plot_frame()
        # x = ['a', 'b', 'c']
        # values = [20, 30, 50]
        x, values = self.get_plot_pie_row_and_line()
        self.plot_pie(x, values, '北京市各区域充电桩数据及比例显示')
        #############################################################
        # 启用登录窗口
        self.on_act_login_triggered()

    # 单击【登录】按钮
    @pyqtSlot()
    def on_act_login_triggered(self):
        login_window = LoginWindow()
        self.change_enabled([1, 2, 3, 4, 5, 6],
                            True)  # 发现的xiao bug 从页面中点击登录后，这块还得判断用户管理权限....... 也就是5不能乱开  待解决！！！2021/12/04  完美解决 如下，调整了顺序就可以 好好理解下信号传递 2021/12/06
        self.change_enabled([0], False)
        login_window.userSignal.connect(self.receive_user) #这个就是信号传递的函数，连接了自动会去执行receive_user()函数
        res_code = login_window.exec()  # 以模态的方式打开登录窗口
        if res_code == 0:
            self.change_enabled([1, 2, 3, 4, 5],
                            False)
            self.change_enabled([0], True)
        
    # 单击【登出】按钮
    @pyqtSlot()
    def on_act_logout_triggered(self):
        self.user = None
        self.change_enabled([0], on=True)
        self.change_enabled([1, 2, 3, 5], on=False)
        self.UI.tabWidget.setVisible(False) #关闭打开的子页面

    # 点击【导入数据】按钮
    #可能存在一个隐患 就是一次数据插入错误（不按标准格式），会导致后面的算法计算导致出错，如何设置一次插入失败全部回滚的操作？？？待解决 ：https://blog.csdn.net/weixin_29649815/article/details/114394636
    #已经解决 回滚问题 2021/12/26， 但是如果数据有问题  是否还得检查数据类型 以及数据范围的问题 判断是否回滚和接收？？？
    #解决导入数据重复问题 2021/12/26
    #解决数据导入与进度条问题，采用多线程的编写方式，以完美解决！！！2021/12/30
    @pyqtSlot()
    def on_act_import_data_triggered(self):
        file_path, *_ = QFileDialog.getOpenFileName(self, "选取文件", "", "excel Files (*.xlsx)")
        # 无意发现一个bug：点击导入数据的时候，直接×掉 会导致暂停程序,所以程序加一个空字符判断  已解决！
        if file_path == '':
            return
        data_df = self.read_excel(file_path)

        thread = Thread_import_data_from_excel(data_df)
        thread.show_info_signal.connect(self.receive_showInfo)
        thread.start() #开始线程
        # 调用进度条窗口
        self.pb = ProgressBar()
        self.pb.show()

        thread.exec() #保护子线程，否则主线程调用函数结束的时候子线程也被迫退出 一定得添加 不然就会报错，调试都调不出来的错误


    # 单击【数据可视化】按钮
    @pyqtSlot()
    def on_act_show_triggered(self):
        window = PlotWindow(self)
        window.setAttribute(Qt.WA_DeleteOnClose)
        curindex = self.UI.tabWidget.addTab(window, "可视化窗口")
        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)


    #  单击【参数设置】按钮
    @pyqtSlot()
    def on_actiongraph_triggered(self):
        window = ParamsSetWindow()
        window.setAttribute(Qt.WA_DeleteOnClose)
        #window.setWindowFlag(Qt.Window, True)  # 指示该窗口是一个独立的窗口
        curindex = self.UI.tabWidget.addTab(window, "参数设置")
        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)


    # 单击【用户管理】按钮
    @pyqtSlot()
    def on_act_manager_triggered(self):
        window = ManageWindow(self)
        window.setAttribute(Qt.WA_DeleteOnClose)
        curindex = self.UI.tabWidget.addTab(window, "用户管理")
        self.UI.tabWidget.setCurrentIndex(curindex)
        self.UI.tabWidget.setVisible(True)

    # 单击【注册】按钮
    @pyqtSlot()
    def on_act_signin_triggered(self):
        window = SigninWindow(self)  # 创建用户窗口
        window.setAttribute(Qt.WA_DeleteOnClose)  # 设置关闭删除实例
        window.setWindowFlag(Qt.Window, True)  # 指示该窗口是一个独立的窗口
        window.show()  # 非模态显示

    # 单击【退出】按钮
    @pyqtSlot()
    def on_act_quit_triggered(self):
        self.close()

    # 接收用户类槽函数
    @pyqtSlot(User)
    def receive_user(self, user: User):
        self.user = user
        self.check_grade()

    # 接受导入数据的出现的问题详情
    @pyqtSlot(ShowInfo)
    def receive_showInfo(self, showInfo: ShowInfo):
        if showInfo.info == -1:
            message = "插入的excel表重复！！！"
            show_information_message(self, message)
        elif showInfo.info == 0:
            message = "全部插入成功!!!"
            show_information_message(self, message)
            x, values = self.get_plot_pie_row_and_line()
            self.plot_pie(x, values, '北京市各区域充电桩数据及比例显示')
            self.get_initial_model(shuaxinchaxun=1)
            data_model = self.init_model
            selection_model = QItemSelectionModel(data_model)
            self.UI.tableView.setModel(data_model)
            self.UI.tableView.setSelectionModel(selection_model)
        elif showInfo.info == -2:
            message = "数据无效（无法计算出唯一解）！！！"
            show_information_message(self, message)
        else:
            message = "大约 " + str(showInfo.info) + "行数据插入失败！请检查，然后重新导入"
            show_information_message(self, message)
        self.pb.close() #数据不管导入成功与否，进度条页面都得关闭

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

    # 审核当前用户权限
    def check_grade(self):
        if self.user is None:
            grade = 0
        else:
            grade = self.user.grade

        if grade == Grade.Administrator.value: #管理员
            pass
        elif grade == Grade.Normal_user.value: #普通用户
            self.change_enabled([5], on=False)

    # 改变控件使能
    def change_enabled(self, change_list, on):
        if not isinstance(change_list, list):
            # 如果不是int参数进行报错
            if not isinstance(change_list, int):
                show_error_message(self, "错误的参数:" + str(change_list))
                return

            change_list = [].append(change_list)

        for i in change_list:
            if i == 0:
                self.UI.act_login.setEnabled(on)
            elif i == 1:
                self.UI.act_logout.setEnabled(on)
            elif i == 2:
                self.UI.act_import_data.setEnabled(on)
            elif i == 3:
                self.UI.act_show.setEnabled(on)
            elif i == 4:
                self.UI.act_signin.setEnabled(on)
            elif i == 5:
                self.UI.act_manager.setEnabled(on)
            elif i == 6:
                self.UI.act_quit.setEnabled(on)

    # 读取excel数据
    def read_excel(self, file_path):
        import pandas as pd
        df = pd.read_excel(file_path, skiprows=1)
        return df

    # 重写【绘制事件】
    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        pointx = 0  # 绘制的左上角
        pointy = self.UI.menubar.height() + self.UI.toolBar.height()  # 绘制的右上角
        # 绘制的图片宽度
        width = self.width()
        # 绘制的图片高度
        height = self.height() - self.statusBar().height() - self.UI.menubar.height() - self.UI.toolBar.height()
        painter.drawPixmap(pointx, pointy, width, height, self.backgroundPix)  # 绘制背景图片
        super(MainWindow, self).paintEvent(event)  # 向上传递QPaintEvent

    # 下载导出高风险等级充电桩的数据文件 .txt (hyd)
    @pyqtSlot()
    def on_act_output_triggered(self):


        file_path = QFileDialog.getSaveFileName(self, "save file", "E:/", "excel Files (*.xls)")  # 这里的file_name是tuple型
        #self.impo
        # rtdatatoexcel.export_to_excel('table_charge_station', file_path[0])
        # lists = [[1, 2, 3, 4], [45, 23, 456, 23, 54, 23], [12, 23, 23, 345, 23, 12]]
        if file_path[0] == '':
             return
        else:
            # self.Save_list(lists, file_path[0])
            # 取tuple第一个元素即为地址
            self.importdatatoexcel.export_to_excel('table_charge_pile', file_path[0])

    # 下载导出模板数据文件 .txt (hyd)
    @pyqtSlot()
    def on_actionact_formwork_triggered(self):
        file_path = QFileDialog.getSaveFileName(self, "save file", "E:/",
                                                "excel Files (*.xls)")  # 这里的file_name是tuple型
        if file_path[0] == '':
            return
        else:
        # self.Save_list(lists, file_path[0])
            # 取tuple第一个元素即为地址
            self.importdatatoexcel.export_to_excel_formwork('table_formwork', file_path[0])

    # 地图风险等级展示按钮  author：hyd
    @pyqtSlot()
    def on_act_map_triggered(self):
        '''
        charge_name = self.UI.comboBox_type_station.currentText()
        sid = self.chargeMapper.find_sid_by_charge_name(charge_name)
        # 先获得经纬度数据,是一个数组类型，可能需要将数据强转float
        longitude_and_latitude = self.chargeMapper.find_longitude_and_latitude_by_charge_name(sid)
        #获取该充电站下的pid以及对应的风险等级数据，返回一个字典类型
        pid_and_risk_level_dict = self.chargeMapper.find_pid_risk_level_by_sid(sid)
        '''
        # todo:外弹框 显示地图就ok，我需要把经纬度数据填

        location = self.chargeMapper_test.find_longitude_latitude_risk()
        if location is None:        # 修复没有数据的时候点击地图展示报错问题
            message = "请先插入数据！"
            show_information_message(self, message)
            return

        location1 = list([])  # 现在location是列表 需要把i i+1单独存成元组
        location2 = list([])

        for i in range(0, len(location)):
            location1.append(location[i][0])
            location2.append(location[i][1])
            # level.append(location[i][2])
        for k in range(0, len(location1)):
            location1[k] = float(Decimal(location1[k]))
            location2[k] = float(Decimal(location2[k]))
        local_real = [list(l) for l in zip(location2, location1)]

        a = 0
        list3 = np.array(list(set([tuple(t) for t in local_real])),
                         dtype='float').tolist()  # The truth value of an array
        # with more than one element is ambiguous. Use a.any() or a.all() 但显示在folium.Icon这块

        level = [[] for x in range(len(list3))]
        for k in range(0, len(list3)):
            if a == len(location):
                break
            for i in range(0, len(location)):
                if location2[i] == list3[k][0]:
                    # list1.append(location[i][2])  # 要把风险等级存入二维列表
                    level[k].append(location[i][2])
                    a = a + 1
                else:
                    j = k + 1
                    level[j].append(location[i][2])
                    a = a + 1

        addr = local_real[len(local_real)-1]
        data = visual_all(list3, addr, *level)  # list输入位置与风险等级

        # mapDisplay = MapDisplay(data)
        self.mapDisplay.trans_data(data)
        # self.mapDisplay.setAttribute(Qt.WA_DeleteOnClose)  # 设置关闭删除实例  应该是这句话一直出现了bug
        self.mapDisplay.setWindowFlag(Qt.Window, True)  # 指示该窗口是一个独立的窗口
        # mapDisplay.exec()  #Qwidths没有模态窗口选项
        self.mapDisplay.show()

    @pyqtSlot(QModelIndex, QModelIndex)
    def do_cur_row_change(self, cur: QModelIndex, pre: QModelIndex):
        self.cur_row = cur.row()

    # 获取最初的数据模型  huang
    def get_initial_model(self, shuaxinchaxun: int):
        new_id = self.chargeMapper.find_newest_sid()
        ret_data = self.chargeMapper.find_first_page_table(new_id, shuaxinchaxun=shuaxinchaxun)
        if ret_data is None:
            return list([])
        data = list([])
        for i in range(0, len(ret_data)):
            temp = list([])
            sum = ret_data[i][1] + ret_data[i][2]
            temp.append(ret_data[i][0])
            temp.append(sum)  # 充电站总数量
            temp.append(ret_data[i][1])  # 交流数量
            temp.append('{:.0f}%'.format(ret_data[i][1] / sum * 100))  # 交流数量占比
            temp.append(ret_data[i][2])  # 直流数量
            temp.append('{:.0f}%'.format(ret_data[i][2] / sum * 100))  # 直流数量占比
            data.append(temp)
        self.init_model = self.add_data(self.model, data)

    # 向模型添加数据
    def add_data(self, model: QStandardItemModel, data) -> QStandardItemModel:
        for i in data:
            row = []
            for j in range(len(i)):
                item = QStandardItem(str(i[j]))
                row.append(item)
            model.appendRow(row)
        return model

    # 初始化画图区域 没直接用plotsubwindow的是因为这里是frame 那个是frame_5 改了会影响数据可视化页面 hyd
    def init_plot_frame(self):
        self.fig_line = Myplot2D(plt0=10)
        #tool = NavigationToolbar(self.fig_line, self.UI.frame)
        layout = QGridLayout()
        layout.addWidget(self.fig_line)
        #layout.addWidget(tool)
        self.UI.frame.setLayout(layout)

    # 一个autopct指向的函数，lambda可以指向
    def func(self, pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%\n({:d} 台)".format(pct, absolute)

    # 绘制饼状图
    def plot_pie(self, x: list, values: list, type: str, grid=False):
        if x is None:  # 没有数据的时候的判断
            return
        self.fig_line.axes.clear()

        self.fig_line.axes.pie(values,
                                labels=x,
                                autopct=lambda pct: self.func(pct, values),
                                shadow=True,
                                #colors=['y', 'g', 'b', 'r', 'w'],
                                startangle=100
                               )
        #self.fig_line.axes.legend(x, title="", loc='center left', fontsize=10, bbox_to_anchor=(1, 0, 0.5, 1))  # 有图例总是无法覆盖 暂时先去掉 加上新数据后再看
        self.fig_line.axes.legend()
        self.fig_line.axes.set_title(type + "饼状图", fontsize=20)
        self.fig_line.axes.axis('equal')
        self.fig_line.draw()

    def get_plot_pie_row_and_line(self):
        x, values = self.chargeMapper_test.find_plot_attr_by_sid_and_main_data()
        return x, values


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
