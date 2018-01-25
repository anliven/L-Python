#! python3
# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.INFO)


def func(s):
    n = int(s)
    print('>>> n = %d' % n)
    logging.info('### n = %d' % n)
    assert n != 0, 'n is zero!'  # 如果表达式“n != 0”不为True，则抛出“AssertionError: n is zero!”
    return 10 / n


def test():
    func('0')
    func("1")


test()

# ### Debug方法
# 打印
# - 利用print()打印出可能有问题的变量，对比查看
#
# 断言（Assert）
# - assert语句用以断言某事是否为真，如果不是真的，就抛出一个断言失败错误AssertionError；
# - 启动Python解释器时可以用-O参数来关闭assert；
# - 可以用断言（assert）替代print()来查看可能有问题的变量；
#
# logging
# - logging不会抛出错误，可以输出信息到文件，也可以同时输出到不同的地方；
# - 可以指定记录信息的级别：debug，info，warning，error等；
#
# Python的调试器pdb
#
# 支持调试功能的IDE
# - PyCharm：http://www.jetbrains.com/pycharm/
# - Eclipse加上pydev插件
