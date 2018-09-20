# -*- coding: utf-8 -*-
from datetime import datetime
import functools  # 导入functools模块

now = datetime.now()


def log(func):  # 作为一个decorator，接受一个函数作为参数，并返回一个函数
    def wrapper(*args, **kw):  # wrapper()函数的参数定义是(*args, **kw)，可以接受任意参数的调用
        print('call %s()' % func.__name__)  # 打印日志；通过__name__属性获得函数名
        # wrapper.__name__ = func.__name__  # 不建议这样的方式，复制原始函数的属性到wrapper()函数中
        return func(*args, **kw)  # 调用原始函数

    return wrapper


@log  # @log放到now()函数的定义处，相当于执行了语句“test = log(test)”
def test():
    print(now)


test()  # 调用test()函数，运行test()函数本身之前打印一行日志(执行log()函数中返回的wrapper()函数)
print(test.__name__)  # 经过decorator装饰之后的函数，__name__已变成'wrapper'


def log2(text):  # 3层嵌套的decorator实现自定义log
    def decorator(func):
        @functools.wraps(func)  # 定义wrapper()前，必须加上@functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s().' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('This is a sample.')  # 相当于执行了语句“test2 = log('This is a sample.')(test2)“
def test2():
    print(now)


test2()
print(test2.__name__)

# ### 装饰器（Decorator）
# 利用Python提供的@语法，可以将语句“test = log(test)”简写为“@log”；
#
# ### functools.wraps
# 在定义wrapper()函数时，需要把原始函数的__name__等属性复制到wrapper()函数中，否则有些依赖函数签名的代码执行就会出错；
# 推荐使用内置的functools.wraps()，而不是添加“wrapper.__name__ = func.__name__”的代码；
