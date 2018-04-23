# -*- coding: utf-8 -*-
__version__ = '0.1'


def say_hello():
    print('Hello, TestPackage.ModuleTest.')


if __name__ == '__main__':  # 判断是否是在直接运行
    print('This program is being run by itself. __name__ ： ', __name__)
else:
    print('I am being imported from another module. __name__ ： ', __name__)


# ### __all__
# 一个string元素组成的list变量，定义了使用“from <module> import *”导入某个模块时能导出的符号（变量，函数，类等）；
# 只有__all__内指定的属性、方法、类可以被导入,
# 如果未定义__all__，模块内的所有符号将被导入，“import *”默认从给定的命名空间导出所有符号（下划线开头的私有变量除外）；
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
# ### 自定义模块位置
# - 自定义模块应该放置在sys.path所列出的其中一个目录下，或者自定义包中；
# - 也可以与引用模块在同一目录，这种方式最简单，但很少使用这样扁平化的结构；
#
# ### 包（Packages）
# - 组织程序的层次结构：变量通常位于函数内部，函数与全局变量通常位于模块内部；
# - 包是用以组织模块的一种层次结构，包含模块与一个特殊的__init__.py文件的文件夹；
# - 每个模块的包中，必须有一个__init__.py文件，才能导入这个目录下的module，在导入一个包时，实际上是导入了包的 __init__.py文件；
# - 可以在__init__.py文件中再导入其他的包或模块；
# - 如果在包的__init__.py定义了变量__all__，那么“from PackageName import *”时，就会把__all__中的子模块和子包导入到当前作用域中；
