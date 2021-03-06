# -*- coding: utf-8 -*-

tup = ()  # 创建空元组
tup2 = (123,)  # 只包含一个值的元组，必须使用逗号
tup3 = tuple("abc")  # 字符串转换为元组
tup4 = tuple([111, 222, 333])  # 列表转换为元组
print(tup, tup2, tup3, tup4)

t = ('aaa', 'bbb', 'ccc')
x, y, z = t  # 元组的拆分
print(x, y, z, len(t))
print(t[0])  # 打印索引为0的元素（注意：返回元素而不是元组，所以返回值没有中括号）
print(t[1:3])  # 打印索引为1到2的元素，作为一个元组返回
for single_item in t:  # 遍历元组中的所有项目
    print('single_item:', single_item)

nt = '777', '888', '999', t
print(len(nt), nt)  # 注意打印结果
print(nt[2], nt[3][2])

# ### 元组（Tuple）
# - 使用括号()声明列表，在括号内部用逗号进行分隔项目，定义格式：tuple = (obj1,obj2,obj3,…)；
# - 元组的元素可以不相同，可以包含数字、字符串、元组等；
# - 特别注意：元组是不可变的，一旦初始化就不能修改，不允许编辑或更改元组的元素；
#
# ### 元组常用方法
# - 通过索引（Indexing）运算符访问元组中的元素；
# - 基本操作等同于字符串、列表（序列）；
# - 元组截取的语法格式：变量[头下标:尾下标]
# - help(tuple)获取Tuple类的更多信息；
#
# ### tuple()
# https://docs.python.org/3/library/functions.html#func-tuple
# 内置函数tuple()用来将一个可迭代对象转化为元组；
#
# ### 尽量用tuple
# - 利用元组内数值不会改变的特性，可以用于保证某一语句或定义的函数可以安全地采用一组数值；
# - 因为tuple不可变，所以代码更安全，如果可能，尽量用tuple代替list；
#
# ### 包含 0 或 1 个元素的元组
# - 空元组：由一对圆括号构成；例如，“myEmpty = ()”；
# - 包含一个元素的元组：唯一的元素必须以逗号结尾来消除歧义；例如，指定一个包含元素2的元组“singleton = (2, )” ；
#
# ### list与tuple的区别
# list和tuple都是Python内置的有序集合，一个可变，一个不可变；
