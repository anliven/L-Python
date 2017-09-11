# -*- coding: utf-8 -*-

name = 'Anliven'
if name.startswith('An'):  # startwith方法用于查找字符串是否以给定的字符串内容开头
    print('The string starts with "An"')
if 'liven' in name:  # in运算符用以检查给定的字符串是否是查询的字符串中的一部分
    print('It contains the string "liven"')
if name.find('li') != -1:  # find方法用于定位字符串中给定的子字符串的位置，如果找不到则返回-1
    print('It contains the string "li"')

delimiter = '_*_'
testList = ['Anliven', 'Love', 'Angelina']
print(delimiter.join(testList))  # 联结序列中的项目并生成字符串

# ### 字符串（Strings）
# - 字符串是一种对象，具有自己的方法；在程序中使用的所有字符串都是str类下的对象；
#
# ### 字符串常用方法
# - help(str)获取String类的更多信息；
#
# ### 数据结构（ Data Structures）
# - 四种内置的数据结构：列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set），都是使用对象与类的实例；
