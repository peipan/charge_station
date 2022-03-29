# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParametersWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ParametersWindow(object):
    def setupUi(self, ParametersWindow):
        ParametersWindow.setObjectName("ParametersWindow")
        ParametersWindow.resize(2281, 817)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParametersWindow.sizePolicy().hasHeightForWidth())
        ParametersWindow.setSizePolicy(sizePolicy)
        ParametersWindow.setMinimumSize(QtCore.QSize(0, 0))
        ParametersWindow.setMaximumSize(QtCore.QSize(2281, 817))
        self.gridLayout = QtWidgets.QGridLayout(ParametersWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(ParametersWindow)
        self.label_8.setMinimumSize(QtCore.QSize(0, 100))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.splitter_8 = QtWidgets.QSplitter(ParametersWindow)
        self.splitter_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_8)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(100, 0, 100, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout.addWidget(self.label_28)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter)
        self.splitter_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.check_time = QtWidgets.QCheckBox(self.splitter_14)
        self.check_time.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.check_time.setObjectName("check_time")
        self.check_frequency = QtWidgets.QCheckBox(self.splitter_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_frequency.sizePolicy().hasHeightForWidth())
        self.check_frequency.setSizePolicy(sizePolicy)
        self.check_frequency.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.check_frequency.setObjectName("check_frequency")
        self.check_temp = QtWidgets.QCheckBox(self.splitter_14)
        self.check_temp.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.check_temp.setObjectName("check_temp")
        self.check_humi = QtWidgets.QCheckBox(self.splitter_14)
        self.check_humi.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.check_humi.setObjectName("check_humi")
        self.check_protect = QtWidgets.QCheckBox(self.splitter_14)
        self.check_protect.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.check_protect.setObjectName("check_protect")
        self.check_other = QtWidgets.QCheckBox(self.splitter_14)
        self.check_other.setObjectName("check_other")
        self.pushButton = QtWidgets.QPushButton(self.splitter_14)
        self.pushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;\n"
