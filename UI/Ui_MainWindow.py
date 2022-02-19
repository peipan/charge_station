# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(11, 11, 761, 571))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableView = QtWidgets.QTableView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 150))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 254);")
        self.tableView.setObjectName("tableView")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setStyleSheet("background-color:#4682b4;\n"
"color: rgb(255, 255, 255);")
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(40, 36))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar_2.sizePolicy().hasHeightForWidth())
        self.toolBar_2.setSizePolicy(sizePolicy)
        self.toolBar_2.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qss/psblack/checkbox_parcial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBar_2.setWindowIcon(icon)
        self.toolBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar_2.setStyleSheet("background-color:#B4CDCD;\n"
"QToolBar{spacing:160px;}")
        self.toolBar_2.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar_2.setIconSize(QtCore.QSize(25, 90))
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar_2.setFloatable(True)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_2)
        self.act_import_data = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/main_help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_import_data.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.act_import_data.setFont(font)
        self.act_import_data.setObjectName("act_import_data")
        self.act_signin = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/main_about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_signin.setIcon(icon2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.act_signin.setFont(font)
        self.act_signin.setObjectName("act_signin")
        self.act_manager = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/main_person.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_manager.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.act_manager.setFont(font)
        self.act_manager.setObjectName("act_manager")
        self.act_quit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/main_company.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_quit.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.act_quit.setFont(font)
        self.act_quit.setObjectName("act_quit")
        self.act_login = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/main_main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_login.setIcon(icon5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.act_login.setFont(font)
        self.act_login.setObjectName("act_login")
        self.act_logout = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/image/main_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_logout.setIcon(icon6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.act_logout.setFont(font)
        self.act_logout.setObjectName("act_logout")
        self.act_show = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/image/main_data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_show.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.act_show.setFont(font)
        self.act_show.setObjectName("act_show")
        self.actiongraph = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/image/main_config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongraph.setIcon(icon8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actiongraph.setFont(font)
        self.actiongraph.setObjectName("actiongraph")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_login)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_signin)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_logout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_manager)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_quit)
        self.toolBar_2.addAction(self.act_import_data)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.act_show)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actiongraph)
        self.toolBar_2.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableView.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.act_import_data.setText(_translate("MainWindow", "数据导入"))
        self.act_import_data.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">导入数据</span></p></body></html>"))
        self.act_signin.setText(_translate("MainWindow", "用户注册"))
        self.act_signin.setToolTip(_translate("MainWindow", "用户注册"))
        self.act_manager.setText(_translate("MainWindow", "用户管理"))
        self.act_manager.setToolTip(_translate("MainWindow", "用户管理"))
        self.act_quit.setText(_translate("MainWindow", "退出系统"))
        self.act_quit.setToolTip(_translate("MainWindow", "退出系统"))
        self.act_login.setText(_translate("MainWindow", "用户登录"))
        self.act_login.setToolTip(_translate("MainWindow", "用户登录"))
        self.act_logout.setText(_translate("MainWindow", "用户退出"))
        self.act_logout.setToolTip(_translate("MainWindow", "用户退出"))
        self.act_show.setText(_translate("MainWindow", "数据可视化"))
        self.act_show.setToolTip(_translate("MainWindow", "数据可视化"))
        self.actiongraph.setText(_translate("MainWindow", "参数设置"))
        self.actiongraph.setIconText(_translate("MainWindow", "参数设置"))
import main_rc
import qss_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

