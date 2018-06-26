#! python3
# -*- coding: utf-8 -*-
from memory_profiler import profile


@profile
def myFunc():
    num = 1
    for i in range(10000):
        num *= i + 1
    return num


@profile
def my_func2():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == "__main__":
    myFunc()
    my_func2()

# ### memory_profiler
# PyPI: https://pypi.org/project/memory_profiler/
# 分析内存使用情况，统计每行代码占用的内存大小;
