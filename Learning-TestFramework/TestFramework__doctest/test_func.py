# -*- coding: utf-8 -*-
__author__ = 'Anliven'


def func(arg):
     """TestCase for fun
     >>> func(1)
     1
     """
     print arg

def square(x):
    """
    Squares a number and returns the results.
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x*x

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# 自从Python2.6之后，可以直接在命令行敲上命令运行testmod()来检测,在这里就不需要if语句部分了。
# python -m doctest -v test_func.py