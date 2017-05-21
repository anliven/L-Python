# -*- coding: utf-8 -*-
__author__ = 'Anliven'

class TheThing(object):
    def __init__(self):
        self.number = 0
    def some_function(self):
        print "I got called."
    def add_me_up(self, more):
        self.number += more
        return self.number

# two different things
a = TheThing()
b = TheThing()
a.some_function()
b.some_function()
print a.add_me_up(20)
print b.add_me_up(30)
print a.number
print b.number

# Study this. This is how you pass a variable from one class to another. You will need this.
class TheMultiplier(object):
    def __init__(self, base):
        self.base = base
    def do_it(self, m):
        return m * self.base
x = TheMultiplier(a.number)
print x.do_it(b.number)


# 如何将变量和状态从一个 class 传递到另一个 class？

# __init__ 是一个特殊的初始方法，可以预设重要的变量在里边

# 理解 self 的概念，以及它在 __init__是怎样使用的