#! python3
# -*- coding: utf-8 -*-
from functools import reduce  # 引入functools模块的reduce函数


def f(x, y):
    return x * y


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


result1 = reduce(f, range(1, 6))  # 返回一个值1*2*3*4*5
print("Result_1:", result1)
result2 = reduce((lambda x, y: x * y), range(1, 6))  # 匿名函数的形式，为便于理解加上了括号
print("Result_2:", result2)

result3 = reduce(add, [1, 3, 5, 7, 9])  # 序列求和
print("Result_3:", result3)

result4 = reduce(fn, [1, 3, 5, 7, 9])  # 将序列变换成整数
print("Result_4:", result4)

# ### reduce函数
# 接收两个参数：函数f(必须接收两个参数)和Iterator；
# reduce在Iterator的第一二个元素上执行函数f得到结果res，然后将结果res继续与第三个元素作为函数f的两个参数执行函数f，直到遍历完成；
