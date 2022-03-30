import time

import pymysql
import xlwt
from Common import get_db_connection, close_db


class ImportDatatoExcel:
    def __init__(self):
        super().__init__()
        self.connection, self.cursor = get_db_connection()

    def export_to_excel(self, table, file_path):

        """将MySQL一个数据表导出到excel文件的一个表的函数
        :param    worksheet:  准备写入的excel表
        :param    cursor:     源数据的数据库游标
        :param    table       源数据的数据表
        :return:  Nove.
        """
        # 初始化workook？
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("sheet1")
        # 首先向excel表中写入数据表的字段
        #column_count = self.cursor.execute("desc %s" % table)
        #column_count = 8

        for i in range(8):
            temple = ["充电站名称", "地址", "运营商", "风险等级", "厂家", "型号", "编号识别码", "导出时间"]
            worksheet.write(0, i, temple[i])
        # 向构建好字段的excel表写入所有的数据记录
        row_count = self.cursor.execute(
                "SELECT pid_name, pid_addr, carrieroperator, risk_level, manufacturer, model_type, factory_num FROM %s WHERE risk_level > 30" % table)

        daochu_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        temple = self.cursor.fetchone()
        for i in range(row_count):

            temple = list(temple)
            temple.append(daochu_time)

            for j in range(8):
                worksheet.write(i + 1, j, temple[j])
                workbook.save(file_path)

        #close_db(self.connection, self.cursor)

    def export_to_excel_formwork(self, table, file_path):

        """将MySQL一个数据表导出到excel文件的一个表的函数
        :param    worksheet:  准备写入的excel表
        :param    cursor:     源数据的数据库游标
        :param    table       源数据的数据表
        :return:  Nove.
        """
        # 初始化workook？
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("sheet1")
        # 首先向excel表中写入数据表的字段
        column_count = self.cursor.execute("desc %s" % table)
        temple = self.cursor \
            .fetchone()
        #close_db(self.connection, self.cursor)
        for i in range(column_count):

            worksheet.write(0, i, temple[0])
        # 向构建好字段的excel表写入所有的数据记录
        row_count = self.cursor.execute(
                "SELECT * FROM %s" % table)
        temple = self.cursor.fetchone()
        for i in range(row_count):

            for j in range(column_count):
                worksheet.write(i + 1, j, temple[j])
                workbook.save(file_path)

        #close_db(self.connection, self.cursor)

"""
if __name__ == "__main__":
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("sheet1")
    connect, cursor = Common.get_db_connection()
    export_to_excel('table_charge_station')
    Common.close_db(connect, cursor)
    workbook.save("test_1.xls")
workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("sheet1")
    connect, cursor = Common.get_db_connection()
    export_to_excel('table_charge_station')
    Common.close_db(connect, cursor)
    workbook.save("test_1.xls")
"""



