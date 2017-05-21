# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
### 内置函数（built-in functions）

# python的内置函数可以直接调用,无需import。
# 查看所有内置函数名可以在python命令行方式中如下输入：
# >>> dir(__builtins__)

# ----------------------------------------------------------------------------------------------------------------------
### 特殊的内置函数

### __init__
# 当一个类实例被创建时， __init__() 方法会自动执行,执行一些该对象的必要的初始化工作。注意，这个名称的开始和结尾都是双下划线。
# 在创建一个类的新实例的时候，把参数包括在圆括号内跟在类名后面，从而传递给__init__方法。
# 通过创建自己的 __init__() 方法， 可以覆盖默认的 __init__()方法（默认的方法什么也不做）。


### __name__和__main__
# 用于判断当前模块是不是程序入口，如果当前程序正在使用，__name__的值为__main__。
# 在编写程序时，通常需要给每个模块添加条件语句，用于单独测试该模块的功能。

# if __name__ == '__main__':
# 运行当前脚本，就会执行if __name__=="__main__"下的函数，如果模块被其他程序import的，那么就不会执行。
# 主要是测试用，测试这个模块有没有实现预期的功能。


### __doc__
# 模块本身是一个对象，而每个对象都会有一个__doc__属性。该属性用于描述该对象的作用。


### __dict__与dir()的区别

# 一个普通对象使用一个dict来保存它自己的属性，可以动态地向其中添加或删除属性。
# 许多内建类型都没有__dict__属性，例如list string等没有__dict__属性
# Python的实例以及对应的类都拥有自己的__dict__。

# 对一个类设置属性时，它的实例也会受到影响
# 直接对一个实例设置属性时，该实例的__dict__中添加了该属性，但它所属的类的__dict__却不受影响。
# 一个实例的__dict__属性仅仅是那个实例的局部属性集合，不包含该实例所有有效属性。

# dir()函数会自动寻找一个对象的所有属性，包括搜索__dict__中列出的属性。
# dir()是使用对象的继承关系来反馈一个对象的完整的有效属性。
# 作用在实例上时，显示实例变量，还有在实例所在的类及所有它的基类中定义的方法和类属性
# 作用在类上时，则显示类以及它的所有基类的__dict__中的内容。
# 作用在模块上时，则显示模块的__dict__的内容。
# 不带参数时，则显示调用者的局部变量。

# dir() 返回的仅是对象的属性的一个名字类表。
# __dict__ 返回的是一个字典，它的键（key）是属性名，键值（value）是相应的属性对象的数据值。


# ----------------------------------------------------------------------------------------------------------------------
### 举例说明：


class man:
    """this is a test"""  # __doc__属性的内容

    def __init__(self, name, age):  # 当一个类实例被创建时， __init__() 方法会自动执行,执行一些该对象的必要的初始化工作。
        self.name = name
        self.age = age

    def Say(self, what):
        print "hello, %s" % what

X = man("test", 30)  # 实例化一个对象X。在创建一个类的新实例的时候，把参数包括在圆括号内跟在类名后面，从而传递给__init__方法。

if __name__ == '__main__':  # 运行当前脚本，就会执行if __name__=="__main__"下的函数，如果模块被其他程序import的，那么就不会执行。

    print X.__dict__  # 打印实例对象X的__dict__属性
    print dir(X)  # 打印实例对象X的所有有效属性。

    print man.__dict__
    print dir(man)

    print dir()


# ----------------------------------------------------------------------------------------------------------------------
### getattr()函数
# 可以获取对象引用，返回对象的任意属性或者方法。
# 通常， getattr(object,"attribute") 相当于 object.attribute。
# 如果 object 是一个模块，那么attribute 可以是定义在模块中的函数，类，或全局变量。
#
# getattr(...)
#     getattr(object, name[, default]) -> value
#
#     Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
#     When a default argument is given, it is returned when the attribute doesn't
#     exist; without it, an exception is raised in that case.


### setattr()函数
# 可以通过该方法，给对象添加或者修改指定的属性
# 接受3个参数：setattr(对象，属性，属性的值)
#
# setattr(...)
#     setattr(object, name, value)
#
#     Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
#     ``x.y = v''.


### delattr()函数
# 通过该方法，删除指定的对象属性
# 接受2个参数：delattr(对象，属性)
#
# delattr(...)
#     delattr(object, name)
#
#     Delete a named attribute on an object; delattr(x, 'y') is equivalent to
#     ``del x.y''.


