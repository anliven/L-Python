#! python3
# -*- coding: utf-8 -*-
from contextlib import contextmanager
from contextlib import closing
from urllib import request


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):  # 通过__enter__和__exit__实现实现上下文管理
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('AAA') as q:
    q.query()


class Query2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager  # @contextmanager装饰器接受一个generator
def create_query(name):
    print('Begin')
    qu = Query2(name)
    yield qu  # 这里yield语句将变量qu输出，后续的with ... as语句实际就成了with Query2(name) as语句
    print('End')


with create_query('BBB') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield  # yield调用执行with语句内部的所有语句，最后执行yield之后的语句
    print("</%s>" % name)


with tag("body"):  # 使用@contextmanager实现程序执行前后自动执行特定代码，这里with语句首先执行yield之前的语句
    print("Hello")
    print("Python!")

with closing(request.urlopen('https://www.bing.com'))as page:  # closing()可以将任意对象变为上下文对象，使之能够用于with语句
    data = page.read()
    print('Status:', page.status, page.reason)

# ### 标准库contextlib模块
# - Utilities for with-statement contexts
# - 官方文档：https://docs.python.org/3/library/contextlib.html
#
# Python的with语句可以方便地使用资源，而不必担心资源没有关闭；
# 正确实现了上下文管理的任何对象，都可以用于with语句；
#
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的，但编写仍然繁琐；
# Python的标准库contextlib提供了更简单的实现方法，使用@contextmanager编写generator可以简化上下文管理；
