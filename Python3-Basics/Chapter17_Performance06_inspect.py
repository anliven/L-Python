# -*- coding: utf-8 -*-
import inspect
import copy

print("$ Module: ", inspect.getmodule(inspect.getmodule))  # 打印定义了inspect.getmodule()的模块
print("$ Line Number: ", inspect.currentframe().f_lineno)  # 打印本行代码所在的行号

print("$ Module path: ", inspect.getabsfile(copy), inspect.getabsfile(copy.copy))  # 打印copy模块及copy函数的位置
print("$ Function args: ", inspect.getfullargspec(copy.copy))  # 以tuple形式返回函数参数的名称和默认值


def aaa():
    """This is a test!"""
    print("hello")


def bbb(m: int, n: float):
    return m * n


class Test(object):
    def __init__(self, name):
        self.name = name

    def ttt(self):
        print(self.name, "hello world!")


print(inspect.ismodule(aaa), inspect.isclass(aaa), inspect.ismethod(aaa), inspect.isfunction(aaa),
      inspect.isbuiltin(aaa))  # 判断对象类型的几个方法
print("$ Docstring: ", inspect.getdoc(aaa))
print("$ Type of function args: ", str(inspect.signature(bbb)), str(inspect.signature(bbb).parameters['m']))
print("$ Members: ", inspect.getmembers(Test, inspect.isfunction))  # 返回一个包含对象的所有成员的(name, value)列表
print("$ Source Code:\n", inspect.getsource(Test.ttt))  # 打印Test.ttt的源码

# ### 标准库inspect模块
# Inspect live objects
# https://docs.python.org/3/library/inspect.html
# 用于收集Python对象的信息，可以获取类或函数的参数信息、源码、解析堆栈等；
# 通过使用inspect可以有效地了解代码的运行机制；
#
# ### 主要功能
#   1- 类型检查（type checking）
#   2- 获取源码（getting source code）
#   3- 获取类和方法的参数信息（inspecting classes and functions）
#   4- 解析堆栈（examining the interpreter stack）
