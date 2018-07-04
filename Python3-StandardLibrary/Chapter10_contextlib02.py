#! python3
# -*- coding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def func():
    try:
        print("[in __enter__] acquiring resources")
        yield
    finally:
        print("[in __exit__] releasing resources")


with func():
    print("[in with-body] Testing")
    # raise (Exception("something wrong"))

# ### 标准库contextlib模块
# - Utilities for with-statement contexts
# - 官方文档：https://docs.python.org/3/library/contextlib.html
#
# ### with语句
# Python的with语句可以方便地使用资源，而不必担心资源没有关闭；
# 正确实现了上下文管理的任何对象，都可以用于with语句；
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的，但编写仍然繁琐；
#
# ### 使用contextlib模块
# 标准库contextlib提供了自定义上下文管理器的方法，可以简化上下文管理；
# 涉及装饰器（@contextmanager）和yield的使用；
# 可以简单理解为：
#   - yield之前的代码相当于__enter__方法，在进入with语句体之前执行；
#   - yield之后的代码相当于__exit__方法，在退出with语句体的时候执行；
