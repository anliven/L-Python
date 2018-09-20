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
print("Result_4:", reduce(lambda x, y: x + y, [1, 3, 5, 7, 9]))

result5 = reduce(fn, [1, 3, 5, 7, 9])  # 将序列变换成整数
print("Result_5:", result5)

# ### functools模块的reduce()
# functools模块：https://docs.python.org/3/library/functools.html
# reduce()函数：https://docs.python.org/3/library/functools.html#reduce
# reduce(func, seq[,init])
#  - 必须接收两个参数：函数func和Iterator；
#  - 在Iterator的第1和2个元素上执行函数func得到结果res，然后将结果res和第3个元素执行函数func，依此类推，直到遍历完成；
#  - 最终将获得一个单一的返回值；
#  - 如果如果指定初始值，函数func将首先作用在初始值和第一个序列元素，而不是序列的前两个元素；
