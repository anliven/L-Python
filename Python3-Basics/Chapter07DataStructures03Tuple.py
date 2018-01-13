#! python3
# -*- coding: utf-8 -*-

tup = ()  # 创建空元组
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
print(zoo[0])  # 打印索引为0的元素（注意：返回元素而不是元组，所以返回值没有中括号）
print(zoo[1:3])  # 打印索引为1到2的元素，作为一个元组返回

newZoo = 'monkey', 'camel', zoo
print('All animals in new zoo are', newZoo)  # 注意打印结果
print('Number of cages in the new zoo is', len(newZoo))
print('Animals brought from old zoo are', newZoo[2])
print('Last animal brought from old zoo is', newZoo[2][2])
print('Number of animals in the new zoo is', len(newZoo) - 1 + len(newZoo[2]))


# ### 元组（Tuple）
# - 使用括号()声明列表，在括号内部用逗号进行分隔项目，定义格式：tuple = (obj1,obj2,obj3,…)；
# - 元组的元素可以不相同，可以包含数字、字符串、元组等；
# - 元组是不可变的，不允许编辑或更改元组的元素；
# - 利用元组内数值不会改变的特性，可以用于保证某一语句或定义的函数可以安全地采用一组数值；
# - 通过索引（Indexing）运算符访问元组中的项目；
# - 元组截取的语法格式：变量[头下标:尾下标]
#
# ### 包含 0 或 1 个项目的元组
# - 空元组：由一对圆括号构成；例如，“myEmpty = ()”；
# - 包含一个项目的元组：唯一的项目必须以逗号结尾；例如，指定一个包含项目2的元组“singleton = (2, )” ；
#
# ### 元组常用方法
# - help(tuple)获取Tuple类的更多信息；
