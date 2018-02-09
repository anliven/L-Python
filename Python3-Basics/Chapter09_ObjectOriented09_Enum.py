#! python3
# -*- coding: utf-8 -*-
from enum import Enum
from enum import unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():  # 遍历枚举类型的所有成员
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数


@unique  # @unique装饰器可以保证没有重复值
class Weekday(Enum):  # 从Enum派生出自定义类，可以更精确地控制枚举类型
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Tue, Weekday['Tue'], Weekday(2), Weekday.Tue.value)  # 访问枚举类型

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# ### Enum类
# 枚举类型定义一个class类型，每个常量都是class的一个唯一实例；
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量；
