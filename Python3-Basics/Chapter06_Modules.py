# -*- coding: utf-8 -*-
import sys  # import语句导入sys模块，sys模块包含了与Python解释器及其环境有关的函数；
from math import sqrt  # 不建议使用from...import...语句
import Chapter06_ModuleTest as cMT  # 导入同一目录下的自定义模块，并设置别名
import TestPackage as tP  # 导入自定义包，只能使用包中__init__.py文件的内容
import TestPackage.ModuleTest as tMT  # 导入自定义包中的模块
# from TestPackage import ModuleTest as tMT  # 与上一句等效
import os
import pprint

print("# dir(module): ", [n for n in dir(cMT) if not n.startswith("_")])  # 查看模块所有可见的自定义属性
print("# __all__: ", cMT.__all__)  # 查看模块的公共接口

cMT.say_hi()  # 注意观察：“__name__”的输出结果
print('Version', cMT.__version__)

print(tP.PI)  # 通过“包名.变量名”方式调用包中__init__.py文件中的变量
print('Version', tMT.__version__)
tMT.say_hello()  # 通过“模块名.方法名”方式调用模块里的方法

pprint.pprint(sys.path)  # 利用pprint模块中的函数pprint分行打印
mp = os.getcwd() + "\\Chapter06_ModuleTest"
sys.path.append(mp)  # 增加sys.path查找路径
print('# The New PYTHONPATH :\n', sys.path)

print("Square root of 36 is", sqrt(36))  # 通过“from...import...语句”引入模块的指定函数，调用时不需要加模块名
cMT.greeting('Anliven')

# ### 模块（Modules）
# - 模块是一个包含函数和变量的.py文件，可以被其它程序通过import方式导入，从而使用该模块中的函数等功能，提升代码复用性；
# - 默认情况下，导入文件或者模块时，Python解释器将在sys.path里寻找其路径，如果没有则报错；
# - 可以通过设置环境变量PYTHONPATH来指定搜索目录；
# - 模块名不能使用特殊字符和中文，更不能与系统模块名冲突；
# - 任何.py文件都可以作为模块导入；
#
# ### 使用模块的好处
# - 1.可以将复杂功能分类细化，提高代码的可维护性和复用性；
# - 2.避免函数名和变量名冲突:相同名字的函数和变量可以分别存在不同的模块;
#
# ### 引入模块的方式
# 通过“import...”或“from...import...”引入模块；
# - “import 语句”引入模块后，必须通过“模块名.方法名”方式调用模块的方法；
# - “from...import...语句”导入模块的指定函数后，调用方法时不需要加模块名；
# 通过“import...as...”或“from...import...as...”为引入的模块设置别名;
# 通过“from support import *”引入support模块的所有函数，作用与“import support”一致；
# 为了使程序更加易读和避免名称冲突，建议使用import语句导入模块，而不是from...import语句；
# 如果导入的模块不存在，Python解释器会报ImportError错误；
#
# ### 同时引入多个模块
# - “import 语句”格式：import module1,module2,...；
# - “from...import...语句”可以同时引入多个模块的多个方法，当引入不同模块的相同方法名时，以最后引入的方法为准；
#
# ### 重新加载模块
# 可使用标准模块importlib的函数reload，接受一个参数（要重新加载的模块），并返回重新加载的模块；
# 适用场景：在程序运行时修改了模块，并希望这种修改反映到程序中；
#
# ### 目录“__pycache__”
# 当导入模块时，将创建子目录“__pycache__”，包含处理后的文件；
# 以后再导入此模块时，如果.py文件未发生变化，Python将导入处理后的文件，否则将重新生成处理后的文件；
# 删除此目录不会影响程序执行，因为必要时会重新创建；
# 在较旧的Python版本中，是扩展名为.pyc的文件；
#
# ### 包（Packages）
# - 组织程序的层次结构：变量通常位于函数内部，函数与全局变量通常位于模块内部；
# - 模块存储在扩展名为.py文件中，而包是一个必须包含__init__.py文件的目录；
# - 包是按目录来组织模块的一种层次结构，是包含模块与一个__init__.py文件（必须存在）的文件夹；
# - 包可以有多级目录，组成多级层次的包结构，每一个层次都有一个__init__.py文件；
# - 通过包来组织模块，可以避免模块名冲突，只要顶层的包名不冲突，那么其所有模块都不会冲突；
# - 简而言之，包就是一个包含__init__.py文件的文件夹；
#
# ### 引入包
# - 方式一：import Package.Module
# - 方式二：from Package import Module
#
# ### 查看信息
# 通过help(module)查看模块帮助信息；
# 通过dir(module)查看模块方法：
# - 内置dir()函数能够返回由对象所定义的名称列表，能够对任何对象工作；
# - 默认情况（没有提供参数），dir函数将返回当前模块的属性列表；
# - 如果参数是模块名称，函数将返回这一指定模块的名称列表；
#
# ### 第三方模块
# 通过包管理工具pip安装第三方模块；
# 通过PyPI（The Python Package Index）获取:https://pypi.python.org/pypi
# Awesome Python：https://awesome-python.com/ （中文：https://github.com/jobbole/awesome-python-cn）
