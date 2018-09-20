# -*- coding: utf-8 -*-
__all__ = ['ModuleTest']

PI = 3.1415926

# ### __all__
# 一个string元素组成的list变量，定义了使用“from <module> import *”导入某个模块时能导出的符号（变量，函数，类等）；
# 只有__all__内指定的属性、方法、类可以被导入,
# 如果未定义__all__，模块内的所有符号将被导入，“import *”默认从给定的命名空间导出所有符号（下划线开头的私有变量除外）；
# 在模块中使用__all__属性可避免在相互引用时的命名冲突;
# 特别注意：
# - __all__只限制了“from <module> import *”方式，对“from <module> import <member>”方式没有影响，仍然可以从外部导入；
# - __all__如果设置在__init__.py文件中，意为包里可导出的模块；
