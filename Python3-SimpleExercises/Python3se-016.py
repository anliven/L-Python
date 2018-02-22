#! python3
# -*- coding: utf-8 -*-
from functools import reduce  # 引入functools模块的reduce函数


def product(x, y):
    return x * y


print(reduce(product, [1, 4, 9, 16, 25]))

# 求一个整数列表所有元素的积；
