#! python3
# -*- coding: utf-8 -*-

r = range(0, 4)  # 生成列表[0,1,2,3]

for x in r:  # 利用for循环来访问
    print(x)

print("List : ", list(range(0, 6, 2)))  # 利用list()将range转为列表对象
print("Tuple : ", tuple(range(2, 9, 3)))  # 利用tuple()将range转为元组对象

data = [1, 2, 3, 4]


def func(i):
    """
    :param i:
    :return:
    """
    return i * i


print([func(x) for x in data])  # 列表生成式

print([x * x for x in range(1, 5)])  # 通过表达式来使用列表生成式

sampleList = ["AAA", "bbb", "CCC"]
print([x.lower() for x in sampleList])  # 将所有的字符串变成小写

# ### range() 函数
# 内置range()函数可以生成一个规律的整数序列，一般用在for循环中；
# 语法格式： range(start,end[,step])；
# start：起始下标（可选），默认为0；end：终止下标；step：步长（可选），默认为1；
# 特别注意：下标的实际有效范围是“前开后闭”的，也就是不包括终止下标的元素。
#
# ### 列表生成式
# 通过列表生成式，可以很容易生成有规律的序列;
# 语法格式：[function(x) for x in list];
# 如果function()比较简单，可以不预先定义function()，直接通过表达式来使用列表生成式;
# 如果列表是数字且有规律，可以通过range()函数来生成;
