
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from PyQt5.QtCore import (Qt, pyqtSlot)
from UI.Ui_webEngineView import Ui_Map
from PyQt5 import QtCore, QtGui, QtWidgets

class MapDisplay(QWidget):
    def __init__(self, parent=None):
        super(MapDisplay, self).__init__(parent)
        #self.data
        self.__UI = Ui_Map()
        self.__UI.setupUi(self)
        #self.__UI.widget.setHtml(data.getvalue().decode()) #这个位置也没有问题，地图都能显示 代表没有出错！！！
        #self.__UI.widget.setHtml(data.getvalue().decode())   #为什么这个位置都能有错？？？

        # 设置自动填充背景
        self.setAutoFillBackground(True)

    def trans_data(self, data):
        self.__UI.widget.setHtml(data.getvalue().decode())

if __name__ == "__main__":
    import sys
    from main import visual_all
    app = QtWidgets.QApplication(sys.argv)
    risk_level = [10, 30, 50, 70, 90]
    data = visual_all(1141.111111, 1221.222222, risk_level)
    map = MapDisplay(data=data)
    map.exec()
    sys.exit(app.exec_())

