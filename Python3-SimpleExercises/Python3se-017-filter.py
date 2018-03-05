#! python3
# -*- coding: utf-8 -*-
import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


print(list(filter(is_sqr, range(1, 101))))

# 筛选出1~100中平方根是整数的数；
