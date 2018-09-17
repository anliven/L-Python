# coding=utf-8
from configparser import ConfigParser

CONFIGFILE = "Chapter10_Files08_config.ini"
config = ConfigParser()
config.read(CONFIGFILE)  # 读取配置文件

print(config['messages'].get('greeting'))  # 获取配置文件的messages部分greeting内容
radius = float(input(config['messages'].get('question') + ' '))
print(config['messages'].get('result_message'), config['numbers'].getfloat('pi') * radius ** 2)

# ### 配置文件
# 使用配置文件可以提取代码中符号常量（symbolic constant），改善程序的适应性；
# 但如果针对整个项目的中央共享变量库使用，可能会降低项目的模块化程度（增大耦合度）；
# 使用配置文件时，务必不要破坏抽象（如封装）；
#
# ### 标准库模块configparser
# Configuration file parser
# https://docs.python.org/3/library/configparser.html
# 可在配置文件中使用标准格式；
