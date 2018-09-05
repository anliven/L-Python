# -*- coding: utf-8 -*-


class Person1:  # 类名通常是大写开头的单词
    pass  # 使用pass语句标明一个空代码块（代码桩）


class Person2:
    def __init__(self, name):  # __init__方法在类的对象被实例化（Instantiated）时立即运行，进行初始化（Initialization）操作
        self.name = name

    def sayhi(self):  # 函数第一个参数是self表明此函数是类的方法
        print('Hello, my name is', self.name)

    def __del__(self):  # __del__方法在对象消逝时被调用，一般不做自定义
        print('Over！')


p = Person1()
print(p)  # 打印结果，类的__main__产生了一个实例，以及这个实例对象的内存地址；

p2 = Person2('Anliven')
print(p2.name)
p2.sayhi()
Person2('Anliven').sayhi()  # 等同于上两行
print(p2.sayhi)  # 注意：p.sayhi是一个绑定到实例的函数对象，不是方法


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
# - 字段（Field）：分为实例变量（Instance Variables）与类变量（Class Variables）；
# - 方法（Method）：在class中定义的全部是实例方法，实例方法第一个参数self是实例本身;
# - 将属性名以双下划线开头可将属性定义为私有属性，表示其只能在类内部以self.的方式访问，类的实例无法访问；
# - 当实例属性和类属性重名时，实例属性优先级高；
#
# ### self
# - 简单的说，self参数是指类实例自身（也就是对象本身）的引用；
# - 在定义实例方法时，self参数必须存在并且只能作为第一个参数，self代表的是类的实例；
# - 即使实例方法不需要任何参数，self也必须存在，而独立的函数或方法则不需要；
# - 对实例调用方法时，方法的参数self将自动关联到实例（称为关联的方法）；
#
# ### 构造函数（constructor）
# 类实例创建后，自动调用类的构造方法__init__()来初始化实例；
# 构造方法__init__()的第一个参数为self，在创建类的实例时，会自动调用该构造方法；
# 必须传入与__init__方法匹配的参数，但self不需要传(Python解释器会自动处理)
#
# ### 析构函数（destructor）
# 析构函数__del__()在对象被销毁（作为垃圾被收集）前被调用；
# 不建议析构函数，因为无法获知准确的调用时间；
#
# ### 举例说明
# - 创建了一个类MyClass，实例化对象为MyObject，然后调用对象的方法MyObject.method(a,b)；
# - 在此过程中，Python自动将对象的方法转化为Myclass.method(MyObject,a,b)，self参数被赋值为MyObject；
#
# ### pass语句
# 标明一个空代码块（代码桩）；
# 使用pass语句可以为后续要实现的代码“先占个位置”，避免过度沉陷在细枝末节中；
