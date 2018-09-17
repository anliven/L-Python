# -*- coding: utf-8 -*-
from line_profiler import LineProfiler


def test():
    print("this is a test!")


def myFunc(num):
    test()
    count = 1
    for i in range(num):
        count *= i + 1
    return count


if __name__ == '__main__':
    num = 10000
    lp = LineProfiler()
    lp.add_function(test)  # 添加被测试函数
    lp_wrapper = lp(myFunc)
    lp_wrapper(num)
    lp.print_stats()

    lp2 = LineProfiler(test)
    lp2.enable()  # 开始性能分析
    test()
    lp2.disable()  # 停止性能分析
    lp2.print_stats()

# ### line_profiler
# PyPI: https://pypi.org/project/line_profiler/
# 可以统计每行代码的执行次数和执行时间等，时间单位为微秒；
#
# ### 结果说明
# - Total Time： 测试代码的总运行时间
# - File： 代码文件的地址
# - Function： 函数的行号
# - Line： 每行代码的行号
# - Hits： 每行代码的运行次数
# - Time： 每行代码的运行时间
# - Per Hit： 每行代码运行一次的时间
# - % Time： 每行代码运行时间与测试代码的总运行时间的百分比
#
# ### 关于使用方式
# 使用命令行
# - 官方文档示例是在被测函数前加一个装饰器@profile，然后在命令行下通过“kernprof -l -v func.py”方式运行测试代码文件；
# - 但使用了@profile的函数无法直接运行，只能在测试代码性能时加上，正常调用时去掉；
# 使用API（推荐）
# - line_profiler提供了和cProfile类似的API；
# - 不需要使用装饰器，也不需要显式使用kernprof脚本；
