# -*- coding: utf-8 -*-


class Person1:
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
# Person2('Anliven').sayhi()  # 等同于上两行

# ### 类与对象
# - 通过class关键字创建类；
# - 对象（Object）是类的实例（Instance）；
# - 字段与方法通称类的属性（Attribute）；
# - 字段（Field）：对象或类的变量，分别被称为实例变量（Instance Variables）与类变量（Class Variables）；
# - 方法（Method）：在类中实现某些功能的函数，可以被对象使用；
#
# ### self
# - 简单的说，self参数是指类实例自身（也就是对象本身）的引用；
# - 在定义类方法(类中的函数)时，self参数必须存在并且只能作为第一个参数；
# - 即使类的方法不需要任何参数，self也必须存在类的方法中，而独立的函数或方法则不需要；
#
# ### 举例说明
# - 创建了一个类MyClass，实例化对象为MyObject，然后调用对象的方法MyObject.method(a,b)；
# - 在此过程中，Python自动将对象的方法转化为Myclass.method(MyObject,a,b)，self参数被赋值为MyObject；
