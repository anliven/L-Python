#! python3
# -*- coding: utf-8 -*-
from collections import Iterable


strSample = "123"
print(isinstance(strSample, Iterable))  # 判断一个对象是否可迭代
for i in strSample:
    print(i)

listSample = [111, 'aaa', "AAA"]
for i, value in enumerate(listSample):  # 内置enumerate函数可以把list变成索引元素对
    print(i, value)

iter_list = iter(listSample)  # iter()读取列表创建迭代器
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
# print(next(iter_list))  # 上一步已经遍历iter_list完成，再次调用next()会报StopIteration的错误

tupleSample = (222, 'bbb', "BBB")
iter_tup = iter(tupleSample)  # iter()读取元组创建迭代器
for var in iter_tup:  # for循环遍历元组
    print(var, end="")

# ### 可以直接作用于for循环的数据类型
# - 一类是集合数据类型，如list、tuple、dict、set、str等；
# - 一类是generator，包括生成器和带yield的generator function；
# - 可以直接作用于for循环的对象统称为可迭代对象Iterable；
# - isinstance()可以判断一个对象是否是Iterable对象；
#
# ### 迭代器（Iterator）
# 迭代器（Iterator）可以记住遍历的位置的对象，从第一个元素开始访问，然后依次访问所有的元素;
# 迭代器只能往前不会后退；
# 两个基本方法：iter()用来创建迭代器，next()用来访问迭代器的下一个元素；
# 字符串、列表或元组对象都能用来创建迭代器，同时也支持for循环遍历；
