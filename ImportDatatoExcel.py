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
        column_count = self.cursor.execute("desc %s" % table)
        for i in range(column_count):
            temple = self.cursor\
                .fetchone()
            worksheet.write(0, i, temple[0])
        # 向构建好字段的excel表写入所有的数据记录
        row_count = self.cursor.execute(
                "SELECT * FROM %s WHERE risk_level > 30" % table)
        for i in range(row_count):
            temple = self.cursor.fetchone()
            for j in range(column_count):
                worksheet.write(i + 1, j, temple[j])
                workbook.save(file_path)

        close_db(self.connection, self.cursor)

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
        for i in range(column_count):
            temple = self.cursor\
                .fetchone()
            worksheet.write(0, i, temple[0])
        # 向构建好字段的excel表写入所有的数据记录
        row_count = self.cursor.execute(
                "SELECT * FROM %s" % table)
        for i in range(row_count):
            temple = self.cursor.fetchone()
            for j in range(column_count):
                worksheet.write(i + 1, j, temple[j])
                workbook.save(file_path)

        close_db(self.connection, self.cursor)

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