"font: 75 12pt \"微软雅黑\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.splitter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.splitter_16 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName("splitter_16")
        self.splitter_15 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.label_16 = QtWidgets.QLabel(self.splitter_15)
        self.label_16.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_16.setObjectName("label_16")
        self.install_time_weight_lineEdit = QtWidgets.QLineEdit(self.splitter_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.install_time_weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.install_time_weight_lineEdit.setSizePolicy(sizePolicy)
        self.install_time_weight_lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.install_time_weight_lineEdit.setText("")
        self.install_time_weight_lineEdit.setObjectName("install_time_weight_lineEdit")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_15 = QtWidgets.QLabel(self.splitter_7)
        self.label_15.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_15.setObjectName("label_15")
        self.temper_weight_lineEdit = QtWidgets.QLineEdit(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temper_weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.temper_weight_lineEdit.setSizePolicy(sizePolicy)
        self.temper_weight_lineEdit.setText("")
        self.temper_weight_lineEdit.setObjectName("temper_weight_lineEdit")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_18 = QtWidgets.QLabel(self.splitter_6)
        self.label_18.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_18.setObjectName("label_18")
        self.maintain_freq_weight_lineEdit = QtWidgets.QLineEdit(self.splitter_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintain_freq_weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.maintain_freq_weight_lineEdit.setSizePolicy(sizePolicy)
        self.maintain_freq_weight_lineEdit.setText("")
        self.maintain_freq_weight_lineEdit.setObjectName("maintain_freq_weight_lineEdit")
        self.verticalLayout.addWidget(self.splitter_16)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_17 = QtWidgets.QLabel(self.splitter_4)
        self.label_17.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_17.setObjectName("label_17")
        self.use_freq_weight_lineEdit = QtWidgets.QLineEdit(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_freq_weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.use_freq_weight_lineEdit.setSizePolicy(sizePolicy)
        self.use_freq_weight_lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.use_freq_weight_lineEdit.setText("")
        self.use_freq_weight_lineEdit.setObjectName("use_freq_weight_lineEdit")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_19 = QtWidgets.QLabel(self.splitter_3)
        self.label_19.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_19.setObjectName("label_19")
        self.humi_weight_lineEdit = QtWidgets.QLineEdit(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.humi_weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.humi_weight_lineEdit.setSizePolicy(sizePolicy)
        self.humi_weight_lineEdit.setText("")
        self.humi_weight_lineEdit.setObjectName("humi_weight_lineEdit")
        self.label_20 = QtWidgets.QLabel(self.splitter_5)
        self.label_20.setMinimumSize(QtCore.QSize(90, 0))
        self.label_20.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_20.setObjectName("label_20")
        self.other_weight_lineEdit = QtWidgets.QLineEdit(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.other_weight_lineEdit.setSizePolicy(sizePolicy)
        self.other_weight_lineEdit.setText("")
        self.other_weight_lineEdit.setObjectName("other_weight_lineEdit")
        self.verticalLayout.addWidget(self.splitter_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.btn_confirm_weight = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_confirm_weight.setMinimumSize(QtCore.QSize(120, 32))
        self.btn_confirm_weight.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btn_confirm_weight.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;\n"
"font: 75 12pt \"微软雅黑\";")
        self.btn_confirm_weight.setAutoDefault(False)
        self.btn_confirm_weight.setObjectName("btn_confirm_weight")
        self.horizontalLayout_3.addWidget(self.btn_confirm_weight)
        spacerItem7 = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem9)
        self.splitter_10 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.label = QtWidgets.QLabel(self.splitter_9)
        self.label.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_3 = QtWidgets.QLabel(self.splitter_11)
        self.label_3.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.littlelowlineEdit = QtWidgets.QLineEdit(self.splitter_11)
        self.littlelowlineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.littlelowlineEdit.setObjectName("littlelowlineEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.lowlineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lowlineEdit.setMinimumSize(QtCore.QSize(123, 0))
        self.lowlineEdit.setObjectName("lowlineEdit")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.label_4 = QtWidgets.QLabel(self.splitter_12)
        self.label_4.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.littlehighlineEdit = QtWidgets.QLineEdit(self.splitter_12)
        self.littlehighlineEdit.setObjectName("littlehighlineEdit")
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.label_5 = QtWidgets.QLabel(self.splitter_13)
        self.label_5.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.highlineEdit = QtWidgets.QLineEdit(self.splitter_13)
        self.highlineEdit.setMinimumSize(QtCore.QSize(126, 0))
        self.highlineEdit.setObjectName("highlineEdit")
        self.verticalLayout.addWidget(self.splitter_10)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.btn_confirm_range = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_confirm_range.setMinimumSize(QtCore.QSize(120, 32))
        self.btn_confirm_range.setMaximumSize(QtCore.QSize(120, 39))
        self.btn_confirm_range.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style:none;\n"
"border:1px solid #3f3f3f; \n"
"\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:15px;\n"
"font: 75 12pt \"微软雅黑\";")
        self.btn_confirm_range.setObjectName("btn_confirm_range")
        self.horizontalLayout_2.addWidget(self.btn_confirm_range)
        spacerItem12 = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem13)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.gridLayout.addWidget(self.splitter_8, 2, 0, 1, 1)

        self.retranslateUi(ParametersWindow)
        QtCore.QMetaObject.connectSlotsByName(ParametersWindow)

    def retranslateUi(self, ParametersWindow):
        _translate = QtCore.QCoreApplication.translate
        ParametersWindow.setWindowTitle(_translate("ParametersWindow", "MainWindow"))
        self.label_8.setText(_translate("ParametersWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_28.setText(_translate("ParametersWindow", "<html><head/><body><p><span style=\" font-family:\'华文隶书\'; font-size:18pt; font-weight:600; color:#336699;\">参数选择设置________________________________________________________________________________________________________________</span></p></body></html>"))
        self.check_time.setText(_translate("ParametersWindow", "安装时长"))
        self.check_frequency.setText(_translate("ParametersWindow", "使用频率"))
        self.check_temp.setText(_translate("ParametersWindow", "环境温度"))
        self.check_humi.setText(_translate("ParametersWindow", "环境湿度"))
        self.check_protect.setText(_translate("ParametersWindow", "维护频次"))
        self.check_other.setText(_translate("ParametersWindow", "其他因素"))
        self.pushButton.setText(_translate("ParametersWindow", "确定"))
        self.label_23.setText(_translate("ParametersWindow", "<html><head/><body><p><span style=\" font-family:\'华文隶书\'; font-size:18pt; font-weight:600; color:#336699;\">参数权重设置________________________________________________________________________________________________________________</span></p></body></html>"))
        self.label_16.setText(_translate("ParametersWindow", "<html><head/><body><p>安装时长权重</p></body></html>"))
        self.install_time_weight_lineEdit.setPlaceholderText(_translate("ParametersWindow", "0"))
        self.label_15.setText(_translate("ParametersWindow", "环境温度权重"))
        self.temper_weight_lineEdit.setPlaceholderText(_translate("ParametersWindow", "0"))
        self.label_18.setText(_translate("ParametersWindow", "维护频次权重"))
        self.maintain_freq_weight_lineEdit.setPlaceholderText(_translate("ParametersWindow", "0"))
        self.label_17.setText(_translate("ParametersWindow", "使用频率权重"))
        self.use_freq_weight_lineEdit.setPlaceholderText(_translate("ParametersWindow", "0"))
        self.label_19.setText(_translate("ParametersWindow", "环境湿度权重"))
        self.humi_weight_lineEdit.setPlaceholderText(_translate("ParametersWindow", "0"))
        self.label_20.setText(_translate("ParametersWindow", "其他因素权重"))
        self.other_weight_lineEdit.setPlaceholderText(_translate("ParametersWindow", "0"))
        self.btn_confirm_weight.setText(_translate("ParametersWindow", "确定"))
        self.label_24.setText(_translate("ParametersWindow", "<html><head/><body><p><span style=\" font-family:\'华文隶书\'; font-size:18pt; font-weight:600; color:#336699;\">风险范围设置__________________________________________________________________________________________________________________</span></p></body></html>"))
        self.label.setText(_translate("ParametersWindow", "电桩整体性能："))
        self.label_3.setText(_translate("ParametersWindow", "较低"))
        self.littlelowlineEdit.setPlaceholderText(_translate("ParametersWindow", "格式：nn-nn"))
        self.label_2.setText(_translate("ParametersWindow", "低"))
        self.lowlineEdit.setPlaceholderText(_translate("ParametersWindow", "格式：nn-nn"))
        self.label_4.setText(_translate("ParametersWindow", "较高"))
        self.littlehighlineEdit.setPlaceholderText(_translate("ParametersWindow", "格式：nn-nn"))
        self.label_5.setText(_translate("ParametersWindow", "高"))
        self.highlineEdit.setPlaceholderText(_translate("ParametersWindow", "格式：nn-nn"))
        self.btn_confirm_range.setText(_translate("ParametersWindow", "确定"))
        self.label_12.setText(_translate("ParametersWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#336699;\">----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</span></p></body></html>"))
        self.label_13.setText(_translate("ParametersWindow", "<html><head/><body><p><span style=\" color:#336699;\">注：所有权重相加不得超过一！</span></p></body></html>"))
import main_rc
