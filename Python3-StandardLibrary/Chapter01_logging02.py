#! python3
# -*- coding: utf-8 -*-
import logging
import sys

logger = logging.getLogger(__name__)  # 声明一个Logger对象
logger.setLevel(level=logging.DEBUG)  # 设置log level
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 设置log formatter
formatter2 = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

file_handler = logging.FileHandler('Chapter01_logging02_output.log')  # 创建FileHandler对象
file_handler.setLevel(level=logging.INFO)  # 设置handler的log level
file_handler.setFormatter(formatter)  # 设置handler的log输出格式
logger.addHandler(file_handler)  # 添加对应的Handler到Logger对象

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
stream_handler.setFormatter(formatter2)  # 如果没有设置Formatter，将只输出了纯粹的日志内容
logger.addHandler(stream_handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')

# ### Handler
# 可以通过设置多个Handler来控制日志的多目标输出；
#
# ### 常用的Handler
# - StreamHandler：logging.StreamHandler；日志输出到流，可以是 sys.stderr，sys.stdout 或者文件;
# - FileHandler：logging.FileHandler；日志输出到文件;
# - SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址;
# - SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog;
# - NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志;
# - MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer;
#
# ### Formatter
# 完成类似basicConfig的作用，设置日志信息的输出格式，可以灵活地为每个Handler单独配置输出格式；
# 使用Formatter的方法：
# 1 - 指定一个Formatter并传入fmt和datefmt参数（指定日志结果的输出格式和时间格式）；
# 2 - 通过Handler对象的setFormatter()方法应用日志根式；
