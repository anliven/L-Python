#! python3
# -*- coding: utf-8 -*-


def test(x):
    print("Executing func_test: %s" % x)


class TestClass(object):
    def instance_test(self, x):  # 默认约定self对类的实例绑定，不建议更改
        print("Executing instance_test: %s,%s" % (self, x))

    @classmethod
    def class_test(cls, x):  # 默认约定cls对类绑定，不建议更改
        print("Executing class_test: %s,%s" % (cls, x))

    @staticmethod
    def static_test(x):  # 静态方法和普通方法一样，不需要进行绑定,
        print("Executing static_test: %s" % x)


test("func")  # 直接调用函数

a = TestClass()  # 初始化实例对象
a.instance_test("instance")  # 类的实例调用类实例方法，实例方法必须通过实例来调用
a.class_test("class")  # 类的实例调用类方法
a.static_test("static")  # 类的实例调用类的静态方法

TestClass.class_test("# class")  # 直接调用类方法
TestClass.static_test("# static")  # 直接调用类的静态方法

# ### 类方法
# 在class中第一个参数为self的方法全部是实例方法，self绑定实例本身;
# 可以通过标记一个@classmethod将一个方法绑定到类上，而非类的实例；
# 类方法的第一个参数将传入类本身，通常将参数名命名为cls；
# 类方法是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用；
#
# ### 静态方法
# 用@staticmethod装饰，可以被实例对象访问或直接访问；
# 静态方法和普通方法一样，不需要进行绑定；
