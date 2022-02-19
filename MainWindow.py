
from PyQt5.QtCore import pyqtSlot, Qt

from Util.Grade import Grade

from Common import show_information_message, show_error_message, init_tableview, get_row_model

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from PyQt5.QtGui import QPainter, QPaintEvent, QPixmap

from UI.Ui_MainWindow import Ui_MainWindow

from loginWindow import LoginWindow, User

from SigninWindow import SigninWindow

from PlotWindow import PlotWindow

from ParamsSetWindow import ParamsSetWindow

from UserManageWindow import ManageWindow

from mapper.ChargeMapper import ChargeMapper

from ImportDateFromExcel import Thread_import_data_from_excel, ShowInfo

from call_mainbar import ProgressBar

import sys

#Administrator_grade = 1


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)

        self.user = None

        self.setCentralWidget(self.UI.tabWidget)  # 将tabwidget设为中心控件
        self.UI.tabWidget.setVisible(False)  # 线隐藏tabwidget控件
        self.UI.tabWidget.clear()  # 清除所有的页
        self.UI.tabWidget.setTabsClosable(True)  # Page有关闭按钮
        self.UI.tabWidget.setDocumentMode(True)  # 设置文档模式

        self.setWindowState(Qt.WindowMaximized)  # 窗口最大化显示
        self.setAutoFillBackground(False)  # 自动绘制背景
        self.setMinimumSize(1680, 1000)

        self.backgroundPix = QPixmap("Icon/000.png")
        self.pb = None #进度条窗口




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
        else:
            message = str(showInfo.info) + "行数据插入失败！请检查，然后重新导入"
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




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
