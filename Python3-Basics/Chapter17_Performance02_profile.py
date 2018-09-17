# -*- coding: utf-8 -*-
import profile
import pstats
import os


def profileTest():
    num = 1
    for i in range(10000):
        num *= i + 1
    return num


if __name__ == "__main__":
    profile.run("profileTest()")
    profile.run("profileTest()", "result.log")  # 指定测试结果的保存文件
    pstats.Stats('result.log').sort_stats(-1).print_stats()  # 格式化显示结果
    os.remove("result.log")

# ### 标准库cProfile和profile模块
# The Python Profilers
# https://docs.python.org/3/library/profile.html
# 两者都是内置的性能分析工具，能够描述程序运行时的性能，并提供统计数据以定位程序的性能瓶颈；
# 两者接口相同，但profile是由纯Python实现，而cProfile由c语言实现；
# cProfile的性能分析速度要快于profile；
#
# ### 标准库pstats模块
# Analysis of the profiler data is done using the Stats class.
# https://docs.python.org/3/library/profile.html#module-pstats
#
# ### 统计数据列
# - ncalls：函数调用的次数；
# - tottime：指定函数的总运行时间(不包括调用子函数的运行时间）；
# - percall：函数运行一次的平均时间（第1个percall），等于“tottime/ncalls”；
# - cumtime：指定函数的总运行时间(包括所有子函数的调用运行时间），即函数开始调用到返回的时间；
# - percall：函数运行一次的平均时间（第2个percall），等于“cumtime/ncalls”；
# - filename:lineno(function)：函数调用的具体信息（函数所在的文件名，函数的行号，函数名）；
