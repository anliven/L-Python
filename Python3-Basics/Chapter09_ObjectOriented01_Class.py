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

p2 = Person2('Anliven')
p2.sayhi()
Person2('Anliven').sayhi()  # 等同于上两行
print(p2.sayhi)  # 注意：p.sayhi是一个绑定到实例的函数对象，不是方法


class Rectangle:
    width = 0  # 定义类的属性
    height = 0

    __color = ""  # 定义类的私有属性

    def __init__(self, width, height, color, **kwargs):  # 定义可变长参数的构造函数
        self.width = width
        self.height = height
        self.__color = color
        # self.id = kwargs.get('id')  # 不建议这样设置可变长参数的属性
        # self.owner = kwargs.get('owner')
        for k, w in kwargs.items():  # **kwargs是字典类型，推荐设置属性的方式
            setattr(self, k, w)

    def __getArea(self):  # 定义类的私有方法
        return self.width * self.height

    def printme(self):  # 定义类的方法；类内部可调用类的私有属性和私有方法
        print("width = %d,height = %d,area = %d,color = %s" % (self.width, self.height, self.__getArea(), self.__color))

    def get_color(self):  # 定义外部代码获取类私有属性的方法
        return self.__color

    def set_color(self, color):  # 定义外部代码修改类私有属性的方法
        self.__color = color


R = Rectangle(3, 4, "blue", id="001", owner="AAA")  # 创建类的实例，自动调用__init__()构造方法
print("width =", R.width, "id = ", R.id, "owner = ", R.owner)  # 访问实例的属性
R.printme()  # 访问实例的方法
# print("color = %s, Area = %d " % (R.__color, R.__getArea()))  # 报错，因为实例无法访问类的私有属性和私有方法

print("__color = ", R.get_color())  # 访问对象的内部状态
R.set_color('red')  # 设置对象的内部状态
print("__color = ", R.get_color())


class Person3(object):
    __count = 0  # 可以通过一个类方法获取类的私有属性

    @classmethod  # 通过标记一个@classmethod将how_many()方法绑定到Person3类
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person3.__count += 1


print(Person3.how_many())
p1 = Person3('Test')
print(Person3.how_many())  # 统计类实例的生成数目

# ### 使用类
# 使用类将有助于降低复杂性，减少bug，并且使代码更可维护；
# 类可以从零开始创建，也可以从Python的内置类或从其他定制类继承；
#
# ### 类与对象
# - 类(Class): 用来描述具有相同的属性和方法的对象的集合，定义了该集合中每个实例所共有的属性和方法。
# - 通过class关键字创建类；
# - 实例化的对象（Object）是类的实例（Instance）；
#
# ### 属性（Attribute）
# - 属性包括字段与方法；
# - 字段（Field）：对象或类的变量，分别被称为实例变量（Instance Variables）与类变量（Class Variables）；
# - 方法（Method）：方法也分实例方法和类方法；在class中定义的全部是实例方法，实例方法第一个参数self是实例本身;
# - 将属性名以双下划线开头可将属性定义为私有属性，表示其只能在类内部以self.的方式访问，类的实例（实例）无法访问；
# - 当实例属性和类属性重名时，实例属性优先级高；
#
# ### self
# - 简单的说，self参数是指类实例自身（也就是对象本身）的引用；
# - 在定义实例方法时，self参数必须存在并且只能作为第一个参数，self代表的是类的实例；
# - 即使实例方法不需要任何参数，self也必须存在，而独立的函数或方法则不需要；
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
# ### 类方法
# 在class中定义的全部是实例方法，实例方法第一个参数self是实例本身;
# 但可以通过标记一个@classmethod将一个方法绑定到类上，而非类的实例；
# 类方法的第一个参数将传入类本身，通常将参数名命名为cls；
# 类方法是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用；
#
# ### 访问限制
# - 属性名称前加上两个下划线__，就变成了一个私有（private）属性，只有内部可以访问，外部不能访问；
# - 但可以通过增加类似get_xxx和set_xxx的方法，间接地实现让外部代码访问和设置类的私有属性和私有方法；
# - 注意：以一个下划线开头的实例变量名，虽然外部是可以访问的，但视为私有变量，不要随意访问；
# - 注意：以双下划线开头并且以双下划线结尾，类似__xxx__的变量是特殊变量，可以直接访问；