### hasattr()函数
# 通过该方法，确定一个对象是否具有某个属性,并返回一个布尔值，属性存在返回True，否则返回False。
# 接受2个参数：hasattr(对象，属性)
#
# hasattr(...)
#     hasattr(object, name) -> bool
#
#     Return whether the object has an attribute with the given name.
#     (This is done by calling getattr(object, name) and catching exceptions.)


# ----------------------------------------------------------------------------------------------------------------------
### 举例 ： getattr(),setattr(),delattr(),hasattr()的作用


# class man:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def Say(self, what):
#         print "hello, %s" % what
#
# X = man("test", 30)  # 实例化一个对象X
#
# print getattr(X, 'name', 'not find')  # 如果X 对象中有属性name则打印self.name的值，否则打印”not find“
# print getattr(X, 'weight', 'not find')   # 如果X 对象中有属性weight则打印self.age的值，否则打印”not find“
# print getattr(man, 'Say', 'not find')  # 如果类man中有方法Say，打印信息，否则打印"not find"
# print getattr(man, 'Say', 'not find')(X, "python")  # 如果类man中有方法Say，执行X.Say("python")，否则打印"not find"
# print getattr(man, 'Say_test', 'not find')  # 如果类man中有方法Say_test，打印信息，否则打印"not find"
#
# print dir(X)
# setattr(X, 'height', '6feet')  # 为对象X添加属性height和值，相当于执行 X.height = '6feet'
# print dir(X)
#
# print dir(man)
# setattr(man, 'action', 'run')  # 为对象man类添加属性action和值
# print dir(man)
#
# print dir(X)
# delattr(X, 'age')  # 删除对象X的属性age，相当于执行 del X.age
# print dir(X)
#
# print hasattr(X, 'age')  # 确定对象X是否具有age属性,存在则打印True，否则打印False。
# print dir(X)


# # 使用getattr可以轻松实现工厂模式。
# # 举例：一个模块支持html、text、xml等格式的打印，根据传入的format参数的不同，调用不同的函数实现几种格式的输出
#
# from sys import stdout
#
#
# def output(data, fileFormat="text"):
#     output_function = getattr(stdout, "output_%s" % fileFormat)
#     return output_function(data)


# ----------------------------------------------------------------------------------------------------------------------

### 举例：利用getattr(),setattr(),delattr(),hasattr()对list操作

# >>> li = [1,2,3,4,5,'a','b','c','d','e']  # 定义了一个列表li
# >>> li
# [1,2,3,4,5,'a','b','c','d','e']

# >>> li.pop  # 得到对象pop方法的一个引用，返回了地址。
# <built-in method pop of list object at 0x00000000020C1A88>
# >>> getattr(li, "pop")  # 得到了同一函数的同一引用。对象是列表li，获得的属性是 pop 方法
# <built-in method pop of list object at 0x00000000020C1A88>
# >>> li  # 内容无变化，说明以上只是得到对象pop方法的一个引用，而不是调用pop方法。
# [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

# >>> li.pop() # 针对列表对象li调用pop方法，这里去除了列表末尾的一个元素，并返回了该元素的值。
# 'e'
# >>> getattr(li, "pop")() # 针对列表对象li调用pop方法，这里去除了列表末尾的一个元素，并返回了该元素的值。
# 'd'
# >>> li.pop(0) # 去除当前列表第一个元素，并返回该元素的值
# 1
# >>> getattr(li, "pop")(0) # 去除当前列表第一个元素，并返回该元素的值
# 2
# >>> li  # 此时列表li的内容
# [3, 4, 5, 'a', 'b', 'c']

# >>> getattr(li, "shuffle")  # 对于不存在的方法，python会给出错误提示。
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'shuffle'
# >>> getattr(li, "shuffle","not find") # 如果li对象中有属性shuffle则显示地址，否则打印”not find“
# 'not find'

# >>> getattr(li, "append","not find")("ZZ")  # 在列表末尾加上字符串ZZ
# >>> getattr(li, "insert","not find")(3, 99)  # 在列表的第三个元素位置插入整数99
# >>> li  # 此时列表li的内容
# [3, 4, 5, 99, 'a', 'b', 'c', 'ZZ']


# >>> hasattr(li, "pop")   # 检查列表对象li是否有pop方法
# True # 返回布尔值True表示列表对象li是存在pop方法


# ----------------------------------------------------------------------------------------------------------------------