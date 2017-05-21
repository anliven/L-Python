# -*- coding: utf-8 -*-
__author__ = 'Anliven'

print "How old are you?", #注意:每行 print 后面加了个逗号(comma) ,
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "So, you're %r old, %r tpall and %r heavy." % (age, height, weight)

print int(raw_input()) #int()函数可以把用户输入的字符串转换成整数

#raw_input() 与input()都是python 的内建函数，通过读取控制台的输入与用户实现交互
#推荐使用 raw_input() 来与用户交互。
#
# raw_input() #将任何类型的输入都直接当作一串字符，可以不用加引号，返回字符串类型
# input()  #可以直接输入数字,或者读取合法的 python 表达式，输入字符的要用引号''或者双引号""
#
# 当输入为纯数字时
#     raw_inpout返回的是字符串类型，string类型
#     input返回的是数值类型，如int,float
#     可以利用type()函数来验证他们的返回值类型。
#
# 当输入为字符串表达式时
#     input会计算在字符串中的数字表达式，而raw_input不会。
#     比如输入 “57 + 3”:  input会得到整数60,而raw_input会得到字符串”57 + 3”
#     也就是说input() 函数会把输入的东西当做Python 代码进行处理，这么做会有安全问题，应该避开这个函数。
#
# 其原理如下：在python input 的文档中，input的定义是这样的：
# def input(prompt):
#     return (eval(raw_input(prompt)))
# 本质上input() 还是使用 raw_input() 来实现的，只是调用完 raw_input() 之后再调用 eval() 函数。
# 除非对 input() 有特别需要，否则一般情况下，都是推荐使用 raw_input() 来与用户交互。