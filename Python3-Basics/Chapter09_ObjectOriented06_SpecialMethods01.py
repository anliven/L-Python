# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __call__(self, teacher):
        print('My name is %s.' % self.name)
        print('My teacher is %s.' % teacher)


s = Student('AAA')
print(s)
s("BBB")  # 直接调用类实例

print(callable(s), callable(max))
print(callable([1, 2, 3]), callable(None), callable('str'))


class Fib(object):  # 定义一个生成斐波那契数列的类
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)


f = Fib(10)
print(len(f), f)  # 用len()函数返回类实例的“长度”，类必须提供__len__()特殊方法，否则无法返回元素的个数


class Test(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q


t = Test(2, 3)
print(int(t))  # 在类中实现特殊方法__int__()，然后利用int()函数将类实例转为int
print(float(t))

# ### 特殊方法
# 以双下划线开头双下划线结尾的函数，是Python的特殊方法（魔术方法）；
# 可以利用这些特殊用途的函数（特殊方法/魔术方法）方便地生成特定的类;
# - 特殊方法定义在class中；
# - 不需要直接调用（几乎所有的特殊方法都是隐式调用）；
# - 某些函数或操作符会调用对应的特殊方法；
# Python的官方文档: https://docs.python.org/3/reference/datamodel.html#special-method-names
#
# ### 实现特殊方法
# - 只需要编写实际用到的特殊方法；
# - 有关联性的特殊方法必须实现；
#
# ### 一些特殊方法
# __str__(): 用于显示给用户：返回用户看到的字符串，如果没有提供 __str__，str()缺省使用repr()的结果；
# __repr__(): 用于显示给开发人员：返回程序开发者看到的字符串，为调试服务的
# __len__()：返回类实例的“长度”，对序列来说为元素个数，对映射来说是键值对的个数；
# __call__()：直接对实例进行调用，实际上是将一个类实例变成一个可调用对象
# ......
#
# ### Callable对象
# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象;
# 通过callable()函数，可以判断一个对象是否是“可调用”对象;
