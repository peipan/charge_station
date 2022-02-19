#该文件主要用与与用户表表（User）进行数据交互作用
from Common import get_db_connection, execute_inquiry, show_information_message

class ChargeMapper():
    def __init__(self):
        self.connection, self.cursor = get_db_connection()

