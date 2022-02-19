
##   ========================== 导入区 ==========================#
from PyQt5.QtCore import (Qt, pyqtSlot)

from PyQt5.QtWidgets import (QDialog, QMessageBox)

from UI.Ui_SigninWindow import Ui_SigninDialog

from Common import (get_db_connection, show_information_message, close_db, get_validator, execute_sql)

##   =========================================================   ##


#创建新用户窗口
class SigninWindow(QDialog):
    def __init__(self, parent=None):
        super(SigninWindow, self).__init__(parent)
        self.UI = Ui_SigninDialog()
        self.UI.setupUi(self)

        # 用户名冲突检测标志
        self.name_state = True
        # 密码冲突检测标志
        self.password_state = True

        ## ======================== 设置输入限制 ==================================#
        # 创建限制器，只能输入英文和数字的正则表达式
        validator = get_validator('[a-zA-z0-9]+$')

        # 用户名、密码设置限制器
        self.UI.name_lineEdit.setValidator(validator)
        self.UI.password_lineEdit.setValidator(validator)

        ## =======================================================================#
        # 设置自动填充背景
        self.setAutoFillBackground(True)
        # 设置固定窗口大小
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("注册新用户")

        ## ======================== Mysql数据库操作 ==================================#
        # 打开数据库连接
        self.connection, self.cursor = get_db_connection()
        ## ======================================================================#

##   ========================== 自动连接的槽函数区 ==========================#
    # 单击【保存】按钮槽函数
    @pyqtSlot()
    def on_btn_confirm_clicked(self):
        # 非空检查
        if self.check_null() is False:
            return

        # 如果用户名冲、密码冲突则直接返回
        if self.name_state:
            return

        # 获取注册信息
        name = self.UI.name_lineEdit.text()
        password = self.UI.password_lineEdit.text()
        check_password = self.UI.check_password_lineEdit.text()
        real_name = self.UI.real_name_lineEdit.text()
        telephone = self.UI.telephone_lineEdit.text()
        department = self.UI.department_lineEdit.text()
        user_grade = 0#用户等级 0代表普通用户，1代表管理员
        check_status = 0  # 0代表未审核（注册的时候），1代表管理员审核通过（只有这个标记位为1的时候才能登录进去）

        if password != check_password:
            # 给出警告
            QMessageBox.warning(self, "提示", "密码两次输入不相同，请检查", QMessageBox.Ok)
            return
        ## ======================== MYSQL数据库更改 ==================================#
        # 区分大小写
        # todo:SQL插入语句
        sql = "insert into user(user_name, password, name, telephone, department, user_grade, check_status) " \
              "values(%s, %s, %s, %s, %s, %s, %s)"
        res = execute_sql(sql, [name, password, real_name, telephone, department, user_grade, check_status],
                          connection=self.connection, cursor=self.cursor)
        if res:
            show_information_message(self, "创建成功")
            show_information_message(self, "请通知管理员审核申请！")
            self.close() #关闭自身窗口

        else:
            show_information_message(self, "创建失败，请检查")

    #用户名修改完成槽函数
    @pyqtSlot()
    def on_name_lineEdit_editingFinished(self):
        name = self.UI.name_lineEdit.text()
        # todo:SQL查询语句
        sql = "select user_name from user u where u.user_name = %s;"

        try:
            import pymysql.cursors
            affected_row = self.cursor.execute(sql, [name])

        except:
            show_information_message(self, "无法获得数据，请检查")

        # 改变冲突状态
        if affected_row != 0:
            self.name_state = True
            show_information_message(self, "用户名已经存在，请更改")
        else:
            self.name_state = False

    # 密码检查
    @pyqtSlot()
    def on_password_lineEdit_editingFinished(self):
        self.password_check()

    # 密码检查
    @pyqtSlot()
    def on_check_password_lineEdit_editingFinished(self):
        self.password_check()

    # 密码检查
    def password_check(self):
        password = self.UI.password_lineEdit.text()
        check_password = self.UI.check_password_lineEdit.text()

        if password != '' and check_password != '':
            # 如果两次密码不一致则给出提示
            if password != check_password:
                self.password_state = True
                show_information_message(self, "密码两次输入不相同，请检查")
            else:
                self.password_state = False

    #单击【取消】按钮槽函数
    @pyqtSlot()
    def on_btn_cancel_clicked(self):
        # 关闭窗口
        self.close()

    # 检查非空
    def check_null(self):
        flg = False
        if self.UI.name_lineEdit.text() == '':
            return flg
        elif self.UI.password_lineEdit.text() == '':
            return flg
        elif self.UI.check_password_lineEdit.text() == '':
            return flg
        elif self.UI.real_name_lineEdit.text() == '':
            return flg
        elif self.UI.department_lineEdit.text() == '':
            return flg
        elif self.UI.telephone_lineEdit.text() == '':
            return flg
        else:
            flg = True

        return flg


