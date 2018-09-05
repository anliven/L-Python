# -*- coding: utf-8 -*-


class Rectangle:
    # width = 0  # 定义类的属性
    # height = 0

    __color = ""  # 定义类的私有属性

    def __init__(self, color, width=0, height=0, **kwargs):  # 定义可变长参数的构造函数
        self.__color = color
        self.width = width
        self.height = height
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


R = Rectangle("blue", 3, 4, id="001", owner="AAA")  # 创建类的实例，自动调用__init__()构造方法
print("width =", R.width, "id = ", R.id, "owner = ", R.owner)  # 访问实例的属性
R.printme()  # 访问实例的方法
# print("color = %s, Area = %d " % (R.__color, R.__getArea()))  # 报错，因为实例无法访问类的私有属性和私有方法

print("__color = ", R.get_color())  # 访问对象的内部状态
R.set_color('red')  # 设置对象的内部状态
print("__color = ", R.get_color())

# ### 访问限制
# - 属性名称前加上两个下划线__，就变成了一个私有（private）属性，只有内部可以访问，外部不能访问；
# - 但可以通过增加类似get_xxx和set_xxx的方法，间接地实现让外部代码访问和设置类的私有属性和私有方法；
# - 注意：以一个下划线开头的实例变量名，虽然外部是可以访问的，但视为私有变量，不要随意访问；
# - 注意：以双下划线开头并且以双下划线结尾，类似__xxx__的变量是特殊变量，可以直接访问；
