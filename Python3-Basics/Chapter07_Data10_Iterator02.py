# -*- coding: utf-8 -*-
from collections import Iterable
from collections import Iterator

x = iter("abc")  # 通过内置的iter()来获取内置可迭代（iterable）对象相应的迭代器
print(type(x))  # type()查看对象类型
for i in x:
    print(i)

d = {'one': 1, 'two': 2, 'three': 3}  # 字典
m = iter(d)
print(type(m))
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
# ### 区分可迭代对象和迭代器对象
# - 可迭代对象：实现了__iter__()方法，__iter__()返回一个迭代器对象；
# - 迭代器对象：实现了__iter__()和__next__()方法，__iter__()返回的是迭代器对象本身；
#
# ### iter()
# https://docs.python.org/3/library/functions.html#iter
# - 生成器都是Iterator对象;
# - 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象；
#
# ### isinstance()
# https://docs.python.org/3/library/functions.html#isinstance
# - isinstance()可以判断一个对象是否是可迭代对象（Iterable）或迭代器对象（Iterator）；
# - Python的for循环本质上就是通过不断调用next()函数实现的；
#
# ### 迭代的过程
# Python中所有形式的迭代，实质上都是由迭代器协议驱动的；
# - 1.当使用for循环遍历迭代器对象时，会自动调用此对象的__next__()方法，并获取下一个item；
# - 2.当所有的item全部取出后，抛出一个StopIteration异常，告知外部调用者迭代完成；
# - 3.外部调用者尝试去捕获这个异常，做进一步的处理；
#
# ### 创建迭代器对象
# 方法1：使用iter()函数将内置的序列对象转换成相应的迭代器；
# 方法2：实现迭代器协议，也就是在类中实现__iter__()和__next__()方法；
# - __iter__()方法返回迭代器对象本身；
# - __next__()方法返回下一个元素，直到结尾抛出StopIteration异常；
#
# ### 迭代器的限制
# - 迭代器是惰性可迭代对象（延迟工作直到请求下一项）；
# - 迭代器是有状态的（一次性使用），只能循环遍历一次，一旦遍历了某一项，这一项就消失了；
# - 迭代器没有长度（可以创建无限长的迭代器），不能被索引；
