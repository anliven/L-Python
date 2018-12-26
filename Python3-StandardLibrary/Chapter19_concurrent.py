# coding=utf-8
import time
import concurrent.futures  # 导入concurrent.futures库


def factorial(x):
    """计算阶乘"""
    num = 1
    for i in range(x):
        num *= i + 1
    return num


NUMBERS = [10000 * i for i in range(1, 15)]


def main():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:  # 创建Process Pool，默认会为每个CPU创建一个Python进程
        for number, result in zip(NUMBERS, executor.map(factorial, NUMBERS)):
            # print('The result of number %d is: %s' % (number, result))
            return number, result


if __name__ == '__main__':

    time_start1 = time.time()
    for n in NUMBERS:
        factorial(n)
        # print('The result of number %d is: %s' % (n, factorial(n)))
    time_end1 = time.time()
    print("test1 cost time: ", time_end1 - time_start1)

    time_start2 = time.time()
    main()
    time_end2 = time.time()
    print("test2 cost time: ", time_end2 - time_start2)

# ### 标准库concurrent.futures模块
# - Launching parallel tasks
# - https://docs.python.org/3/library/concurrent.futures.html
# 默认情况下，Python程序使用一个CPU以单个进程运行；
# 使用concurrent.futures 模块，只需几行代码就能将普通数据处理脚本改变为能并行处理数据脚本，充分利用多核CPU，提高处理速度；
#
# ### executor.map()函数
# - 调用时需要输入辅助函数和待处理的数据列表；
# - 此函数将列表分为多个子列表、并将子列表发送到每个子进程、运行子进程以及合并结果等；
# - 按照和输入数据相同的顺序返回结果，使用zip()函数作为捷径，一步获取输入的内容和每次的匹配结果；
#
# ### 适用场景
# 如果一列数据中的每个数据都能单独处理时，适用此方法（Process Pools）来并行处理，能够较好地提速；
# - 从一系列单独的网页服务器日志里抓取统计数据；
# - 从一堆XML，CSV和JSON文件中解析数据；
# - 对大量图片数据做预处理，建立机器学习数据集；
