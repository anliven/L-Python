#! python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s.' % self.name)


print(Student('AAA'))
s = Student('BBB')
s()
print(s)

print(callable(s), callable(max))
print(callable([1, 2, 3]), callable(None), callable('str'))

# ### 定制方法
# Python的class有很多可定制的方法(特殊用途的函数)，可以非常方便地生成特定的类;
# Python的官方文档: https://docs.python.org/3/reference/datamodel.html#special-method-names;
#
# __str__(): 返回用户看到的字符串
# __repr__(): 返回程序开发者看到的字符串，为调试服务的
# __call__()：直接对实例进行调用
# ......
#
# Callable对象
# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象;
# 通过callable()函数，可以判断一个对象是否是“可调用”对象;
