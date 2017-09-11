# -*- coding: utf-8 -*-

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
newZoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(newZoo))
print('All animals in new zoo are', newZoo)
print('Animals brought from old zoo are', newZoo[2])
print('Last animal brought from old zoo is', newZoo[2][2])
print('Number of animals in the new zoo is', len(newZoo) - 1 + len(newZoo[2]))

# ### 元组（Tuple）
# - 元组类似于字符串，但元组是不可变的，不能编辑或更改；
# - 使用括号()声明列表，在括号内部用逗号进行分隔项目；
# - 利用元组内数值不会改变的特性，可以用于保证某一语句或定义的函数可以安全地采用一组数值；
# - 通过索引（Indexing）运算符访问元组中的项目；
#
# ### 包含 0 或 1 个项目的元组
# - 空元组：由一对圆括号构成；例如，“myEmpty = ()”；
# - 包含一个项目的元组：唯一的项目必须以逗号结尾；例如，指定一个包含项目2的元组“singleton = (2, )” ；
#
# ### 元组常用方法
# - help(tuple)获取Tuple类的更多信息；
