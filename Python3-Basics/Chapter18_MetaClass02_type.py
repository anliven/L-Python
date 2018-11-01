# coding=utf-8


class Foo():
    pass


Foo2 = type('Foo2', (object,), {})  # 使用type()创建了一个名为Foo2的类，然后赋给变量Foo2

print(Foo)
print(Foo2)


class Foo3(object):
    foo3 = True

    def greet3(self):
        print('hello world - Foo3', self.foo3)


def greet4(self):
    print('hello world - Foo4', self.foo4)


Foo4 = type('Foo4', (object,), {'foo4': True, 'greet4': greet4})  # 具有属性和方法

f3 = Foo3()
f4 = Foo4()
print(Foo3, f3.foo3)
print(Foo4, f4.foo4)
f3.greet3()
f4.greet4()


class Foo5(Foo):
    foo5 = True


Foo6 = type('Foo6', (Foo,), dict(foo6=True))  # 继承

f5 = Foo5()
f6 = Foo6()
print(Foo5, f5.foo5)
print(Foo6, f6.foo6)

# ### 内置函数type()
# https://docs.python.org/3/library/functions.html#type；
# type()可以返回对象的类型，还可以用来在运行时、动态地创建类（对象）;
# 创建类或对象的方式（接受一个类的描述作为参数，然后返回一个类）： type(类名, (父类的元组,), {属性和方法})；
#   - 第1个参数是字符串，表示类名，将成为该类的__name__属性；
#   - 第2个参数是元组，表示所有的父类（可以为空，如果只有一个父类需要使用tuple的单元素写法），将成为该类的__bases__属性；
#   - 第3个参数是字典，包含属性和方法的字典（名称和值），如果是空字典则表示没有定义属性和方法，将成为该类的__dict__属性；
#
# type()是创建类对象的类，实际上也就是一个Python的内建元类，用来创建所有类的元类；
