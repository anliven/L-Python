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

# ### 标准库timeit模块
# Measure execution time of small code snippets
# https://docs.python.org/3/library/timeit.html
# 可以对小段Python代码的运行时间进行简单测试；
# 只输出输出被测试代码的总运行时间，单位为秒，并不提供详细的统计；
# 如果要进行详尽的性能分析，建议使用profile或cProfile模块；
#
# ### 重要的事
# “沉迷性能分析”和“过早的、不成熟的优化”是程序实现的万恶之源；
# 清晰而易于理解的代码实现，应该首先得到关注；
