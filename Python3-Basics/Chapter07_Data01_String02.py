# -*- coding: utf-8 -*-
from string import Template

pi = 3.1415926

tmp = Template("Hello $what. I am $who.")  # 使用模板字符串
tmp.substitute(what="Python3", who="Anliven")
print(tmp.substitute(what="Python3", who="Anliven"))

print("Hello %s. I am %s." % ('Python3', 'Anliven'))  # 使用字符串格式设置运算符（百分号）和转换说明符（这里为%s）
print("What time is it now? It’s %d o’clock." % 10)  # 转换说明符（%d）

print("Hello {}. I am {}.".format('Python3', 'Anliven'))  # 使用字符串方法format
print("{2}---{1}---{0}".format('AAA', 'BBB', 'CCC'))  # 替换索引
print("{name} is {value:.2f}.".format(value=pi, name='PI'))  # 替换字段名
print("{chr1}---{1}---{chr2}---{0}".format('aaa', 'bbb', chr1='ccc', chr2='ddd'))
print("The number is {num}---{num:f}---{num:b}---{num:#b}.".format(num=123))  # 指定转换的值类型
print("#{test1:4.2f}# --- #{test2:10}#.".format(test1=123.456, test2="789"))  # 指定宽度和精度
print("{:,}".format(123456789))  # 千位分隔符

print("{:010.2f}".format(pi))  # 指定填充内容，默认为(零、加号、减号、空格)，默认为空格
print("{:^010.2f}".format(pi))  # 指定对齐方式（对齐说明符：<左对齐、>右对齐、^居中）
print("{:$^010.2f}".format(pi))  # 扩充对齐说明符

# ### 设置字符串格式
# - 使用模板字符串；
# - 使用字符串格式设置运算符（百分号）和转换说明符；
# - 使用字符串方法format；
