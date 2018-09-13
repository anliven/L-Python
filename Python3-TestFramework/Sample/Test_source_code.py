# coding=utf-8
"""
This is a test!
"""


def rect_area(height, width):
    """This is a sample."""
    return height * width


def square(var_x):  # 在文档字符串中添加doctest测试的内容：此函数在命令行下成功运行的过程
    """
    Squares a number and returns the results.
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return var_x * var_x


def product(var_x, var_y):
    """This is a test!"""
    return var_x * var_y
