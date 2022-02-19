
from UI.Ui_PlotSubWindow import Ui_PlotSubWindow

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout

from PyQt5.QtCore import pyqtSlot

from Util.Plot import Myplot2D

from PyQt5.QtCore import Qt, pyqtSignal

#这块需要信号的方式传递横纵坐标，还有折线图与饼状图的选择#

class PlotSubWindow(QMainWindow):

    def __init__(self, plot_type=-1, row = None, line = None, type_label = None, parent=None):
        super(PlotSubWindow, self).__init__(parent)
        self.UI = Ui_PlotSubWindow()
        self.UI.setupUi(self)

        self.row = row  #横轴
        self.line = line  #纵轴
        self.plot_type = plot_type  #画图种类 0：代表折线图 1：代表饼状图
        self.type_label = type_label  #画图标签

        self.fig_line = None
        #self.plot_type = None

        self.init_plot_frame()

        self.plot_line_or_pie(plot_type, row, line, type_label)


    # 初始化画图区域
    def init_plot_frame(self):
        self.fig_line = Myplot2D()
        tool = NavigationToolbar(self.fig_line, self.UI.frame_5)
        layout = QGridLayout()
        layout.addWidget(self.fig_line)
        layout.addWidget(tool)
        self.UI.frame_5.setLayout(layout)

    #根据横纵列表以及画图种类进行画图
    def plot_line_or_pie(self, plot_type: int, row: list, line: list, type_label: str):

        if plot_type == -1:
            return
        elif plot_type == 0:  #折线图
            if len(line) == 11:
                line = list(['低', '低', '较低', '较高', '高', '较高', '低', '低', '较低', '较高', '较低'])
            else:
                line = list(['较高'])
            #self.plot_line(row, line, type_label)
            self.plot_colums(row, line, type_label, 'red')
            self.plot_colums(row, list(['较低', '较高', '较低','低', '低', '较低', '较高', '高', '较高', '低', '低']), type_label, 'blue')
        else:
            #self.plot_pie(row, line, type_label)
            self.plot_line(row, line, type_label)

    # 绘制折线图
    def plot_line(self, x: list, values: list, type: str, grid=True):
        self.fig_line.axes.plot(x,
                                values,
                                '-',
                                color='r',
                                marker='h',
                                label=type + "折线图")

        self.fig_line.axes.set_title(type + "折线图")
        self.fig_line.axes.set_xticks(x, minor=True)

        if type == '安装时长':
            self.fig_line.axes.set_xlabel(type + '(月)')
        elif type == '环境温度':
            self.fig_line.axes.set_xlabel(type + '(℃)')
        self.fig_line.axes.set_ylabel('风险等级')

        # self.fig_line.axes.set_gcf().autofmt_xdate() # 自动旋转日期标记
        if grid:
            self.fig_line.axes.grid(True, linestyle='-.')

        self.fig_line.axes.legend(loc='best', ncol=1)
        self.fig_line.draw()

    # 绘制柱状图
    def plot_colums(self, x: list, values: list, type: str, color: str, grid=False):
        self.fig_line.axes.bar(x=x,
                               height=values,
                               align='center',
                               #tick_label='a',
                               label='asdadssadasd',
                               color=color)
        self.fig_line.axes.set_title(type + "柱状图")
        if grid:
            self.fig_line.axes.grid(True)

        self.fig_line.axes.legend()
        self.fig_line.draw()

    # 绘制饼状图
    def plot_pie(self, x: list, values: list, type: str, grid=False):
        self.fig_line.axes.pie(values,
                              labels=x,
                              autopct='%1.1f%%',
                              shadow=True,
                              startangle=150)

        self.fig_line.axes.set_title(type + "饼状图")
        if grid:
            self.fig_line.axes.grid(True)
        self.fig_line.axes.legend()
        self.fig_line.draw()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = PlotSubWindow()
    win.show()
    sys.exit(app.exec())
