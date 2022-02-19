# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebEngineView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Map(object):
    def setupUi(self, Map):
        Map.setObjectName("Map")
        Map.resize(663, 425)
        self.verticalLayout = QtWidgets.QVBoxLayout(Map)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWebEngineWidgets.QWebEngineView(Map)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Map)
        QtCore.QMetaObject.connectSlotsByName(Map)

    def retranslateUi(self, Map):
        _translate = QtCore.QCoreApplication.translate
        Map.setWindowTitle(_translate("Map", "Form"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Map = QtWidgets.QWidget()
    ui = Ui_Map()
    ui.setupUi(Map)
    Map.show()
    sys.exit(app.exec_())

