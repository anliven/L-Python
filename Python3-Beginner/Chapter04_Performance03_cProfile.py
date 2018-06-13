#! python3
# -*- coding: utf-8 -*-
import cProfile
import random


def func1(li):
    l1 = sorted(li)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]


def func2(li):
    l1 = [i for i in li if i < 0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]


testlist = [random.random() for i in range(1000000)]
cProfile.run('func1(testlist)')
cProfile.run('func2(testlist)')

# ### 标准库cProfile和profile模块
# The Python Profilers
# https://docs.python.org/3/library/profile.html
# 两者都是内置的性能分析工具，能够描述程序运行时候的性能，并提供统计数据以定位程序的性能瓶颈；
# 两者接口相同，但profile是由纯Python实现，而cProfile由c语言实现；
#
# ### 标准库pstats模块
# Analysis of the profiler data is done using the Stats class.
# https://docs.python.org/3/library/profile.html#module-pstats
#
# ### 结果说明
# - ncalls：函数调用的次数；
# - tottime：指定函数的总运行时间(不包括调用子函数的运行时间）；
# - percall：函数运行一次的平均时间（第1个percall），等于“tottime/ncalls”；
# - cumtime：指定函数的总运行时间(包括所有子函数的调用运行时间），即函数开始调用到返回的时间；
# - percall：函数运行一次的平均时间（第2个percall），等于“cumtime/ncalls”；
# - filename:lineno(function)：函数调用的具体信息（函数所在的文件名，函数的行号，函数名）；

