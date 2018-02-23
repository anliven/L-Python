#! python3
# -*- coding: utf-8 -*-
from functools import reduce  # 引入functools模块的reduce函数


def product(x, y):
    return x * y


print(reduce(product, [1, 4, 9, 16, 25]))


def calc_product(lst):
    def count():
        return reduce(lambda x, y: x * y, lst)

    return count


func = calc_product([1, 2, 3, 4])
print(func())

# 求一个整数列表所有元素的积；
