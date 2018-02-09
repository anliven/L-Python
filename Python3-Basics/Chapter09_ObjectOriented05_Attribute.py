#! python3
# -*- coding: utf-8 -*-

print(type(123))  # 使用type()函数判断对象类型
print(type(None))
print(type(abs))
print(type('abc') == str)  # 比较两个变量的type类型是否相同

print(isinstance('a', str))
print(isinstance(b'a', bytes))
print(isinstance('abc', type(123)))

print(dir('abc'))


class Sample(object):
    dsc = "hi"

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


test = Sample()
print(hasattr(test, 'x'))  # hasattr()是否具有属性
print(test.x)
print(hasattr(test, 'y'))
print(getattr(test, 'y', 404))  # getattr()获取属性，如果不存在，返回默认值404
setattr(test, 'y', 999)  # setattr()设置属性
print(getattr(test, 'y'))  # getattr()获取属性
print(test.y)

print(test.dsc, Sample.dsc)
test.dsc = "hello"
print(test.dsc, Sample.dsc)  # 实例属性优先级比类属性高
del test.dsc
print(test.dsc, Sample.dsc)

# ### 获取对象信息
# - type()函数: 判断对象类型
# - isinstance()函数: 判断一个对象是否是该类型本身，或者位于该类型的父继承链上（多用于判断class的类型）
# - 能用type()判断的基本类型也可以用isinstance()判断，优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”；
# - dir()函数： 获得一个对象的所有属性和方法；
#
# ### 操作对象状态
# 配合getattr()、setattr()以及hasattr()，可以直接操作一个对象的状态
#
# ### 实例属性和类属性
# - 类属性属于类所有，所有实例共享一个属性；
# - 实例属性属于各个实例所有，互不干扰；
# - 相同名称的实例属性将屏蔽掉类属性，但删除实例属性后，再使用相同的名称，访问到的将是类属性;
# 注意： 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误；
