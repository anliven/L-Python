# -*- coding: utf-8 -*-
import sys  # sys模块（特定系统的功能）：https://docs.python.org/3/library/sys.html
import platform  # platform模块（获取平台或操作系统的信息）：https://docs.python.org/3/library/platform.html
import os  # os模块（操作系统交互）：https://docs.python.org/3/library/os.html
import logging

print('Python Version: ', sys.version, '\nPlatform:', sys.platform, '\nInfo:', sys.version_info)
print('OS Version: ', platform.version(), '\nPlatform:', platform.platform(), '\nPython:', platform.python_version())

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getcwd(), 'test.log')  # os.path.join()函数聚合位置信息，并符合当前操作系统的预期格式
else:
    logging_file = os.path.join(os.getenv('PWD'), 'test.log')

print("Logging to", logging_file)

logging.basicConfig(  # 通过basicConfig来进行全局配置，以特定的格式将信息写入指定的文件
    level=logging.INFO,  # 设置只输出INFO级别的信息
    datefmt='%Y/%m/%d %H:%M:%S',  # 指定时间的输出格式
    format='%(asctime)s -- %(lineno)d -- %(process)d -- %(name)s -- %(levelname)s -- %(message)s',  # 指定日志输出格式
    filename=logging_file,  # 日志输出的文件名
    filemode='w',  # 指定日志文件的写入方式（ w：清除后写入，a：追加写入）
)
logger = logging.getLogger(__name__)  # 声明一个Logger对象，是日志输出的主类
print("logger name:", logger.name)  # 初始化时已传入模块名称“__name__”
logger.debug("Start of the program.")  # 调用对象的debug()方法输出DEBUG级别的日志信息
logger.info("Doing something.")
logging.warning("Done.")  # 注意和上一行代码的区别
logging.shutdown()  # 关闭logging之后，可以删除日志文件

# with语句获取由open语句返回的对象，在代码块执行之前调用对象的__enter__函数，之后调用对象的___exit__函数
with open(logging_file) as f:
    for line in f:
        print(line, end='')

os.remove(logging_file)

# ### Python标准库（Python Standard Library）
# - 标准库是标准的Python安装包中的一部分，包含了大量有用的模块，能够满足和实现大部分的功能需求；
# - 熟悉Python标准库将极大地有助于解决问题；
#
# ### 一些文档
# - Python标准库文档: http://docs.python.org/3/library/
# - Python 3 Module of the Week : https://pymotw.com/3/
#
# ### 标准库logging模块
# - Logging facility for Python
# - https://docs.python.org/3/library/logging.html
#
# ### logging模块相比print的优点
# - 设置输出等级：通过设置不同的输出等级来记录对应的日志；
# - 设置输出位置：标准输出流、写入文件、写入远程服务器等；
# - 灵活的配置和格式化功能：输出当前模块信息、运行时间等；
#
# ### logging模块日志信息的输出格式
# 借助basicConfig进行全局配置格式化输出内容
# - %(levelno)s ：打印日志级别的数值
# - %(levelname)s ：打印日志级别的名称
# - %(pathname)s ：打印当前执行程序的路径，其实就是sys.argv[0]
# - %(filename)s ：打印当前执行程序名
# - %(funcName)s ：打印日志的当前函数
# - %(lineno)d ：打印日志的当前行号
# - %(asctime)s ：打印日志的时间
# - %(thread)d ：打印线程ID
# - %(threadName)s ：打印线程名称
# - %(process)d ：打印进程ID
# - %(processName)s ：打印线程名称
# - %(module)s ：打印模块名称
# - %(message)s ：打印日志信息
#
# ### 输出日志的等级
# logging模块的每个日志等级都对应了一个数值，系统只会输出大于或等于该指定日志等级数值的日志；
# 例如设置输出日志level为INFO，那么将不会输出DEBUG和NOTSET级别的日志；
# - CRITICAL、FATAL --- 50
# - ERROR --- 40
# - WARNING、WARN（WARNING的简写形式） --- 30
# - INFO --- 20
# - DEBUG --- 10
# - NOTSET --- 0
