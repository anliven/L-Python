#! python3
# -*- coding: utf-8 -*-

r = range(0, 4)  # 生成列表[0,1,2,3]
for x in r:  # 利用for循环来访问
    print(x)

print("List : ", list(range(0, 6, 2)))  # 利用list()将range转为列表对象
print("Tuple : ", tuple(range(2, 9, 3)))  # 利用tuple()将range转为元组对象


def func(i):
    """
    :param i:
    :return:
    """
    return i * i


sampleList1 = [1, 2, 3, 4]
print("new list: ", [func(x) for x in sampleList1])  # 列表生成式，产生新列表
print("old list: ", sampleList1)  # 原始列表保持不变

sampleList2 = ["AAA", "bbb", "CCC"]
print("new list: ", [x.lower() for x in sampleList2])  # 将所有的字符串变成小写
print("old list: ", sampleList2)

listOne = [1, 2, 3, 4, 5]
listTwo = [2 * i for i in listOne if i > 2]  # 通过表达式来使用列表生成式
print('listOne:', listOne)
print('listTwo:', listTwo)
print([2 * x for x in range(1, 6) if x > 2])


# ### range() 函数
# 内置range()函数可以生成一个规律的整数序列，一般用在for循环中；
# 语法格式： range(start,end[,step])；
# start：起始下标（可选），默认为0；end：终止下标；step：步长（可选），默认为1；
# 特别注意：下标的实际有效范围是“前开后闭”的，也就是不包括终止下标的元素。
#
# ### 列表生成式
# 通过列表生成式，可以很容易生成有规律的序列;
# 适用于根据旧表建立新表的场景，有效减少代码数量；
# 语法格式：[function(x) for x in list];
# 如果function()比较简单，可以不预先定义function()，直接通过表达式来使用列表生成式;
# 如果列表是数字且有规律，可以通过range()函数来生成;
