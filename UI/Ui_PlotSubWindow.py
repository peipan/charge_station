# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotSubWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotSubWindow(object):
    def setupUi(self, PlotSubWindow):
        PlotSubWindow.setObjectName("PlotSubWindow")
        PlotSubWindow.resize(1035, 704)
        self.centralwidget = QtWidgets.QWidget(PlotSubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(3)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout.addWidget(self.frame_5)
        PlotSubWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotSubWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotSubWindow)

    def retranslateUi(self, PlotSubWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotSubWindow.setWindowTitle(_translate("PlotSubWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotSubWindow = QtWidgets.QMainWindow()
    ui = Ui_PlotSubWindow()
    ui.setupUi(PlotSubWindow)
    PlotSubWindow.show()
    sys.exit(app.exec_())

