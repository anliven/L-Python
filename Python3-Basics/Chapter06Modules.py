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
print("Square root of 36 is", sqrt(36)) # 通过“from...import...语句”引入模块的指定函数，调用时不需要加模块名；

print(dir())
print(dir(sys))

# ### 模块（Modules）
# - 模块是一个包含函数和变量的.py文件，可以被其它程序通过import方式导入，从而使用该模块中的函数等功能，提升代码复用性；
# - 默认情况下，导入文件或者模块，Python解释器将在sys.path里找其路径，如果没有则报错；
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
# ### dir()
# - 内置dir()函数能够返回由对象所定义的名称列表，能够对任何对象工作；
# - 默认情况（没有提供参数），dir函数将返回当前模块的属性列表；
# - 如果参数是模块名称，函数将返回这一指定模块的名称列表；
