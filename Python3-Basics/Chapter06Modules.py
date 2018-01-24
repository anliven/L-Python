#! python3
# -*- coding: utf-8 -*-
import sys  # import语句导入sys模块，sys模块包含了与Python解释器及其环境有关的函数；
from math import sqrt  # 不建议使用from...import语句
import Chapter06ModuleTest  # 导入同一目录下的自定义模块
import TestPackage.ModuleTest  # 导入自定义包中的模块

Chapter06ModuleTest.say_hi()
print('Version', Chapter06ModuleTest.__version__)

TestPackage.ModuleTest.say_hello()
print('Version', TestPackage.ModuleTest.__version__)

print('\nThe PYTHONPATH is', sys.path)  # 通过“模块名.方法名”方式调用模块里的方法
print("Square root of 36 is", sqrt(36))  # 通过“from...import...语句”引入模块的指定函数，调用时不需要加模块名

print('dir(): ', dir())
print('dir(sys): ', dir(sys))

Chapter06ModuleTest.greeting('Anliven')

# ### 模块（Modules）
# - 模块是一个包含函数和变量的.py文件，可以被其它程序通过import方式导入，从而使用该模块中的函数等功能，提升代码复用性；
# - 默认情况下，导入文件或者模块，Python解释器将在sys.path里找其路径，如果没有则报错；
# - 可以通过设置环境变量PYTHONPATH来指定搜索目录；
# - 模块名不能使用特殊字符和中文，更不能与系统模块名冲突；
#
# ### 使用模块的好处
# - 1.提高代码的可维护性和复用性；
# - 2.避免函数名和变量名冲突:相同名字的函数和变量可以分别存在不同的模块;
#
# ### 引入模块
# - 可以通过“import 语句”或“from…import… 语句”引入模块；
# - 通过“import 语句”引入模块后，必须通过“模块名.方法名”方式调用模块的方法；
# - 通过“from...import...语句”导入模块的指定函数后，调用方法时不需要加模块名；
# - “from support import *”可以引入support模块的所有函数，作用与“import support”一致；
# - 为了使程序更加易读和避免名称冲突，建议使用import语句导入模块，而不是from...import语句；
#
# ### 同时引入多个模块
# - “import 语句”格式：import module1,module2,...；
# - “from...import...语句”可以同时引入多个模块的多个方法，当引入不同模块的相同方法名时，以最后引入的方法为准；
#
# ### 包（Packages）
# - 组织程序的层次结构：变量通常位于函数内部，函数与全局变量通常位于模块内部；
# - 包是按目录来组织模块的一种层次结构，是包含模块与一个__init__.py文件（必须存在）的文件夹；
# - 包可以有多级目录，组成多级层次的包结构，每一个层次都有一个__init__.py文件；
# - 通过包来组织模块，可以避免模块名冲突，只要顶层的包名不冲突，那么其所有模块都不会冲突；
#
# ### dir()
# - 内置dir()函数能够返回由对象所定义的名称列表，能够对任何对象工作；
# - 默认情况（没有提供参数），dir函数将返回当前模块的属性列表；
# - 如果参数是模块名称，函数将返回这一指定模块的名称列表；
#
# ### 第三方模块
# 通过包管理工具pip安装第三方模块;
# 通过PyPI（The Python Package Index）获取:https://pypi.python.org/pypi
#
# ### 安装常用模块
# Anaconda是一个基于Python的数据处理和科学计算平台，内置了许多非常有用的第三方库，简单易用；
# Anaconda官网：https://www.anaconda.com/
# 安装Anaconda完成后，Path环境变量将指向Anaconda自带的Python，其内置的第三方模块安装在自己的路径下，不影响系统已安装的Python目录；
