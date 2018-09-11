# -*- coding: utf-8 -*-
import re

print("# match: ", re.match('www', 'www.bing.com'))
print("# match: ", re.match('com', 'www.bing.com'))
if re.match(r'^(\d{3})-(\d{3,8})$', '028-12345678'):  # 利用函数返回值进行判断
    print('The match is successful.')

print("# search: ", re.search('www', 'www.bing.com'))
print("# search: ", re.search('com', 'www.bing.com'))
print("# search: ", re.search('www', 'www.bing.com').span(), re.search('com', 'www.bing.com').span())
if re.search('www', 'www.bing.com'):  # 利用函数返回值进行判断
    print('The match is successful.')

print("# split: ", re.split(r'[\s,]+', 'aaa,bbb, ccc,,,ddd   eee'))
print("# split: ", re.split(r'[\s,]+', 'aaa,bbb, ccc,,,ddd   eee', maxsplit=2))  # 指定分割次数

print("# sub: ", re.sub('{name}', 'Anliven', 'Hello {name}!'))  # 替换内容
print("# sub: ", re.sub(r'#.*$', "", "123-456-789 # this is a phone-number."))  # 删除注释
print("# sub: ", re.sub(r'\D', "", "123-456-789 # this is a phone-number."))  # 移除非数字的内容
print("# sub: ", re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', '2018-12-31'))  # 改变日期格式

text = 'He said: "En... this is a RE test!"'
print("# findall: ", re.findall(r'[.:"!]+', text))  # 找出指定标点符号
print("# findall: ", re.findall(r'[a-zA-Z]+', text))  # 找出字母组合
string = "aaaaa bbbbb ccccc ddddd eeeee fffff"
print("# findall: ", re.findall("\w+\s+\w+", string))
print("# findall: ", re.findall("(\w+)\s+\w+", string))  # 注意括号的使用
print("# findall: ", re.findall("((\w+)\s+\w+)", string))

print("# escape: ", re.escape('www.python.org'))
print("# escape: ", re.escape('This is a test!'))

# ### 正则表达式(Regular Expression）
# 正则表达式是可匹配文本片段的模式；
# 利用正则表达式，可以在文本中查找符合匹配模式的片段、替换文本内容、分割文本等；
#
# ### 标准库re模块
# re模块包含所有正则表达式的功能，用编译后的正则表达式去匹配字符串，如果正则表达式的字符串本身不合法，则会报错；
# 详细信息：https://docs.python.org/3/library/re.html
#
# ### 常用方法
# - re.match()  在字符串开头匹配模式，如果匹配成功返回匹配对象（Match object），失败则返回None;
# - re.search()  扫描整个字符串并返回第一个成功的匹配对象（Match object），否则返回None;
# - re.findall()  返回一个列表，包含字符串中所有与模式匹配的子串；
# - re.finditer()  返回字符串中所有的匹配，返回形式为迭代器，调用group()、groups()或group(index)方法获取匹配结果；
# - re.sub()  替换字符串中的匹配项;
# - re.split()  根据模式分割字符串;
# - re.escape()  对字符串中所有可能被视为正则表达式运算符的字符进行转义;
#
# ### 转义特殊字符
# 在Python中，如果要让特殊字符的行为与普通字符相同，必须对其进行转义；
# 在特殊字符前加上一个反斜杠“\”，即可完成转义，强烈建议使用Python的r前缀，就不用考虑转义的问题；
# 一些示例：
# - “\-”               转义特殊字符“-”
# - “\\”               转义特殊字符“\”
# - “python\\.org”     匹配“python.org”
# - “r'python.org'”    使用原始字符串匹配“python.org”
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
# .      匹配任意一个字符（与除换行符外的任何字符都匹配，因此被称为通配符wildcard）
# *      匹配任意个字符（包括0个）
# +      匹配至少一个字符
# ?      匹配0个或1个字符，
# {n}    匹配n个字符
# {n,m}  匹配n-m个字符
# A|B    表示匹配A或B
# ^      指定匹配行的开头，例如“^\d”表示必须以数字开头
# $      指定匹配行的结尾，例如“\d$”表示必须以数字结尾
# \n	 匹配一个换行符
# \t     匹配一个制表符
#
# ### 字符集
# 字符集用来表示匹配范围；
# 用方括号将一个子串括起，就可创建一个字符集，表示满足括号内的任意一个字符，如果是以“^”开头则表示反向匹配）；
# 在字符集中，可以对“? * .”等特殊字符进行转义，但通常无需这样做；
# 特别注意：字符集只能匹配一个字符；
# 一些示例：
# - [aeiou]        匹配中括号内的任意一个字母
# - [^aeiou]       除了aeiou以外的任意一个字符
# - [0-9]          匹配任何一个数字
# - [^0-9]         匹配除了数字外的任何一个字符
# - [a-zA-Z0-9]    匹配大小写字母、数字的任意一个字符
#
# ### 子模式、可选模式和重复模式
# 模式“python|perl”，使用子模式的方式可以重写为“p(ython|erl)”；
# 特别注意：单个字符也可成为子模式；
# 在子模式后面加上“?”，可将其指定为可选的（可出现一次，也可不出现），每个可选的子模式都放在圆括号内；
# 例如：“r'(www\.)?python\.org'”可匹配“www.python.org”和“python.org”;
# 重复模式（子模式可以重复多次）：
# - (pattern)*         pattern可重复0、1或多次
# - (pattern)+         pattern可重复1或多次
# - (pattern){m,n}     pattern可重复m~n次
# 例如：“r'w{2,3}\.python\.org'”只匹配“ww.python.org”和“www.python.org”;
#
# ### 一些示例：
# \d{3}\s+\d{3,8} : 匹配以任意个空格隔开的带区号的电话号码(\d{3}匹配3个数字;\s+表示至少有一个空格;\d{3,8}表示3-8个数字)
# [0-9a-zA-Z\_]+  : 匹配至少由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} : 匹配长度是1-20个的字符串（前面1个字符+后面最多19个字符）
# r'(www\.)?python\.org'  : 匹配“www.python.org”和“python.org”
# r'w{2,3}\.python\.org'  : 匹配“ww.python.org”和“www.python.org”
#
#
# ### re.findall()中的括号
# 如果没有括号，返回：匹配正则表达式后的结果；
# 如果使用括号，返回：匹配正则表达式后，这个括号部分的结果；
# 如果使用多个括号，返回：匹配正则表达式后，多个括号部分的结果；
# 简而言之，有括号时只能返回正则表达式中括号部分的内容；
