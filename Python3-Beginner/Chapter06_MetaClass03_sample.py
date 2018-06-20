# coding=utf-8


class ListMetaclass(type):  # 定义一个元类，类名默认以Metaclass结尾；元类是由“type”衍生而出，所以必须从type类型派生

    def __new__(mcs, name, bases, attrs):  # 自定义__new__()方法
        attrs['add'] = lambda self, value: self.append(value)
        return super().__new__(mcs, name, bases, attrs)  # 返回新创建的类
        # return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):  # 第一个参数是父类，第二个参数是metaclass指示使用元类来定制类
    pass


L = MyList()  # 这里Python解释器在创建MyList时，实际通过ListMetaclass.__new__()来创建
L.add(123)  # 普通的List类型没有add()方法
L.add(456)
L.add(789)
print(L)

# ### 元类（metaclass）
# 元类（metaclass）是用来动态创建类（对象）的可调用对象，先定义metaclass，然后根据metaclass创建类，最后根据类创建实例；
# 简而言之，元类是类的模板，类是实例对象的模板；也就是说，元类创建类，类创建实例；
# 一般情况下，使用类作为元类，通过使用元类，可以控制类的创建行为，自动地改变类；
# 元类会隐式地继承到子类，即使没有显示地在子类使用“__metaclass__”；
#
# ### 特殊方法“__new__”
# 元类的操作在特殊方法“__new__”中完成；
# “__new__”用来创建对象并返回创建后的对象，在“__init__”之前被调用，参数解释如下：
# - cls：将要创建的类；
# - name：类的名字；
# - bases：类的父类集合；
# - attrs：类的属性和方法，是一个字典；
#
# ### 动态修改的意义
# 一般情况下不会使用动态修改，只适用于某些特殊的场景，能够极大地精简代码，例如编写ORM框架；
