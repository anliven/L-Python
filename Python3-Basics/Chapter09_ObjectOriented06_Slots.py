#! python3
# -*- coding: utf-8 -*-
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = "SSS"  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)  # 动态给实例绑定一个方法
s.set_age(29)  # 调用实例方法
print(s.age)


def set_score(self, score):
    self.score = score


Student.set_score = set_score  # 动态给class绑定方法（同时，也就给所有实例都绑定了方法）
s.set_score(100)
print(s.score)


class Teacher(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


t = Teacher()
# t.score = 99  # 试图绑定不允许的属性，将提示AttributeError错误


class Master(Teacher):
    __slots__ = ('skill')  # 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


m = Master()
m.name = "MMM"
m.age = "111"
m.skill = "VVV"
print(m.name, m.age, m.skill)

# ### 动态绑定属性
# 正常情况下，创建一个class的实例后，可以给该实例绑定任何属性和方法，这就是动态语言的灵活性；
# 实例属性属于各个实例所有，互不干扰；也就是说，给一个实例绑定的属性和方法，对另一个实例是不起作用的；
# 动态绑定允许在程序运行的过程中动态给class加上功能;
#
# ### types.MethodType()
# 利用types.MethodType()可以把一个函数变为一个方法，可以动态地添加到实例；
# 虽然可以给一个实例动态添加方法，但这种情况并不常见，因为直接在class中定义更直观；
#
# ### 限制实例的属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 试图绑定未在__slots__变量中的属性，将得到AttributeError的错误;
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用；
# 在子类中也可以定义__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__；
