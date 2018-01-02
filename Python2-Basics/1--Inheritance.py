# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# 继承(Inheritance)：一个类的大部分或全部功能都是从一个父类中获得；
# 隐式继承（Implicit Inheritance）： 在父类里定义了一个函数，但没有在子类中定义；
# 显式覆写（Explicit Override）： 也被称作重载（Override），就是在子类中覆写父类的方法，从而实现新功能；

class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):
    def override(self):  # 显式覆写（Explicit Override）： 在子类中覆写父类的方法，从而实现新功能；
        print "CHILD override()"

    def altered(self):  # 在运行前或运行后覆写 ： 在父类中定义的内容运行之前或者之后再修改行为
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()  # Python 的内置函数 super。这里是用 super 来获取 Parent.altered。
        print "CHILD, AFTER PARENT altered()"


class ChildNew(Parent):  # 隐式继承（Implicit Inheritance）： 在父类里定义了一个函数，但没有在子类中定义
    pass  # pass 是在 Python 中创建空的代码区块的方法。


# 实例化对象
dad = Parent()
son = Child()
sonNew = ChildNew()
# 调用--隐式继承（Implicit Inheritance）
dad.implicit()
son.implicit()
sonNew.implicit()
# 调用--显式覆写（Explicit Override）
dad.override()
son.override()
# 调用--在运行前或运行后覆写
dad.altered()
son.altered()

