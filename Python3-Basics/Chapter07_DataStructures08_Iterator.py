#! python3
# -*- coding: utf-8 -*-
from collections import Iterable
from collections import Iterator

x = iter("abc")  # 字符串
for i in x:
    print(i)

d = {'one': 1, 'two': 2, 'three': 3}  # 字典
m = iter(d)
for i in d:  # 注意这里i是迭代key
    print(i, d[i])

listSample = [111, 'aaa', "AAA"]  # 列表
print("Is it iterable? ", isinstance(listSample, Iterable))  # 判断一个对象是否是可迭代对象（Iterable）
for i in listSample:
    print(i)
for i, value in enumerate(listSample):  # 内置enumerate函数可以把list变成索引元素对
    print(i, value)

iter_list = iter(listSample)  # iter()读取列表创建迭代器Iterator对象
print("Is it iterator? ", isinstance(iter_list, Iterator))  # 判断一个对象是否是迭代器对象（Iterator）
while True:
    try:
        x = next(iter_list)  # 获得下一个值；如果上一步已经遍历iter_list完成，再次调用next()会报StopIteration的错误
        print(x)
    except StopIteration:  # 遇到StopIteration就退出循环
        break

tupleSample = (222, 'bbb', "BBB")
iter_tup = iter(tupleSample)  # iter()读取元组创建迭代器Iterator对象
for var in iter_tup:  # for循环遍历元组
    print(var, end="")

# ### 可迭代对象（Iterable）
# - 可以直接作用于for循环的对象统称为可迭代对象Iterable；
# - 一类是集合数据类型，如list、tuple、dict、set、str等；
# - 一类是generator，包括生成器和带yield的generator function；
#
# ### 迭代器（Iterator）
# - 可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator；
# - 迭代器可以记住遍历的位置的对象，从第一个元素开始访问，然后依次访问所有的元素;
# - 迭代器只能往前不会后退，而且迭代器是一个惰性计算的序列，只有在需要返回下一个数据时才会计算；
# - 两个基本方法：iter()用来创建迭代器，next()用来访问迭代器的下一个元素；
#
# ### iter()函数
# - 生成器都是Iterator对象;
# - 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象；
#
# ### isinstance()函数
# - isinstance()可以判断一个对象是否是可迭代对象（Iterable）或迭代器对象（Iterator）；
# - Python的for循环本质上就是通过不断调用next()函数实现的；
