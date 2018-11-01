# coding=utf-8


class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):
        _attrs = (('my_' + name, value) for name, value in attrs.items())  # 给所有属性和方法前面加上前缀“my_”
        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加一个echo方法
        return super().__new__(cls, name, bases, _attrs)  # 返回创建后的类


class Foo(metaclass=PrefixMetaclass):  # 指定元类
    name = 'foo'

    def test(self):
        print('this is a test!')


class Bar(Foo):  # 继承（元类会隐式地继承到子类，即使没有显示地在子类使用“__metaclass__”）
    prop = 'bar'


f = Foo()
print(f.my_name)
f.my_test()
print(f.echo("hello"))

b = Bar()
print(b.my_prop)
print(b.my_name)
b.my_test()
print(b.echo("hi"))

# ### 自定义Metaclass的作用
# 1-可以拦截类的创建；
# 2-可以读取类的信息，并做修改；
# 3-可以返回新的类；
