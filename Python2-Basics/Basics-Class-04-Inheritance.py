# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Parent(object):
    """
    sample.
    """

    def aaa(self):
        """
        sample.
        """
        print ("Parent---aaa().")

    @staticmethod
    def bbb():
        """
        sample.
        """
        print ("Parent---bbb().")

    def ccc(self):
        """
        sample.
        """
        print ("Parent---ccc().")


class Child(Parent):
    """
    sample.
    """

    def aaa(self):  # 显式覆写：在子类中覆写父类的方法，从而实现新功能；
        """
        sample.
        """
        print ("Child, aaa().")

    def ccc(self):  # 在运行前或运行后覆写 ： 在父类中定义的内容运行之前或者之后再修改行为;
        """
        sample.
        """
        print ("Child, Before Parent ccc().")
        super(Child, self).ccc()  # 相当于Parent.ccc()；
        print ("Child, After Parent ccc().")


class ChildNew(Parent):  # 隐式继承：在父类里定义了一个函数，但没有在子类中定义;
    """
    sample.
    """
    pass  # 创建空的代码区块;


dad = Parent()
dad.bbb()
dad.aaa()
dad.ccc()

son = Child()
son.bbb()  # 调用--隐式继承（Implicit Inheritance）
son.aaa()  # 调用--显式覆写（Explicit Override）
son.ccc()  # 调用--在运行前或运行后覆写

sonNew = ChildNew()
sonNew.bbb()

# 继承(Inheritance)：一个类的大部分或全部功能都是从一个父类中获得；
# 隐式继承（Implicit Inheritance）： 在父类里定义了一个函数，但没有在子类中定义；
# 显式覆写（Explicit Override）： 也被称作重载（Override），就是在子类中覆写父类的方法，从而实现新功能；
