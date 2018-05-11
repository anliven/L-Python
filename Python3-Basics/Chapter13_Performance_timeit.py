#! python3
# -*- coding: utf-8 -*-
import timeit


def timeTest():
    num = 1
    for i in range(10000):
        num *= i + 1
    return num


if __name__ == "__main__":
    t = timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
    print("t: ", t)
    t2 = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
    print("t2: ", t2.timeit())
    print("t2 repeat: ", t2.repeat(repeat=2))
    t3 = timeit.timeit("timeTest()", setup="from __main__ import timeTest", number=10)
    print("t3: ", t3)

# ### 标准库time模块
# Measure execution time of small code snippets
# https://docs.python.org/3/library/timeit.html
# 只输出输出被测试代码的总运行时间，单位为秒，并不提供详细的统计；
