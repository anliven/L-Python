# -*- coding: utf-8 -*-
__version__ = '0.1'
__all__ = ["say_hi", "greeting"]


def say_hi():
    print("Hi,", __name__)


def _private_1(name):
    print('Hello, %s' % name)


def _private_2(name):
    print('Hi, %s' % name)


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':  # 判断是否是在直接运行
    print('This program is being run by itself. __name__ ： ', __name__)
    say_hi()
else:
    print('I am being imported from another module. __name__ ： ', __name__)

# ### __all__
# 一个string元素组成的list变量，定义了使用“from <module> import *”导入某个模块时能导出的符号（变量，函数，类等）；
# 只有__all__内指定的属性、方法、类可以被导入,
# 如果未定义__all__，则会在以“import *”方式导入时，导入所有不以下划线开头（私有变量）的全局名称；
# 在模块中使用__all__属性可避免在相互引用时的命名冲突;
# 特别注意：
# - __all__只限制了“from <module> import *”方式，对“from <module> import <member>”方式没有影响，仍然可以从外部导入；
# - __all__如果设置在__init__.py文件中，意为包里可导出的模块；
#
# ### __name__
# - 模块是对象，并且每个模块都有一个内置属性__name__；
# - 模块被直接运行时，该模块__name__值就等于'__main__'；
# - 模块被import时 ，该模块__name__值等于该模块名，也就是文件名去掉py扩展名的部分；
#
# ### 自定义模块的存放位置
# - 自定义模块应该放置在sys.path所列出的其中一个目录下，或者自定义包中；
# - 也可以与引用模块在同一目录，这种方式最简单，但很少使用这样扁平化的结构；
# - 直接修改sys.path来告知解释器，此方法不常见也不建议；
# - 标准做法是将模块所在目录包含在环境变量PYTHONPATH（也是一个目录列表，内容类似于sys.path，随系统而异）中；
#
# ### 模块的作用域
# 正常的函数和变量是公开的（public），可以被直接引用；
# 通过_前缀来实现的类似__xxx__的变量是有特殊用途的变量，但可以被直接引用；
# 通过_前缀来实现的类似_xxx和__xxx的函数和变量是非公开的（private），从编程习惯上不应该被直接引用，建议仅在模块内部使用；
# Python中无法完全限制访问private函数或变量，仅仅是从编程习惯上建议“不应该”被直接引用；
#
# ### 一种常用的代码封装和抽象
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public;
