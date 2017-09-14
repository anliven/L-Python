# -*- coding: utf-8 -*-
__version__ = '0.1'


def say_hi():
    print('Hi, Chapter06ModuleTest.')


if __name__ == '__main__':  # 判断是否是在直接运行
    print('This program is being run by itself. __name__ ： ', __name__)
else:
    print('I am being imported from another module. __name__ ： ', __name__)

# ### __name__属性
# - 模块是对象，并且每个模块都有一个内置属性__name__；
# - 模块被直接运行时，该模块__name__值就等于'__main__'；
# - 模块被import时 ，该模块__name__值等于该模块名，也就是文件名去掉py扩展名的部分；
#
# ### 自定义模块位置
# - 自定义模块应该放置在sys.path所列出的其中一个目录下，或者自定义包中；
# - 也可以与引用模块在同一目录，这种方式最简单，但很少使用这样扁平化的结构；

