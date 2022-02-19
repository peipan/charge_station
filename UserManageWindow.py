import copy

from Common import show_information_message, show_error_message, \
    get_db_connection, close_db, execute_sql, init_tableview, get_row_model, \
    get_user_head, execute_inquiry, get_logger

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QHeaderView

from PyQt5.QtCore import QItemSelectionModel, pyqtSlot, QModelIndex

from PyQt5.QtGui import QStandardItem, QStandardItemModel

from UI.Ui_UserManageWindow import Ui_ManageWindow

from delegate.myDelegates import QmyComboBoxDelegate

import sys


class ManageWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ManageWindow, self).__init__(parent)
        self.UI = Ui_ManageWindow()
        self.UI.setupUi(self)

        self.cur_row = -1
        self.init_model = None
        self.logger = get_logger("manage")

        init_tableview(self.UI.tableView)


        self.get_initial_model()
        # todo:不确定这是否是深拷贝还是只是两个变量同时索引同一个对象
        data_model = self.init_model
        #data_model = copy.deepcopy(self.init_model)  #深拷贝
        selection_model = QItemSelectionModel(data_model)

        self.UI.tableView.setModel(data_model)
        self.UI.tableView.setSelectionModel(selection_model)
        # 设置表格充满这个布局QHeaderView
        self.UI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面

        #
        self.UI.tableView.setItemDelegateForColumn(7, QmyComboBoxDelegate()) #使用代理做审核状态：1：审核通过 0：未通过
        self.UI.tableView.setColumnHidden(0, True) #隐藏第一列

        self.UI.tableView.selectionModel().currentRowChanged.connect(self.do_cur_row_change)

    # 接收行切换
    @pyqtSlot(QModelIndex, QModelIndex)
    def do_cur_row_change(self, cur: QModelIndex, pre: QModelIndex):
        self.cur_row = cur.row()

    # 单击【保存】按钮
    @pyqtSlot()
    def on_btn_save_clicked(self):
        data = self.get_model_data()
        self.execute_update(data)

    # 单击【删除】按钮
    @pyqtSlot()
    def on_btn_delete_clicked(self):
        if self.cur_row != -1:
            res = QMessageBox.information(self, "温馨提示", "确定删除？", QMessageBox.Ok | QMessageBox.Cancel)
            if res == QMessageBox.Ok:
                self.execute_delete()

                model = self.UI.tableView.model()
                model.removeRow(self.cur_row)

    # 单击【重置】按钮  重置并没有实现
    @pyqtSlot()
    def on_btn_reset_clicked(self):
        self.UI.tableView.setModel(self.init_model)

    # 单击【退出】按钮
    @pyqtSlot()
    def on_btn_quit_clicked(self):
        self.close()

    # 执行删除语句
    def execute_delete(self):
        connection, cursor = get_db_connection()
        model = self.UI.tableView.model()

        ID = int(model.item(self.cur_row, 0).text())

        # todo:删除语句按ID
        sql = "delete from user where uid = %s"
        execute_sql(sql, [ID], connection=connection, cursor=cursor, on=False)

    # 获取最初的数据模型
    def get_initial_model(self):
        head =  list(get_user_head().values())
        model = get_row_model(8, header=head)
        connection, cursor = get_db_connection()

        flg, res, data = self.get_initial_data(connection, cursor)

        if not flg:
            show_information_message(self, "查询失败")
        else:
           if res == 0:
               self.init_model = model
           else:
               self.init_model = self.add_data(model, data)

    # 获取最初的信息
    def get_initial_data(self, connection, cursor):
        # todo：SQL查询语句
        sql = """select * from user"""

        return execute_inquiry(sql, None, connection=connection, cursor=cursor)

    # 向模型添加数据
    def add_data(self, model: QStandardItemModel, data) -> QStandardItemModel:
        for i in data:
            row = []
            for j in range(len(i)):
                if j == 7:
                    if i[j] == 0:
                        item = QStandardItem("未审核")
                    else:
                        item = QStandardItem("审核通过")
                else:
                    item = QStandardItem(str(i[j]))

                row.append(item)

            model.appendRow(row)

        return model

    # 获取模型数据
    def get_model_data(self):
        model = self.UI.tableView.model()
        col_count = model.columnCount()
        row_count = model.rowCount()
        final_data = []

        for i in range(row_count):
            row = []
            for j in range(col_count):
                data = model.item(i, j).text()
                row.append(data)

            final_data.append(row)

        return final_data

    # 执行更新
    def execute_update(self, data: list):
        connection, cursor = get_db_connection()

        for row in data:
            try:
                ID = int(row[0])
                grade = int(row[6])
                state = str(row[7])
                if state == "未审核" :
                    state = 0
                else:
                    state = 1
            except ValueError as error:
                self.logger.debug("转换错误，错误原因:" + error)
                show_information_message(self, "ID, 等级, 检查状态不能为小数")
                return

            name = row[1]
            password = row[2]
            real_name = row[3]
            telephone = row[4]
            department = row[5]

            # todo:更新语句
            sql = "update user set user_name = %s, password = %s, name = %s, telephone = %s, " \
                  "department = %s, user_grade = %s, check_status = %s where uid = %s"
            execute_sql(sql, [name, password, real_name, telephone, department, grade, state, ID],
                        connection=connection, cursor=cursor, on=False)

        show_information_message(self, "更新完毕")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ManageWindow()
    win.show()
    sys.exit(app.exec())