# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(1135, 867)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlotWindow.sizePolicy().hasHeightForWidth())
        PlotWindow.setSizePolicy(sizePolicy)
        PlotWindow.setMinimumSize(QtCore.QSize(548, 309))
        PlotWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 120))
        self.label.setPixmap(QtGui.QPixmap("UI/image/edge(params).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(325, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 17pt \"Adobe 黑体 Std R\";\n"
"\n"
"color:#B4CDCD;")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.btn_factory = QtWidgets.QPushButton(self.frame)
        self.btn_factory.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_factory.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_factory.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;")
        self.btn_factory.setObjectName("btn_factory")
        self.verticalLayout.addWidget(self.btn_factory)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_frequency = QtWidgets.QPushButton(self.frame)
        self.btn_frequency.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_frequency.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;")
        self.btn_frequency.setObjectName("btn_frequency")
        self.verticalLayout.addWidget(self.btn_frequency)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_tem = QtWidgets.QPushButton(self.frame)
        self.btn_tem.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;")
        self.btn_tem.setObjectName("btn_tem")
        self.verticalLayout.addWidget(self.btn_tem)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_temp = QtWidgets.QPushButton(self.frame)
        self.btn_temp.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;")
        self.btn_temp.setObjectName("btn_temp")
        self.verticalLayout.addWidget(self.btn_temp)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.btn_time = QtWidgets.QPushButton(self.frame)
        self.btn_time.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;")
        self.btn_time.setObjectName("btn_time")
        self.verticalLayout.addWidget(self.btn_time)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem5)
        self.btn_other = QtWidgets.QPushButton(self.frame)
        self.btn_other.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;")
        self.btn_other.setObjectName("btn_other")
        self.verticalLayout.addWidget(self.btn_other)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_load = QtWidgets.QPushButton(self.frame)
        self.btn_load.setObjectName("btn_load")
        self.verticalLayout.addWidget(self.btn_load)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: 17pt \"Adobe 黑体 Std R\";\n"
"\n"
"color:#B4CDCD;")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setLineWidth(3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.frame)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tableView = QtWidgets.QTableView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 220))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 280))
        self.tableView.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        PlotWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(PlotWindow)
        self.statusBar.setObjectName("statusBar")
        PlotWindow.setStatusBar(self.statusBar)

        self.retranslateUi(PlotWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "MainWindow"))
        self.label_2.setText(_translate("PlotWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#145b7d;\">-------------参量待选状态---------------</span></p></body></html>"))
        self.btn_factory.setText(_translate("PlotWindow", "生产厂家"))
        self.btn_frequency.setText(_translate("PlotWindow", "使用频率"))
        self.btn_tem.setText(_translate("PlotWindow", "环境温度"))
        self.btn_temp.setText(_translate("PlotWindow", "运营商"))
        self.btn_time.setText(_translate("PlotWindow", "安装时长"))
        self.btn_other.setText(_translate("PlotWindow", "其他因素"))
        self.btn_load.setText(_translate("PlotWindow", "下载数据"))
        self.label_3.setText(_translate("PlotWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#145b7d;\">----------------------------------------------</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PlotWindow", "Tab 1"))
import main_rc
import qss_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotWindow = QtWidgets.QMainWindow()
    ui = Ui_PlotWindow()
    ui.setupUi(PlotWindow)
    PlotWindow.show()
    sys.exit(app.exec_())

