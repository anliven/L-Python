# coding=utf-8


class SayMetaClass(type):

    def __new__(mcs, name, bases, attrs):  # 自定义__new__()方法
        attrs['say_' + name] = lambda self, value, saying=name: print(saying + ',' + value + '!')
        x = super().__new__(mcs, name, bases, attrs)
        x.value = 100  # 自定义属性
        return x  # 返回新创建的类


class Hello(object, metaclass=SayMetaClass):
    pass


class Nihao(object, metaclass=SayMetaClass):
    pass


h = Hello()
h.say_Hello('world')
print(h.value)
n = Nihao()
n.say_Nihao('中国')
print(n.value)

# ### 元类（metaclass）
# 元类（metaclass）是用来创建类（对象）的可调用对象；
# 简而言之，类是实例对象的模板，元类是类的模板；也就是说，类创建实例，元类创建类；
# 一般情况下，使用类作为元类，通过使用元类，可以控制类的创建行为，自动地改变类；
# 元类会隐式地继承到子类，即使没有显示地在子类使用“__metaclass__”；
#
# ### 特殊方法“__new__”
# 元类的操作在特殊方法“__new__”中完成；
# “__new__”用来创建对象并返回创建后的对象，在“__init__”之前被调用，参数解释如下：
# - mcs：将要创建的类
# - name：类的名字
# - bases：类的父类集合
# - attrs：类的属性和方法，是一个字典
#
# ### “__metaclass__”的顺序
# - Python会按照“当前类-->父类-->更上一级父类-->...”的顺序，在类中寻找“__metaclass__”；
# - 如果在任何父类中都找不到“__metaclass__”，就会到模块层次中寻找；
# - 如果在模块层次中还找不到，就会用type()来创建这个类;
# 简而言之:
# - 创建类时，解释器会调用元类来生成;
# - 定义一个继承自object的普通类(没有定义“__metaclass__”)意味着调用type()来创建;
