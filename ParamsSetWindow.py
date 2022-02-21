
from Ui_ParametersWindow import Ui_ParametersWindow

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QDialog

from PyQt5.QtCore import pyqtSlot, QCoreApplication

from Common import show_error_message, show_information_message, get_validator

from Util.Plot import Myplot2D

from PyQt5.QtCore import Qt, pyqtSignal

class ParamsSetWindow(QDialog):
    def __init__(self):
        super(ParamsSetWindow, self).__init__()
        self.__UI = Ui_ParametersWindow()
        self.__UI.setupUi(self)

        ##  ================================================================ #
        #self.setAutoFillBackground(True)  # 设置自动填充背景
        #self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 设置固定窗口大小
        #self.setAttribute(Qt.WA_DeleteOnClose)  # 关闭时删除对象

        ##  ===================== 设置输入限制 =============================== #
        validator = get_validator('^(1|(0(.\d{1,10})?))$')
        self.__UI.temper_weight_lineEdit.setValidator(validator)
        self.__UI.error_weight_lineEdit.setValidator(validator)
        self.__UI.use_freq_weight_lineEdit.setValidator(validator)
        self.__UI.humi_weight_lineEdit.setValidator(validator)
        self.__UI.install_time_weight_lineEdit.setValidator(validator)
        self.__UI.maintain_freq_weight_lineEdit.setValidator(validator)

    @pyqtSlot()
    def on_btn_confirm_weight_clicked(self):
        temper_weight = self.str_to_float(self.__UI.temper_weight_lineEdit.text())  # 获取温度权重
        error_weight = self.str_to_float(self.__UI.error_weight_lineEdit.text())   # 获取计量误差权重
        install_time_weight = self.str_to_float(self.__UI.install_time_weight_lineEdit.text()) # 获取安装时长权重
        use_freq_weight = self.str_to_float(self.__UI.use_freq_weight_lineEdit.text())  # 获取使用频率权重
        humi_weight = self.str_to_float(self.__UI.humi_weight_lineEdit.text())  # 获取湿度权重
        maintain_freq_weight = self.str_to_float(self.__UI.maintain_freq_weight_lineEdit.text())  # 获取维护频次权重
        sum = (temper_weight + error_weight + install_time_weight + use_freq_weight + humi_weight + maintain_freq_weight)
        if sum > 1 or sum < 1:
            #提示错误信息
            message = "所有权重不加不等于一！！！"
            show_error_message(self, message)

    def str_to_float(self, s: str):
        if s == '':
            return 0
        s1 = s.split('.')[0]
        s2 = s.split('.')[1]
        if s1 == '1':
            return 1
        div = 1
        for i in range(0, len(s2)):
            div *= 10
        sum = float(int(s2) / div)
        return sum


if __name__ == "__main__":
    import sys
    #QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    dia = ParamsSetWindow()
    #dia.setMinimumSize(1400, 800)
    dia.show()
    sys.exit(app.exec())
