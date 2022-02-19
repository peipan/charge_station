# 导入程序运行必须模块
import sys
from time import sleep

# PyQt5使用的基本控件都在PyQt5.QtWights模块中
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QBasicTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

# 导入designer生成的bar_win模块
from UI.bar_win import Ui_form
# 导入designer生成的mainbar模块
from UI.mainbar import Ui_mainWindow


class ProgressBar(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setStyleSheet("#Form{background-color:'#4682B4'}"
                           "#MainWindow{background-color:'#4682B4';color:white;font-weight:600;}"
                           )  # 设置启动窗背景色和进度信息的字体样式等
        self.timer = QBasicTimer()  # 定时器对象
        self.step = 0  # 进度值
        # self.main_win = BarWin()  # 进度结束后显示完成界面
        # self.main_win.show()
        self.process_run()

    def process_run(self):  # 启动进度线程
        self.call = LoadThread()  # 线程对象
        self.call.part_signal.connect(self.process_set_part)
        #self.call.data_signal.connect(self.show_main_win)
        self.call.start()  # 调用线程


    def process_set_part(self, num):
        self.step = num  # 进度从num开始
        self.progressBar.setValue(self.step)
        if num == 0:
            self.timer.start(100, self)  # 启用 QBasicTimer(),每20毫秒调用一次回调函数
            self.label.setText("数据加载中...")
        """if num == 1:
            self.timer.stop()  # 重启，调整进度条增值速度
            self.timer.start(5, self)  # 重新启用 QBasicTimer(),每20毫秒调用一次回调函数
            self.textBrowser_2.setText("文件已完成，正在打开主界面")
        """

    def timerEvent(self, *args, **kwargs):  # QBasicTimer时间回调函数
        self.progressBar.setValue(self.step)
        if self.step < 100:
            self.step += 1

    def show_main_win(self, mes):
        self.main_win.set_data(mes)
        self.main_win.show()
        self.close()


class LoadThread(QThread):  # 自定义计算线程类
    part_signal = pyqtSignal(int)  # 进度换届信号
    #data_signal = pyqtSignal(str)  # 数据传递信号

    def __init__(self):
        super().__init__()

    def run(self):
        self.part_signal.emit(0)  # emit是发射信号，与connect相对应，在本程序文件中对应nun的值
        self.fun_part_one()
        # self.part_signal.emit(1)
        sleep(10)  # 模拟加载耗时
        #self.data_signal.emit("文件已打开")

    def fun_part_one(self):
        sleep(3)  # 模拟计算耗时


class BarWin(QWidget, Ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#Form{background-color:'#4682B4'}"
                           "#Form{background-color:'#4682B4';color:white;font-weight:600;}"
                           )  # 设置启动窗背景色和进度信息的字体样式等

    def set_data(self, mes):
        # self.font = QtGui.QFont()
        # self.font.setFamily("Arial")  # 括号里可以设置成自己想要的其他字体
        # self.font.setPointSize(20)  # 括号里的数字大小可以设置成自己想要的字体大小
        self.textBrowser.setText(mes)


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    pbar = ProgressBar()
    # 将窗口控件显示在屏幕上
    pbar.show()
    # 程序运行，sys.exit方法确保程序完整推出
    sys.exit(app.exec_())
