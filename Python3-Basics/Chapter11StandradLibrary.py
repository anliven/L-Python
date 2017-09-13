# -*- coding: utf-8 -*-
import sys
import platform
import os
import logging

print('Python Version: ', sys.version, '\nPlatform:', sys.platform, '\nInfo:', sys.version_info)
print('OS Version: ', platform.version(), '\nPlatform:', platform.platform(), '\nPython:', platform.python_version())

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getcwd(), 'test.log')  # os.path.join()函数聚合位置信息，并符合当前操作系统的预期格式；
else:
    logging_file = os.path.join(os.getenv('PWD'), 'test.log')

print("Logging to", logging_file)

logging.basicConfig(  # 配置logging模块，以特定的格式将信息写入指定的文件；
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Start of the program.")
logging.info("Doing something.")
logging.warning("Done.")
logging.shutdown()  # 关闭logging之后，可以删除日志文件

# with语句获取由open语句返回的对象，在代码块执行之前调用对象的__enter__函数，之后调用对象的___exit__函数
with open(logging_file) as f:
    for line in f:
        print(line, end='')

os.remove(logging_file)

# ### Python标准库（Python Standard Library）
# - 标准库是标准的Python安装包中的一部分，包含了大量有用的模块，能够满足和实现基础的功能需求；
# - 熟悉Python标准库将极大地有助于解决问题；
#
# ### 一些文档
# - Python标准库文档: http://docs.python.org/3/library/
# - Python Module of the Week : https://pymotw.com/2/
# - Python 3 Module of the Week : https://pymotw.com/3/
#
# ### 一些标准库
# - sys模块：包括针对特定系统的功能；
# - os模块：用以和操作系统交互；
# - platform模块：用以获取平台或操作系统的信息；
# - logging模块：用来记录信息；
