
import matplotlib.pyplot as plt
from matplotlib import cbook

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QSizePolicy


# 画图类
class Myplot2D(FigureCanvas):
    def __init__(self, parent=None, width=15, height=10, dpi=100):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置支持中文
        plt.rcParams['axes.unicode_minus'] = False  # 设置-号

        self.fig = plt.figure(figsize=(width, height), dpi=dpi)  # 创建一个新的图框

        #########################解决一个bug: {AttributeError}'Myplot2D' object has no attribute '_draw_pending'############################
        self._draw_pending = None
        self._is_drawing = None
        #########################解决一个bug############################

        FigureCanvas.__init__(self, self.fig)  # 激活图框，必须要有这句话！！
        self.setParent(parent)  # 设定父类，！注：暂不指定父类，用来以后修改继承从而增加新的功能
        self.axes = self.fig.add_subplot(111)  # 打开一个分图片显示区域
        self.fig.subplots_adjust(hspace=0.3, wspace=0.3)

        # 设置画布的尺寸策略
        FigureCanvas.setSizePolicy(self, QSizePolicy.Ignored, QSizePolicy.Ignored)
