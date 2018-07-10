# -*- coding: utf-8 -*-


class Foo(object):

    def bar(self):
        print('Foo.bar')


def bar(self):
    print('Modified bar')


def new():
    print("New func")


Foo.bar = bar  # 运行时动态替换方法
Foo().bar()
Foo.new = new  # 运行时动态增加方法
Foo.new()

# ### Monkey Patch（猴子补丁）
# 不改变源码，在运行时对功能进行追加和变更，达到“hot patch”的目的；
# 简而言之，猴子补丁就是在运行时对属性做动态修改；
# - 运行时动态替换方法；
# - 运行时动态增加方法；
# 使用Monkey Patch虽然可以动态改变对象属性，快速实现某些功能，但同时也有破坏代码整洁性的风险；
