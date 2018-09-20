# -*- coding: utf-8 -*-
__version__ = '0.1'


def say_hello():
    print('Hello, TestPackage.ModuleTest.')


if __name__ == '__main__':  # 判断是否是在直接运行
    print('This program is being run by itself. __name__ ： ', __name__)
else:
    print('I am being imported from another module. __name__ ： ', __name__)

# ### 包（Packages）
# - 组织程序的层次结构：变量通常位于函数内部，函数与全局变量通常位于模块内部；
# - 模块存储在扩展名为.py文件中，而包是一个必须包含__init__.py文件的目录；
# - 包是用以组织模块的一种层次结构，包含模块与一个特殊的__init__.py文件的文件夹；
# - 每个模块的包中，必须有一个__init__.py文件，才能导入这个目录下的module，在导入一个包时，实际上是导入了包的 __init__.py文件；
# - 可以在__init__.py文件中再导入其他的包或模块；
# - 如果在包的__init__.py定义了变量__all__，那么“from PackageName import *”时，就会把__all__中的子模块和子包导入到当前作用域中；
#
# ### 示例
# 假设一个包里有三个模块：mod1.py、mod2.py、mod3.py
# 在__init__.py文件中设置“__all__ = ['mod1','mod3']”，使用“from PackageName import *”导入模块时，就只有只有mod1和mod3被导入；
