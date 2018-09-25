# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from datetime import timezone

now = datetime.now()
print(now)  # 获取当前日期和时间
print("Date: ", now.date(), " Time: ", now.time())  # 分别获取当前日期与时间
now_utc = datetime.utcnow()
print(now_utc)


dt = datetime(2018, 6, 30, 0, 00)  # 获取指定日期和时间的datetime
print(dt)
print(dt.timestamp())  # 将datetime转换为timestamp

ts = 1218124800.0
print(datetime.fromtimestamp(ts))  # 将timestamp转换为本地时间(系统设定时区的时间)的datetime
print(datetime.utcfromtimestamp(ts))  # 将timestamp转换为UTC时间(UTC+0:00时区的时间)的datetime

dt2 = datetime.strptime('2018-6-30 00:00:00', '%Y-%m-%d %H:%M:%S')  # str转换为datetime
print(dt2)
print(now.strftime('%a, %b %d %H:%M'))  # datetime转换为str

print(now + timedelta(days=2, hours=12))  # 可以直接用+和-运算符对日期和时间进行加减(往后或往前计算)

dt_utc = now_utc.replace(tzinfo=timezone.utc)  # 获取UTC时间，并强制设置时区为UTC+0:00
print(dt_utc)
dt_bj = dt_utc.astimezone(timezone(timedelta(hours=8)))  # 转换时区为北京时间
print(dt_bj)

# ### 标准库datetime模块
# - Basic date and time types
# - https://docs.python.org/3/library/datetime.html
#
# ### datetime
# - datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间；
# - 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关；
#
# ### timestamp
# 当前时间相对于epoch time（1970年1月1日 00:00:00 UTC+00:00时区）的秒数；
# 1970年以前的时间timestamp为负数；
# timestamp的值与时区毫无关系，全球各地任意时刻的timestamp都是完全相同的；
# 注意：Python的timestamp是一个浮点数，小数位表示毫秒数；
#
# ### 时区转换
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区；
