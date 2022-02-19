

from logging.__init__ import Logger

from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QAbstractItemView, QWidget

from PyQt5.QtGui import QRegExpValidator, QStandardItemModel

import configparser

import logging

import pymysql

import logging.handlers


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(threadName)s - %(lineno)d - %(message)s"


# 获取日志管理器
def get_logger(log_name: str, default_level=logging.DEBUG,
               debug_location='Log/debug.log',
               error_location='Log/error.log') -> Logger:
    """

    :param log_name:
    :param default_level:
    :param debug_location:
    :param error_location:
    :return:
    """
    logger = logging.getLogger(log_name)
    logger.setLevel(default_level)

    debug_handler = logging.handlers.TimedRotatingFileHandler(debug_location,
                                                              when='midnight',
                                                              interval=1,
                                                              backupCount=7)

    debug_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    error_handler = logging.FileHandler(error_location)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logger.addHandler(debug_handler)
    logger.addHandler(error_handler)

    return logger


# 初始ini处理器
def get_ini_parser(name, encoding):
    '''
    初始化配置文件读取对象
    :param name: 字符串型，指定要读取的配置文件名称
    :return: 返回该文件的读取对象
    '''
    conf = configparser.ConfigParser()  # 初始化读取对象【conf】
    conf.read(name, encoding=encoding)  # 读取配置文件
    return conf  # 返回配置文件的读取对象


# 获取用户名称
def get_user_head():
    file_path = "Config/normal.ini"
    items_name = "USER_HEAD"
    return read_items_data(file_path, items_name)

# 获取画图类型参数
def get_plot_type():
    file_path = "Config/plot.ini"
    items_name = "PLOT_TYPE"
    return read_items_data(file_path, items_name)


# 获取数据库连接参数
def get_db_param():
    file_path = "Config/connection.ini"
    items_name = 'DB_CONNECTION'
    return read_items_data(file_path, items_name)


# 读取块数据
def read_items_data(file_path, items_name, encoding='utf-8'):
    logger = get_logger("file")
    try:
        parser = get_ini_parser(file_path, encoding=encoding)
        items = parser.items(items_name)

    except configparser.NoSectionError as e:
        logger.warning(e)
        return

    except Exception as e:
        logger.warning(e)
        return

    return {key: value for key, value in items}


# 获取数据库连接
def get_db_connection():
    '''
        连接MYSQL数据库函数
        :return: 返回MYSQL数据库连接和钩子
        '''
    logger = get_logger("connection")
    try:
        param_dict = get_db_param() # 调用函数读取配置信息
        if len(param_dict) != 5:
            raise ValueError

    except ValueError:
        message = "连接参数有误，现有参数{}，需要5".format(len(param_dict))
        logger.warning(message)
        return

    host = param_dict.get("host")
    user = param_dict.get("username")
    password = param_dict.get("userpassword")
    database = param_dict.get("databasename") #"databaseName"这样写是错误的，需要全部小写
    port = int(param_dict.get("port"))

    # 获取数据库连接
    connection = pymysql.connect(host=host, user=user, password=password, port=int(port), database=database)
    cursor = connection.cursor() #获取钩子

    return connection, cursor #返回MYSQL数据库连接和钩子


# 关闭连接
def close_db(connection, cursor):
    connection.close()
    cursor.close()


# 显示错误信息
def show_error_message(parent, message) -> None:
    QMessageBox.warning(parent, "警告", message, QMessageBox.Ok)


# 显示消息
def show_information_message(parent, message: str) -> None:
    QMessageBox.information(parent, "温馨提示", message, QMessageBox.Ok)


# 获取输入限制器
def get_validator(regression: str) -> QRegExpValidator:
    reg = QRegExp(regression)
    validator = QRegExpValidator()
    validator.setRegExp(reg)

    return validator


# 执行插入、删除语句
def execute_sql(sql: str, arg, on=True, **kwargs):
    logger = get_logger("execute")
    flg = False

    # 获取连接和钩子
    if 'connection' not in kwargs:
        return flg
    if 'cursor' not in kwargs:
        return flg

    connection = kwargs['connection']
    cursor = kwargs['cursor']

    # 提交修改, 成功则给出提示，失败则回滚
    try:
        cursor.execute(sql, arg)
        connection.commit()
        flg = True

    except Exception as e:
        connection.rollback()
        logger.warning("执行-->" + sql + "<--错误，错误原因是:" + str(e))
        flg = False

    finally:
        if on:
            # 关闭数据库连接和钩子
            close_db(connection, cursor)

        return flg


# 查询数据
def execute_inquiry(sql: str, arg, **kwargs):
    logger = get_logger("inquiry")
    flg = False
    res = 0

    # 获取连接和钩子
    if 'connection' not in kwargs:
        return flg
    if 'cursor' not in kwargs:
        return flg

    connection = kwargs['connection']
    cursor = kwargs['cursor']

    # 提交修改, 成功则给出提示，失败则回滚
    try:
        if arg is None:
            res = cursor.execute(sql)
        else:
            res = cursor.execute(sql, arg)

        flg = True

    except Exception as e:
        logger.warning("执行-->" + sql + "<--错误，错误原因是:" + str(e))
        flg = False

    if res != 0:
        data = cursor.fetchall()
    else:
        data = None

    return flg, res, data


# 初始化table_view函数
def init_tableview(widget: QWidget, hor_size: int = 100, ver_size: int = 75, alter_color=True):
    # 设置交错颜色
    widget.setAlternatingRowColors(alter_color)
    # 设置选择行为单位
    widget.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 设置只能单选
    widget.setSelectionMode(QAbstractItemView.SingleSelection)
    # 设置单元格大小
    widget.horizontalHeader().setDefaultSectionSize(hor_size)
    widget.verticalHeader().setDefaultSectionSize(ver_size)


# 获取初始模型
def get_row_model(column_count: int, header: list):
    model = QStandardItemModel(0, column_count)
    model.setHorizontalHeaderLabels(header)
    return model


# 记录操作信息
def record_operation():
    pass


