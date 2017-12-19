# -*- coding: utf-8 -*-
__author__ = 'Anliven'

cars = 100  # "=(single-equal)" 的作用是将右边的值赋予左边的变量
drivers = 30
cars_not_driven = cars - drivers  # 计算;下划线(underscore) 字符通常被用来隔开单词
print cars, "cars available.", drivers, "drivers available.", cars_not_driven, "empty cars."
print "Hey %s there." % "you"  # "you"是字符串，不是变量

my_name = 'Anliven'  # 变量名以字母开头
my_age = 35
my_height = 175
my_weight = 72
print "Let's talk about %s." % my_name  # "%s"格式化字符串(formatstring);"%"运算符实际上是一种“格式控制工具”
print "He's %d inches tall and %d kilos heavy." % (my_height, my_weight)  # 两个及以上的值则需要用小括号括起来
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

test = """hello,\nworld"""
print "this is test1: %s" % test
print "this is test2: %r" % test

# %实际上是一种“格式控制工具”：把右边的变量带到字符串中，并且把变量值放到 %code(字符串格式化代码) 所在的位置上。
# %% 	百分号标记，即在”格式标记字符串“中输出%本身
# %c 	字符及其ASCII码
# %s 	字符串
# %r    表示打印的是对象，打印所有内容；因为可以显示原始数据（raw data）能用来做debug
# %d 	有符号整数(十进制)
# %u 	无符号整数(十进制)
# %o 	无符号整数(八进制)
# %x 	无符号整数(十六进制)
# %X 	无符号整数(十六进制大写字符)
# %e 	浮点数字(科学计数法)
# %E 	浮点数字(科学计数法，用E代替e)
# %f 	浮点数字(用小数点符号)
# %g 	浮点数字(根据值的大小采用%e或%f)
# %G 	浮点数字(类似于%g)
# %p 	指针(用十六进制打印值的内存地址)
# %n 	存储输出字符的数量放进参数列表的下一个变量中

formatter = "%r %r %r %r %r %r"
print formatter % ("one", "two three", 123, True, False, formatter)
