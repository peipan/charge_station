import numpy as np

from Common import get_plot_type, get_db_connection, close_db, get_logger, show_information_message, execute_inquiry, \
    get_row_model, init_tableview

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QHeaderView

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

import seaborn as sns  #https://seaborn.apachecn.org/#/docs/12   seaborn中文文档

import pandas as pd

from PyQt5.QtCore import pyqtSlot, QItemSelectionModel, QModelIndex

from PyQt5.QtGui import QStandardItem, QStandardItemModel

from UI.Ui_PlotSubWindow import Ui_PlotSubWindow

from Util.Plot import Myplot2D

#https://seaborn.apachecn.org/#/docs/12   seaborn中文文档

#这块需要信号的方式传递横纵坐标，还有折线图与饼状图的选择#



class PlotSubWindow(QMainWindow):

    def __init__(self, plot_type=-1, row = None, line = None, data = None, type_label = None, parent=None):
        super(PlotSubWindow, self).__init__(parent)
        self.UI = Ui_PlotSubWindow()
        self.UI.setupUi(self)

        self.row = row  #横轴
        self.line = line  #纵轴
        self.plot_type = plot_type  #画图种类 1：代表折线图 0：代表柱状图
        self.type_label = type_label  #画图标签

        self.fig_line = None
        #self.plot_type = None

        self.init_plot_frame()
        if plot_type == 0:  # 柱状图
            self.plt_multi_colums(row, line, type_label)
        elif plot_type == 1:
            self.plt_multi_line(row, line, type_label)

        #self.plot_line_or_pie(plot_type, row, line, type_label)

        ##################################加tableView功能######################
        if data is not None:
            self.init_model = None
            init_tableview(self.UI.tableView, hor_size=50, ver_size=50)
            self.get_initial_model(data, type_label)
            data_model = self.init_model
            selection_model = QItemSelectionModel(data_model)

            self.UI.tableView.setModel(data_model)
            self.UI.tableView.setSelectionModel(selection_model)
            # 设置表格充满这个布局QHeaderView
            self.UI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面

        #####################################################################

    # 初始化画图区域

    def init_plot_frame(self):
        self.fig_line = Myplot2D()
        #tool = NavigationToolbar(self.fig_line, self.UI.frame_5)
        layout = QGridLayout()
        layout.addWidget(self.fig_line)
        #layout.addWidget(tool)
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

    # 绘制折线图，三根线 有最高、平均、最低，折线图 比较简单，容易理解
    def plot_line(self, x: list, values: list, type_label: str, grid=True):
        self.fig_line.axes.plot(x,
                                values[0],
                                '-',
                                color='r',
                                marker='h',
                                label=type_label + "折线图")

        self.fig_line.axes.set_title(type_label + "折线图")
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

    # 绘制柱状图，柱状图该怎么画出那种高、中、低效果，待研究2022/2/22 23:56
    def plot_colums(self, x: list, values: list, type: str, color: str, grid=False):
        self.fig_line.axes.bar(x=x,
                               height=values,
                               align='center',
                               label='asdadssadasd',
                               color=color)
        self.fig_line.axes.set_title(type + "柱状图")
        if grid:
            self.fig_line.axes.grid(True)

        self.fig_line.axes.legend()
        self.fig_line.draw()

    '''
    def plt_multi_line(self, row=None, line=None, type=None):
        
        episode = row
        reward = line[0]
        reward2 = line[1]
        reward3 = line[2]
        
        episode = [1, 2, 3]
        reward = [5, 8, 5]
        reward2 = [4, 6, 6]
        reward3 = [6, 4, 7]
        RL1_date = pd.DataFrame({'iteration': episode, 'reward': reward, 'algo': 'DRL1', 'style': '*'})
        RL2_data = pd.DataFrame({'iteration': episode, 'reward': reward2, 'algo': 'DRL2', 'style': 'h'})
        RL3_data = pd.DataFrame({'iteration': episode, 'reward': reward3, 'algo': 'DRL3', 'style': 'v'})
    '''

    def plt_multi_line(self, row=None, line=None, type_label=None):
        reward = list([])
        reward2 = list([])
        reward3 = list([])

        for i in range(0, len(row)):
            if type_label == '安装时长':
                row[i] = float(row[i])
            reward.append(float(line[0][i]))
            reward2.append(float(line[1][i]))
            reward3.append(float(line[2][i]))
        episode = row
        '''
        episode = [23]
        reward = [35]
        reward2 = [34]
        reward3 = [33]
        '''
        RL1_date = pd.DataFrame({'iteration': episode, 'reward': reward, 'algo': '最高指数', 'style': '*'})
        RL2_data = pd.DataFrame({'iteration': episode, 'reward': reward2, 'algo': '平均指数', 'style': 'h'})
        RL3_data = pd.DataFrame({'iteration': episode, 'reward': reward3, 'algo': '最低指数', 'style': 'v'})

        frames = [RL1_date, RL2_data, RL3_data]
        # pd.concat(frames).plot(kind="bar", x="iteration", y="reward", ax=self.fig_line.axes)
        dataset = pd.concat(frames)
        self.fig_line.axes.grid(True, linestyle='-.')

        sns.set_context("paper", font_scale=1.3, rc={"lines.linewidth": 1.5})

        #  palette：调色板
        ax = sns.relplot(x="iteration", y="reward", ax=self.fig_line.axes, palette=['r', 'b', 'g'], hue="algo", ci="5",
                         kind="line", markers=True, style='style',
                         data=dataset, legend='brief')

        x_ticks = None

        if type_label == '温度':  # 温度规定，温度范围从-20℃~50℃，以2℃间隔段为一个点。
            x_ticks = np.arange(-20, 50, 2.0)
            self.fig_line.axes.set_xticks(x_ticks)
            self.fig_line.axes.set_xlabel("温度（℃）", fontsize=13)
        elif type_label == '安装时长':
            #x_ticks = np.arange(1, 4, 1)
            #self.fig_line.axes.set_xticks(x_ticks)
            self.fig_line.axes.set_xlabel("安装时长（月）", fontsize=13)
        elif type_label == '使用频率':
            self.fig_line.axes.set_xlabel("使用频率", fontsize=13)


        self.fig_line.axes.set_ylabel("风险等级指数", fontsize=13)

        self.fig_line.axes.legend(title='', loc='lower right', labels=["最高指数", "平均指数", "最低指数"])


    # 绘制柱状图，画出那种高、中、低效果 主要
    def plt_multi_colums(self, row=None, line=None, type_label=None):
        '''
        episode = [1, 2, 3]
        reward = [5, 8, 5]
        reward2 = [4, 6, 6]
        reward3 = [6, 4, 7]
        '''
        episode = row
        reward = line[0]
        reward2 = line[1]
        reward3 = line[2]

        RL1_date = pd.DataFrame({'iteration': episode, 'reward': reward, '等级指数': '最高指数', 'palette': 'r'})
        RL2_data = pd.DataFrame({'iteration': episode, 'reward': reward2, '等级指数': '平均指数', 'palette': 'b'})
        RL3_data = pd.DataFrame({'iteration': episode, 'reward': reward3, '等级指数': '最低指数', 'palette': 'g'})

        frames = [RL1_date, RL2_data, RL3_data]
        #pd.concat(frames).plot(kind="bar", x="iteration", y="reward", ax=self.fig_line.axes)
        dataset = pd.concat(frames)

        #  palette：调色板

        ax = sns.catplot(x="iteration", y="reward", ax=self.fig_line.axes, palette=['r', 'b', 'g'], hue="等级指数", ci="sd", kind="bar", data=dataset, legend=True)

        #sns.despine(top=False, right=False, left=False, bottom=False)
        #ax.set(xlabel='Iteration', ylabel='风险等级指数')
        self.fig_line.axes.set_ylabel("风险等级指数", fontsize=13)
        if type_label == '生产厂家':
            self.fig_line.axes.set_xlabel("生产厂家", fontsize=13)
        elif type_label == '运营商':
            self.fig_line.axes.set_xlabel("运营商", fontsize=13)
        elif type_label == '使用频率':
            self.fig_line.axes.set_xlabel("使用频率", fontsize=13)
        #self.fig_line.axes.legend(title='', loc='upper right', labels=["最高指数", "平均指数", "最低指数"])
        #plt.show()
        #self.fig_line.draw_idle()

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

    # 添加表格到tableView区 2022/2/27

    # 获取最初的数据模型
    def get_initial_model(self, data=None, type_label=None):
        head = None
        if type_label == '安装时长':
            head = list(['安装时长（月）', '最高（风险等级指数）台数', '平均（...）', '最低（...）'])
        elif type_label == '生产厂家':
            head = list(['生产厂家', '最高（风险等级指数）台数', '平均（...）', '最低（...）'])
        elif type_label == '运营商':
            head = list(['运营商', '最高（风险等级指数）台数', '平均（...）', '最低（...）'])
        elif type_label == '使用频率':
            head = list(['使用频率', '最高（风险等级指数）台数', '平均（...）', '最低（...）'])
        elif type_label == '温度':
            head = list(['温度（℃）', '最高（风险等级指数）台数', '平均（...）', '最低（...）'])
        model = get_row_model(2, header=head)
        self.init_model = self.add_data(model, data)

    # 向模型添加数据
    def add_data(self, model: QStandardItemModel, data) -> QStandardItemModel:
        #line1 = list(['', 0, 3, 0])
        for i in data:
            row = []
            for j in range(len(i)):
                item = QStandardItem(str(i[j]))
                row.append(item)
            model.appendRow(row)
        return model


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = PlotSubWindow()
    win.show()
    sys.exit(app.exec())
