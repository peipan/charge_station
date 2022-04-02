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
        if temple is None: # 修复点击导出excel的时候出现bug问题 2022/3/31
            return
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
        # 初始化workook？
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("sheet1")
        temple = ["充电开始时间", "充电结束时间", "运营商电话", "充电设备名称", "型号", "出厂编号", "生产厂家", "所属充电站名称", "省市/区", "详细地址",
                  "经度", "维度", "运营商", "安装日期", "安装时长", "是否首检", "充电桩种类", "充电设备接口编码", "充电设备接口类型", "执行的国家标准", "充电桩额定功率（kw）",
                  "各非车载充电机AC - DC转换效率数据", "额定电压上限（V）", "额定电压下限（V）", "额定电流（A）", "最小电流（A）", "脉冲常数（i/kWh）",
                  "电能分辨力（kWh）", "标称等级", "温度（℃）", "相对湿度（%RH）", "累积充电量", "充电站总表累计电量", "站内除充电桩外其他设备累积电量",
                  "各非车载充电机交流侧累积电量", "各非车载充电机直流侧累积电量", "各交流充电桩累积电量", "充电订单号（客户编码）", "电池额定容量",
                  "充电开始电池剩余电量Soc", "充电电开始电池电压", "充电结束电池剩余电量Soc", "充电结束电池电压", "单次充电电量", "计量误差Δn", "计量误差Δn /标称等级",
                  "使用频率（平均每天充电时间/12）", "风险等级指数", "总结论"]
        row_count = ["2022-03-25 00:00:00", "2022-03-26 00:00:00", "138xxxxxxxx", "直流充电桩", "EV-CL-A3", "020200323031",
                     "北京华商三优科技有限公司", "星星充电", "北京市朝阳区", "北京市朝阳区北京工业大学",
                     "116.559404", "39.827266", "星星充电", "2018/5/20", "4", "否", "直流充电桩", "3/4", "", "", 80,
                     "", 450, 20, 200, 5, 3000, "0.01", 1, 25, 40, "", "169.25", 5, "", "45.00", "", "", "", "", "", "",
                     "", "", "", "",
                     "0.23", "", ""]
        for i in range(len(temple)):
            worksheet.write(0, i, temple[i])
            worksheet.write(1, i, None)

        for j in range(len(temple)):
            worksheet.write(2, j, row_count[j])
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



