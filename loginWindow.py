
##   ========================== 导入区 ==========================#
import sys

from PyQt5.QtWidgets import (QDialog, QApplication, QMessageBox, QLabel)

from PyQt5.QtCore import (Qt, pyqtSlot, pyqtSignal, QRegExp)

from PyQt5.QtGui import QPixmap

from UI.Ui_LogInWindow import Ui_LogInWindow

from Common import get_db_connection, get_logger, show_error_message, \
    show_information_message, close_db, get_validator

from SigninWindow import SigninWindow

##   =========================================================   ##


#登录窗口
class User:
    def __init__(self, *args):
        self.name, self.grade = args

# 登录窗口类
class LoginWindow(QDialog):
    userSignal = pyqtSignal(User)  #自定义信号：用户变动信号

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.__UI = Ui_LogInWindow()
        self.__UI.setupUi(self)
        self.logger = get_logger("LogIn")

         ##################################################

         #  ===================== 设置输入限制 =============================== #
        validator = get_validator('[a-zA-z0-9]+$')
        #
        self.__UI.user_name_lineEdit.setValidator(validator) #设置用户名限制器
        #  ================================================================ #

        self.setAutoFillBackground(True)    #设置自动填充背景
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)    #设置固定窗口大小
        self.setAttribute(Qt.WA_DeleteOnClose)  #关闭时删除对象

        ## ======================== 数据库操作 ================================== #
        # 打开数据库连接
        self.connection, self.cursor = get_db_connection()
        ## ====================================================================== #

##   ========================== 自动连接的槽函数区 ==========================#
    #单击【确定】按钮槽函数
    @pyqtSlot()
    def on_btn_confirm_clicked(self):
        username = self.__UI.user_name_lineEdit.text()   #获取用户名
        userpassword = self.__UI.user_password_lineEdit.text()   #获取用户密码

        if self.check_connection(username, userpassword):
            self.accept()  # 设置接收
            self.send_user(username, self.get_grade(username))
            close_db(self.connection, self.cursor)
            self.close()



    #单击【取消】按钮槽函数
    @pyqtSlot()
    def on_btn_cancel_clicked(self):
        self.close()    #关闭窗口，默认拒绝

    #单击【注册用户】按钮槽函数
    @pyqtSlot()
    def on_btn_register_clicked(self):
        signin_window = SigninWindow(self)
        # 设置关闭时删除实例
        signin_window.setAttribute(Qt.WA_DeleteOnClose)
        # 指示该窗口是一个独立的窗口
        signin_window.setWindowFlag(Qt.Window, True)
        signin_window.show()

##   ====================================================================#
    # 检查登录
    def check_connection(self, username, userpassword):
        if not self.check_null(username, userpassword):
            return
        if not self.check_user(username, userpassword):
            return
        if not self.check_is_admin_pass(username):
            return
        return True

    # 检查是否被管理员审核通过
    def check_is_admin_pass(self, username):
        try:
            # todo:SQL查询语句
            sql = "select check_status from user where user_name = binary %s"
            res = self.cursor.execute(sql, [username])
            check_status = self.cursor.fetchall()
        except Exception as e:
            message = "无法获得用户数据,请检查"
            self.logger.warning(message.split(',')[0] + "错误原因" + str(e))
            show_error_message(self, message)
            return

        if res == 0:
            show_information_message(self, "没有找到相关用户信息，请检查")
            return False
        else:
            status = check_status[0][0]
            if status != 1: # 1代表已经审核通过
                show_information_message(self, "未审核，请及时通知管理员审核！！！")
                return False

            return True

    # 检查用户和密码是否填写
    def check_null(self, user, password):
        flg = False

        if user == "" and password == "":
            show_information_message(self, "请输入用户名和密码")
        elif user == "":
            show_information_message(self, "请输入用户名")
        elif password == "":
            show_information_message(self, "请输入用户密码")
        else:
            flg = True

        return flg

    # 检查姓名和密码
    def check_user(self, user, password):
        try:
            # todo:SQL查询语句
            sql = 'select user_name, password from user u where u.user_name = binary %s'
            res = self.cursor.execute(sql, [user])
            #res = self.cursor.execute("""select user_name, password from user u where u.user_name = binary "%s";""" % user)
            userChecked = self.cursor.fetchall()
        except Exception as e:
            message = "无法获得用户数据,请检查"
            self.logger.warning(message.split(',')[0] + "错误原因" + str(e))
            show_error_message(self, message)
            return

        if res == 0:
            show_information_message(self, "没有找到相关用户信息，请检查")
            return False
        else:
            user_name, user_password = userChecked[0]
            if user_password != password:
                show_information_message(self, "密码错误，请重试")
                return False

            return True

    # 获取当前用户权限等级
    def get_grade(self, user):
        # todo:SQL查询语句
        try:
            sql = 'select user_grade from user u where u.user_name = binary %s'
            self.cursor.execute(sql, [user])
            #grade = int(self.cursor.fetchone())

        except Exception as e:
            message = "无法获得数据,请检查"
            self.logger.warning(message.split(',')[0] + "错误原因:" + str(e))
            show_error_message(self, message)
            return
        grade = self.cursor.fetchall()
        return int(grade[0][0])

    # 发送登录用户权限
    def send_user(self, *args):
        res_user = User(*args)
        self.userSignal.emit(res_user)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dia = LoginWindow()
    dia.show()
    sys.exit(app.exec())
