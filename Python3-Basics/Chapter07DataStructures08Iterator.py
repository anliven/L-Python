#! python3
# -*- coding: utf-8 -*-


listSample = [111, 'aaa', "AAA"]
iter_list = iter(listSample)  # iter()读取列表创建迭代器
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
# print(next(iter_list))  # 上一步已经遍历iter_list完成，再次调用next()会报StopIteration的错误

strSample = "abc123ABC"
iter_str = iter(strSample)  # iter()读取字符串创建迭代器
print(next(iter_str))
print(next(iter_str))
print(next(iter_str))

tupleSample = (222, 'bbb', "BBB")
iter_tup = iter(tupleSample)  # iter()读取元组创建迭代器
for var in iter_tup:  # for循环遍历元组
    print(var, end="")

# 迭代器（Iterator）可以记住遍历的位置的对象，从第一个元素开始访问，然后依次访问所有的元素;
# 迭代器只能往前不会后退；
# 两个基本方法：iter()用来创建迭代器，next()用来访问迭代器的下一个元素；
# 字符串、列表或元组对象都能用来创建迭代器，同时也支持for循环遍历；
