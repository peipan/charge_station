# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SigninWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SigninDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(707, 565)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(685, 129))
        self.label_8.setPixmap(QtGui.QPixmap("UI/image/edge(sign).png"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QSplitter(Dialog)
        self.name.setOrientation(QtCore.Qt.Horizontal)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(self.name)
        self.label.setMinimumSize(QtCore.QSize(47, 19))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.name_lineEdit = QtWidgets.QLineEdit(self.name)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_lineEdit.setSizePolicy(sizePolicy)
        self.name_lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.name_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.name_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_lineEdit.setStyleSheet("color: #000000")
        self.name_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.name_lineEdit.setClearButtonEnabled(True)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.verticalLayout.addWidget(self.name)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.real_name = QtWidgets.QSplitter(Dialog)
        self.real_name.setOrientation(QtCore.Qt.Horizontal)
        self.real_name.setObjectName("real_name")
        self.label_5 = QtWidgets.QLabel(self.real_name)
        self.label_5.setMinimumSize(QtCore.QSize(47, 19))
        self.label_5.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.real_name_lineEdit = QtWidgets.QLineEdit(self.real_name)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.real_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.real_name_lineEdit.setSizePolicy(sizePolicy)
        self.real_name_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.real_name_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.real_name_lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.real_name_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.real_name_lineEdit.setStyleSheet("color:#000000")
        self.real_name_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.real_name_lineEdit.setClearButtonEnabled(True)
        self.real_name_lineEdit.setObjectName("real_name_lineEdit")
        self.verticalLayout.addWidget(self.real_name)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.password = QtWidgets.QSplitter(Dialog)
        self.password.setOrientation(QtCore.Qt.Horizontal)
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(self.password)
        self.label_2.setMinimumSize(QtCore.QSize(47, 19))
        self.label_2.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.password_lineEdit = QtWidgets.QLineEdit(self.password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.password_lineEdit.setStyleSheet("color:#000000")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_lineEdit.setClearButtonEnabled(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout.addWidget(self.password)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.repeat_password = QtWidgets.QSplitter(Dialog)
        self.repeat_password.setOrientation(QtCore.Qt.Horizontal)
        self.repeat_password.setObjectName("repeat_password")
        self.label_4 = QtWidgets.QLabel(self.repeat_password)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.check_password_lineEdit = QtWidgets.QLineEdit(self.repeat_password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_password_lineEdit.sizePolicy().hasHeightForWidth())
        self.check_password_lineEdit.setSizePolicy(sizePolicy)
        self.check_password_lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.check_password_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.check_password_lineEdit.setStyleSheet("color: #000000\n"
                                                   "")
        self.check_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.check_password_lineEdit.setClearButtonEnabled(True)
        self.check_password_lineEdit.setObjectName("check_password_lineEdit")
        self.verticalLayout.addWidget(self.repeat_password)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.department = QtWidgets.QSplitter(Dialog)
        self.department.setOrientation(QtCore.Qt.Horizontal)
        self.department.setObjectName("department")
        self.label_7 = QtWidgets.QLabel(self.department)
        self.label_7.setMinimumSize(QtCore.QSize(47, 19))
        self.label_7.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_7.setObjectName("label_7")
        self.department_lineEdit = QtWidgets.QLineEdit(self.department)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.department_lineEdit.sizePolicy().hasHeightForWidth())
        self.department_lineEdit.setSizePolicy(sizePolicy)
        self.department_lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.department_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.department_lineEdit.setStyleSheet("color:#000000")
        self.department_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.department_lineEdit.setClearButtonEnabled(True)
        self.department_lineEdit.setObjectName("department_lineEdit")
        self.verticalLayout.addWidget(self.department)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.phone = QtWidgets.QSplitter(Dialog)
        self.phone.setOrientation(QtCore.Qt.Horizontal)
        self.phone.setObjectName("phone")
        self.label_6 = QtWidgets.QLabel(self.phone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(99, 19))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.label_6.setObjectName("label_6")
        self.telephone_lineEdit = QtWidgets.QLineEdit(self.phone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.telephone_lineEdit.sizePolicy().hasHeightForWidth())
        self.telephone_lineEdit.setSizePolicy(sizePolicy)
        self.telephone_lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.telephone_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.telephone_lineEdit.setStyleSheet("color:#000000")
        self.telephone_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.telephone_lineEdit.setClearButtonEnabled(True)
        self.telephone_lineEdit.setObjectName("telephone_lineEdit")
        self.verticalLayout.addWidget(self.phone)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.btn = QtWidgets.QSplitter(Dialog)
        self.btn.setOrientation(QtCore.Qt.Horizontal)
        self.btn.setObjectName("btn")
        self.btn_confirm_2 = QtWidgets.QPushButton(self.btn)
        self.btn_confirm_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-style:none;\n"
            "border:1px solid #3f3f3f; \n"
            "\n"
            "padding:5px;\n"
            "min-height:20px;\n"
            "border-radius:15px;\n"
            "font: 75 12pt \"微软雅黑\";")
        self.btn_confirm_2.setObjectName("btn_confirm_2")
        self.btn_cancel = QtWidgets.QPushButton(self.btn)
        self.btn_cancel.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.541701, y1:1, x2:0.537, y2:0, stop:0.20398 rgba(51, 102, 153, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-style:none;\n"
            "border:1px solid #3f3f3f; \n"
            "\n"
            "padding:5px;\n"
            "min-height:20px;\n"
            "border-radius:15px;\n"
            "font: 75 12pt \"微软雅黑\";")
        self.btn_cancel.setObjectName("btn_cancel")
        self.verticalLayout.addWidget(self.btn)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setMinimumSize(QtCore.QSize(75, 75))
        self.label_9.setMaximumSize(QtCore.QSize(75, 75))
        self.label_9.setPixmap(QtGui.QPixmap("UI/image/main_title.jpg"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "              用户名:"))
        self.name_lineEdit.setPlaceholderText(_translate("Dialog", "用户名"))
        self.label_5.setText(_translate("Dialog", "               姓名:"))
        self.real_name_lineEdit.setPlaceholderText(_translate("Dialog", "姓名"))
        self.label_2.setText(_translate("Dialog", "               密码:"))
        self.password_lineEdit.setPlaceholderText(_translate("Dialog", "用户密码"))
        self.label_4.setText(_translate("Dialog", "             重复密码:"))
        self.check_password_lineEdit.setPlaceholderText(_translate("Dialog", "确认用户密码"))
        self.label_7.setText(_translate("Dialog", "               部门："))
        self.department_lineEdit.setPlaceholderText(_translate("Dialog", "部门"))
        self.label_6.setText(_translate("Dialog", "               电话："))
        self.telephone_lineEdit.setPlaceholderText(_translate("Dialog", "电话"))
        self.btn_confirm_2.setText(_translate("Dialog", "确认"))
        self.btn_cancel.setText(_translate("Dialog", "取消"))
        #self.label_9.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SigninDialog = QtWidgets.QDialog()
    ui = Ui_SigninDialog()
    ui.setupUi(SigninDialog)
    SigninDialog.show()
    sys.exit(app.exec_())

