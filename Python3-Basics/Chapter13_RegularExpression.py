#! python3
# -*- coding: utf-8 -*-
import re

test = '028-12345678'
if re.match(r'^(\d{3})-(\d{3,8})$', test):
    print('The match is successful.')
else:
    print('The match is failed.')

m = re.match(r'^(\d{3})-(\d{3,8})$', '028-12345678')
print(m.group(0), m.group(1), m.group(2))  # group(0)永远是原始字符串，group(1)、group(2)……表示第1、2……个子串

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 预编译正则表达式，提高效率
print(re_telephone.match('028-12345678').groups())
print(re_telephone.match('028-10000').groups())

print(re.match('www', 'www.bing.com'))
print(re.match('com', 'www.bing.com'))

print(re.search('www', 'www.bing.com'))
print(re.search('com', 'www.bing.com'))
print(re.search('www', 'www.bing.com').span(), re.search('com', 'www.bing.com').span())

print(re.split(r'[\s\,]+', 'aaa,bbb, ccc'))

print(re.sub(r'#.*$', "", "123-456-789 # this is a phone-number."))  # 删除注释
print(re.sub(r'\D', "", "123-456-789 # this is a phone-number."))  # 移除非数字的内容
print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', '2018-12-31'))  # 改变日期格式

string = "aaaaa bbbbb ccccc ddddd eeeee fffff"
print(re.findall("\w+\s+\w+", string))
print(re.findall("(\w+)\s+\w+", string))  # 注意括号的使用
print(re.findall("((\w+)\s+\w+)", string))

# ### re模块
# re模块包含所有正则表达式的功能，用编译后的正则表达式去匹配字符串，如果正则表达式的字符串本身不合法，则会报错；
# 特别注意Python的字符串本身也用\转义；
# 强烈建议使用Python的r前缀，就不用考虑转义的问题；
#
# re.match()  只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None;
# re.search()  扫描整个字符串并返回第一个成功的匹配;
# re.findall()  查找所有匹配项；
# re.sub()  替换字符串中的匹配项;
# re.split()  切分字符串;
#
# ### 常用正则表达式
# \d     匹配任意一个数字，等价于 [0-9]
# \D     匹配任意一个非数字
# \w     匹配任意一个字母或数字
# \W	 匹配任意一个非字母数字
# \s     匹配任意一个空格（也包括Tab等空白符）
# \S	 匹配任意一个非空字符
# \A	 匹配字符串开始
# \Z	 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
# .      匹配任意字符
# *      匹配任意个字符（包括0个）
# +      匹配至少一个字符
# ?      匹配0个或1个字符
# {n}    匹配n个字符
# {n,m}  匹配n-m个字符
# A|B    表示匹配A或B
# ^      表示匹配行的开头，例如“^\d”表示必须以数字开头
# $      表示匹配行的结束，例如“\d$”表示必须以数字结束
# \-     转义特殊字符-
# \n	 匹配一个换行符
# \t     匹配一个制表符
#
# []         匹配范围，表示满足括号内的任一字符，如果是以“^”开头则表示反向匹配
# [aeiou]    匹配中括号内的任意一个字母
# [^aeiou]   除了aeiou以外的任意一个字符
# [0-9]      匹配任何一个数字
# [^0-9]     匹配除了数字外的任何一个字符
#
# ### 举例：
# \d{3}\s+\d{3,8} : 匹配以任意个空格隔开的带区号的电话号码(\d{3}匹配3个数字;\s+表示至少有一个空格;\d{3,8}表示3-8个数字;)
# [0-9a-zA-Z\_]+  : 匹配至少由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} : 匹配长度是1-20个的字符串（前面1个字符+后面最多19个字符）
#
# ### 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 如果想要采用非贪婪匹配（也就是尽可能少匹配），可以通过加“?”的类似方式来限定匹配结果；
#
# ### 括号
# 如果没有括号，返回：匹配正则表达式后的结果；
# 如果使用括号，返回：匹配正则表达式后，这个括号部分的结果；
# 如果使用多个括号，返回：匹配正则表达式后，多个括号部分的结果；
# 简而言之，有括号时只能返回正则表达式中括号部分的内容；
