# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# 面向对象编程语言(Object Oriented Programming Language)
# 模块(module)是包含函数和变量的Python文件；import这个文件后，可以使用 ‘.’ 操作符访问到模块中的函数和变量；
# 类(class)是在Python文件中包含函数和数据的一种代码结构；
# 将一个类实例化(instance)以后，就得到一个对象(object)；


class MyStuff(object):
    """
    sample.
    """

    def __init__(self):  # __init__函数是一个特殊的初始方法，可以预设重要的变量；self是Python创建的空对象；
        self.fruit = "Fruit, Fruit, Fruit!"  # 初始化空对象

    @staticmethod  # 静态方法
    def apple():
        """
        apples.
        """
        print ("Hi, Apples!")


One = MyStuff()  # 实例化MyStuff类的一个对象
print (One.fruit)
One.apple()  # 引用MyStuff类的apple方法


# 实例化对象的过程
# 1- Python环境获取类的定义信息，创建一个空对象（包含类中def定义的所有函数）；
# 2- 如果类中包含魔法函数（__init__），Python环境会调用这个函数对空对象实现初始化；
# 3- 最后Python将这个新建的空对象赋给一个变量，以供后面使用；


class Song(object):
    """
    sample.
    """

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singing(self):
        """
        sample.
        """
        for line in self.lyrics:
            print (line)

    @staticmethod
    def some_function():
        """
        sample.
        """
        print ("Got called.")


happy_birthday = Song(["Happy birthday to you!", "Happy birthday to you!", "Happy birthday to my Angel！"])
happy_birthday.singing()
happy_birthday.some_function()

# 创建 __init__ 或者类函数时，书写self变量，说明是实例的属性
