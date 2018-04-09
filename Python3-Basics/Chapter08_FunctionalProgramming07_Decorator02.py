#! python3
# -*- coding: utf-8 -*-


class Persion:
    name = "aaa"
    age = 29

    def __init__(self, n, a):
        self.name = n
        self.age = a

    @property
    def hi(self):  # 用@property装饰器将方法“装饰”成属性
        print("Hello!", self.name)
        return self.name

    @classmethod
    def say(self):  # 用@classmethod装饰，是类的方法
        print("My name is %s. I am %d years old." % (self.name, self.age))

    def say2(self):  # 不使用@classmethod装饰，是实例对象的方法
        print("My name is %s. I am %d years old." % (self.name, self.age))

    @staticmethod
    def bye():  # 用@staticmethod装饰，可以被实例对象访问或直接访问
        print("Goodbye!")

    # def bye2():  # 不使用@staticmethod装饰，则此方法无法被实例对象调用
    #     print("Goodbye, Two.")


p = Persion("AAA", 35)

print(p.hi)  # 调用属性

Persion.say()
p.say()  # 注意结果
# Persion.say2()  # 不能通过类去调用实例对象的方法
p.say2()  # 注意结果

Persion.bye()
p.bye()
Persion.bye2()
# p.bye2()  # 调用报错

# ### 内置装饰器
# @staticmethod  类静态方法：没有self参数，并且可以在类不进行实例化的情况下调用；
# @classmethod  类方法：接收的第一个参数是cls（当前类的具体类型），而不是self（类实例的指针）；
# @property  属性方法：将一个类方法转变成一个类的只读属性；
#
# ### 类方法
# 在class中定义的全部是实例方法，实例方法第一个参数self是实例本身;
# 但可以通过标记一个@classmethod将一个方法绑定到类上，而非类的实例；
# 类方法的第一个参数将传入类本身，通常将参数名命名为cls；
# 类方法是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用；
