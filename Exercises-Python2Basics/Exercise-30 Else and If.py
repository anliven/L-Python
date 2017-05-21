# -*- coding: utf-8 -*-
__author__ = 'Anliven'

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."


# Python 编程中 if 语句用于控制程序的执行，基本形式为：
# if 判断条件：
#     执行语句……
# else：
#     执行语句……
# 其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。
# else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句。

# 当判断条件为多个值是，可以使用以下形式：
# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……

