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

# ### “__metaclass__”的顺序
# - Python会按照“当前类-->父类-->更上一级父类-->...”的顺序，在类中寻找“__metaclass__”；
# - 如果在任何父类中都找不到“__metaclass__”，就会到模块层次中寻找；
# - 如果在模块层次中还找不到，就会用缺省的Metaclass（即type()）来创建这个类;
# 简而言之:
#   - 创建类时，解释器会调用元类来生成;
#   - 定义一个继承自object的普通类(没有定义“__metaclass__”)意味着调用type()来创建;
