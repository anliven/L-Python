# -*- coding: utf-8 -*-
import sys  # import语句导入sys模块，sys模块包含了与Python解释器及其环境有关的函数；
from math import sqrt  # 不建议使用from...import语句
import Chapter06ModuleTest  # 导入同一目录下的自定义模块
import TestPackage.ModuleTest  # 导入自定义包中的模块

Chapter06ModuleTest.say_hi()
print('Version', Chapter06ModuleTest.__version__)

TestPackage.ModuleTest.say_hello()
print('Version', TestPackage.ModuleTest.__version__)

print('\nThe PYTHONPATH is', sys.path)
print("Square root of 36 is", sqrt(36))

print(dir())
print(dir(sys))

# ### 模块（Modules）
# - 模块可以被其它程序导入并运用其功能；
# - 最简单模块是包含函数与变量，以.py为后缀的文件；
# - 默认情况下，导入文件或者模块，Python解释器将在sys.path里找其路径，如果没有则报错；
# - 为了使程序更加易读和避免名称冲突，建议使用import语句导入模块，而不是from...import语句；
#
# ### dir()
# - 内置dir()函数能够返回由对象所定义的名称列表，能够对任何对象工作；
# - 默认情况（没有提供参数），dir函数将返回当前模块的属性列表；
# - 如果参数是模块名称，函数将返回这一指定模块的名称列表；
