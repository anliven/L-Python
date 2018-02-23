#! python3
# -*- coding: utf-8 -*-
import functools

print(int('123'))  # 字符串转换为整数
print(int('123', base=8))  # base参数可以设置转换的进制，默认值为10
print(int('123', 16))  # 打印16进制字符串对应的10进制整数

int2 = functools.partial(int, base=2)  # 定义int2()的函数，默认把base=2传进去
print(int2('1000000'))  # 打印二进制字符串对应的10进制数
print(int2('1010101'))

# ### 偏函数（Partial Function）
# 这里偏函数的含义为：设定函数的某些参数默认值，返回一个新函数，然后可以简洁地调用这个新函数；
# 当函数的参数个数太多，需要简化时，可以利用functools.partial创建一个参数少的新函数（偏函数），简化调用
