#! python3
# -*- coding: utf-8 -*-
import profile


def profileTest():
    num = 1
    for i in range(10000):
        num *= i + 1
    return num


if __name__ == "__main__":
    profile.run("profileTest()")

# ### 标准库cProfile和profile模块
# The Python Profilers
# https://docs.python.org/3/library/profile.html
# profile和cProfile是内置的性能分析工具，能够描述程序运行时候的性能，并提供统计数据以定位程序的性能瓶颈。
#
# ### 统计数据列
# - ncalls：函数调用的次数；
# - tottime：指定函数的总运行时间(不包括调用子函数的运行时间）；
# - percall：函数运行一次的平均时间（第1个percall），等于“tottime/ncalls”；
# - cumtime：指定函数的总运行时间(包括所有子函数的调用运行时间），即函数开始调用到返回的时间；
# - percall：函数运行一次的平均时间（第2个percall），等于“cumtime/ncalls”；
# - filename:lineno(function)：函数调用的具体信息（函数所在的文件名，函数的行号，函数名）；
