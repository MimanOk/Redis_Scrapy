# -*- coding: utf-8 -*-
# : Time    : 2020/05/14
__author__ = "Miman"


import logging

class ContextFilter(logging.Filter):
    """ 定制用户id """
    def filter(self, record):
        # user_id 可以改成其他名字，后面格式化时对应即可
        record.user_id = '123'
        return True

# 设置log的名字
logger = logging.getLogger(__name__)
# 设置logger对象的log的等级
logger.setLevel(logging.DEBUG)

# 实例化流句柄
log_con = logging.StreamHandler()
# 设置该流的log等级
log_con.setLevel(logging.DEBUG)
# 格式化输出，固定名称写法
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s - %(message)s")
log_con.setFormatter(formatter)
# 添加到logger对象
logger.addHandler(log_con)

# 实例化文件流句柄
log_file = logging.FileHandler("file.log")
# 设置文件流log等级
log_file.setLevel(logging.INFO)
# 格式化输出，固定名称写法
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)-8s - %(user_id)s - %(message)s")
log_file.setFormatter(formatter)
# 使用ContextFilter类来设置日志输出id
logger.addFilter(ContextFilter())
# 添加到logger对象
logger.addHandler(log_file)

logger.debug("->> debug level 10")
logger.info("->> info level 20")
logger.warning("->> warning level 30")
logger.error("->> error level 40")
logger.critical("->> critical level 50")