#! python3
# -*- coding: utf-8 -*-

a = 2  # 整型变量
b = 1.5  # 浮点型变量
c = True  # 布尔型变量
d = 3.14j  # 复数型变量
e = True + False  # True代表1，False代表0
print(a, b, c, d, e)

string_sample = "HelloPython!"
print(string_sample[0:2])  # 从下标0到下标2，包括0不包括2
print(string_sample[0:-1])  # 从下标0到倒数第1个,不包括倒数第1个
print(string_sample[5:])  # 从下标5到最后
print(string_sample[:-7])  # 从开始到倒数第7个,,不包括倒数第7个
print(string_sample[0])  # 打印下标0的值
print(string_sample * 2)  # 连续输出两次
print(string_sample + "HelloWorld!")  # 连接字符串
print('Hello' in string_sample)  # in运算符用以检查给定的字符串是否是查询的字符串中的一部分
print('Java' in string_sample)
print('Java' not in string_sample)  # 判断'Java'是否不是str的子串

print('\nHello')  # 转义字符\n可以换行
print(r'\nHello')  # 字符串前加上r或R可以使字符串原样输出，防止被转义

name = 'Anliven'
print("The length of this string: %d" % len(name))  # len(string)方法返回字符串长度
print("name.count('n'): %d" % name.count("n", 0, len(name)))  # 返回str在 string 里面出现的次数
if name.startswith('An'):  # startswith()方法用于查找字符串是否以给定的字符串内容开头
    print('The string starts with "An"')
if 'liven' in name:  # in运算符用以检查给定的字符串是否是查询的字符串中的一部分
    print('It contains the string "liven"')
if name.find('li') != -1:  # find(str, beg=0 end=len(string))方法用于返回子字符串开始的索引值，如果找不到则返回-1
    print('It contains the string "li"')

delimiter = '_*_'
testList = ['Anliven', 'Love', 'Angelina']
print(delimiter.join(testList))  # 联结序列中的项目并生成字符串

# ### Number：数字
# Number包括整型、浮点型、布尔型和复数型。Number可以进行常见的数值运算，运算时布尔型True为1，False为0；
#
# ### String：字符串
# - 字符串是一种对象，具有自己的方法；在程序中使用的所有字符串都是str类下的对象；
# - 字符串使用单引号(”)或双引号(“”)括起来，同时使用反斜杠(\)转义特殊字符；
# - 字符串截取的语法格式：变量[头下标:尾下标]；
#
# ### 字符串输出格式化
# 字符串有多种输出方式，最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中；
# 字符串前加上r或R可以使字符串原样输出，防止被转义;
#
# ### 字符串常用方法
# - help(str)获取String类的更多信息；
#
# ### 数据结构（ Data Structures）
# - 四种内置的数据结构：列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set），都是使用对象与类的实例；
