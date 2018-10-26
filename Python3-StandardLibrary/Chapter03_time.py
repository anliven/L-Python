# -*- coding: utf-8 -*-
import time

print("asctime: ", time.asctime())
print("time: ", time.time())

print("localtime: ", time.localtime())  # 不加参数，显示当前时间
print("localtime: ", time.localtime(1540523874.2708123))  # 将秒数（从新纪元开始后）
print("gmtime: ", time.gmtime())  # 与localtime()作用类似，但采用国际标准时间

# ### 标准库time模块
# Time access and conversions
# https://docs.python.org/3/library/time.html
# 用于获取当地时间、操作时间和日期、从字符串中读取日期、将日期格式化为字符串；
#
# ### “新纪元”
# 一般为距离（1970年1月1日 00:00:00 UTC+00:00时区）的秒数；
# 具体秒数可能随平台而异；
#
# ### 常用方法
# - asctime(): 将时间元组转换为字符串；
# - time()：返回当前的国际标准时间（从新纪元开始后的秒数，以UTC为准）；
# - localtime(): 将秒数（从新纪元开始）转换为日期元组；
# - gmtime()：与localtime()功能类似，但采用国际标准时间；
# - mktime()：与localtime()功能相反，将时间元组转换为从新纪元后的秒数；
# - sleep(x)：休眠（什么都不做，让解释器等待）x秒；
# - strptime()：将字符串（其格式与asctime所返回的字符串格式相同）转换为时间元组；
