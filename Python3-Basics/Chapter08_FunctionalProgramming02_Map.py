#! python3
# -*- coding: utf-8 -*-


def cube(x):
    return x * x * x


print(map(cube, range(1, 11)))  # 把结果作为新的Iterator返回
print(list(map(cube, range(1, 11))))  # map通过函数对列表进行处理得到新的列表，用一个列表来提供返回值


def f(x):
    return x * x


result1 = map(f, [1, 2, 3])  # 返回一个Iterator迭代器，可用for循环来访问
for var in result1:
    print("Result_1:", var)

result2 = map(lambda x: x + 6, [1, 2, 3])  # 匿名函数的形式
for var in result2:
    print("Result_2:", var)

result3 = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 将list所有数字转为字符串
print("Result_3:", result3)

# ### map函数
# map(func, seq1[, seq2])
# 接收两个参数，一个是函数func，一个是Iterator，map将函数func作用于给定序列的每个元素，并把结果作为新的Iterator返回；
# 如果函数func比较简单，可以不事先定义函数，而是以匿名函数的形式来进行计算；
# 注意：对序列中每个值进行批量转化操作后，结果是作为Iterator返回，利用for循环或者next()函数来访问Iterator的每个值；
