#! python3
# -*- coding: utf-8 -*-


def is_even(x):
    return x % 2 == 0


f_sample = filter(is_even, [0, 1, 2, 3, 4, 5, 6])
print(f_sample)
for var in f_sample:  # for循环遍历迭代器
    print(var)

f_sample2 = ("hello", "Python", "world")
result = filter((lambda x: x.find("hello") != -1), f_sample2)  # 筛选出字符串元组中包含hello的所有字符串
for i in result:
    print(i)

f_sample3 = ["abcde", "12345", "hello", "python"]
result = filter((lambda x: len(x) == 6), f_sample3)  # 筛选出字符串列表中长度为6的字符串
for i in result:
    print(i)

# ### filter函数
# 接收两个参数：一个函数和一个序列；
# 用于过滤序列：将函数作用在序列的元素，根据函数返回值True或False，决定是否舍弃该元素，最终返回一个迭代器，内容是原序列的子序列；
