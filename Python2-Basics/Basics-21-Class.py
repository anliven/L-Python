# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class TheMultiplier(object):
    """
    sample.
    """

    def __init__(self, base):  # __init__函数是一个特殊的初始方法，可以预设重要的变量；self是Python创建的空对象；
        self.base = base  # 初始化空对象

    def do_it(self, m):
        """
        :param m:
        :return:
        """
        return m * self.base


x = TheMultiplier(20)
print ("Multiplier: "), (x.do_it(30))
