# -*- coding: utf-8 -*-
__author__ = 'Anliven'

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y
print "I said: %r." % x  # %r 不管什么都打印出来
print "I said: %s." % x  # %s 字符串
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w + e

# %r 用来做 debug 比较好，因为它会显示变量的原始数据（raw data）
# 而%s %d等其它的符号则是用来向用户显示输出的。
