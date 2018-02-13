#! python3
# -*- coding: utf-8 -*-


class Person1:  # 类名通常是大写开头的单词
    pass  # 使用pass语句标明一个空代码块


class Person2:
    def __init__(self, name):  # __init__方法在类的对象被实例化（Instantiated）时立即运行，进行初始化（Initialization）操作
        self.name = name

    def sayhi(self):
        print('Hello, my name is', self.name)


p = Person1()
print(p)  # 打印结果，类的__main__产生了一个实例，以及这个实例对象的内存地址；

p = Person2('Anliven')
p.sayhi()
Person2('Anliven').sayhi()  # 等同于上两行


class Rectangle:
    width = 0  # 定义类的属性
    height = 0

    __color = ""  # 定义类的私有属性

    def __init__(self, width, height, color):  # 定义构造函数
        self.width = width
        self.height = height
        self.__color = color

    def __getArea(self):  # 定义类的私有方法
        return self.width * self.height

    def printme(self):  # 定义类的方法；类内部可调用类的私有属性和私有方法
        print("width = %d,height = %d,area = %d,color = %s" % (self.width, self.height, self.__getArea(), self.__color))

    def get_color(self):  # 定义外部代码获取类私有属性的方法
        return self.__color

    def set_color(self, color):  # 定义外部代码修改类私有属性的方法
        self.__color = color


R = Rectangle(3, 4, "blue")  # 创建类的实例，自动调用__init__()构造方法
print("width =", R.width)  # 访问实例的属性
R.printme()  # 访问实例的方法
# print("color = %s, Area = %d " % (R.__color, R.__getArea()))  # 报错，因为实例无法访问类的私有属性和私有方法

print("__color = ", R.get_color())  # 访问对象的内部状态
R.set_color('red')  # 设置对象的内部状态
print("__color = ", R.get_color())

# ### 使用类
# 使用类将有助于降低复杂性，减少bug，并且使代码更可维护；
# 类可以从零开始创建，也可以从Python的内置类或从其他定制类继承；
#
# ### 类与对象
# - 类(Class): 用来描述具有相同的属性和方法的对象的集合，定义了该集合中每个实例所共有的属性和方法。
# - 通过class关键字创建类；
# - 实例化的对象（Object）是类的实例（Instance）；
#
# ### 类的属性（Attribute）
# - 类的属性包括字段与方法；
# - 字段（Field）：对象或类的变量，分别被称为实例变量（Instance Variables）与类变量（Class Variables）；
# - 将属性名以双下划线开头可将属性定义为私有属性，表示其只能在类内部以self.的方式访问，类的实例（实例）无法访问；
#
# ### 类的方法（Method）
# - 在类中使用def关键字定义的函数，类方法必须包含参数self且为第一个参数，self代表的是类的实例；
# - 方法名以双下划线开头可将方法定义为私有方法，表示表示其只能在类内部访问以self.的方式访问，类的实例（实例）无法访问；
#
# ### self
# - 简单的说，self参数是指类实例自身（也就是对象本身）的引用；
# - 在定义类方法(类中的函数)时，self参数必须存在并且只能作为第一个参数；
# - 即使类的方法不需要任何参数，self也必须存在类的方法中，而独立的函数或方法则不需要；
#
# ### __init__()
# 类的构造方法__init__()会在创建类实例的同时初始化实例；
# 构造方法__init__()的第一个参数必须为self，在创建类的实例时，会自动调用该构造方法；
# 必须传入与__init__方法匹配的参数，但self不需要传(Python解释器会自动处理)
#
# ### 举例说明
# - 创建了一个类MyClass，实例化对象为MyObject，然后调用对象的方法MyObject.method(a,b)；
# - 在此过程中，Python自动将对象的方法转化为Myclass.method(MyObject,a,b)，self参数被赋值为MyObject；
#
# ### 访问限制
# - 属性名称前加上两个下划线__，就变成了一个私有（private）属性，只有内部可以访问，外部不能访问；
# - 但可以通过增加类似get_xxx和set_xxx的方法，间接地实现让外部代码访问和设置类的私有属性和私有方法；
# - 注意：以一个下划线开头的实例变量名，虽然外部是可以访问的，但视为私有变量，不要随意访问；
# - 注意：以双下划线开头并且以双下划线结尾，类似__xxx__的变量是特殊变量，可以直接访问；
