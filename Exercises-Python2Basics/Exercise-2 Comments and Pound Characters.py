# -*- coding: utf-8 -*-
# 如果 # 是注解的意思，为什么 # -*- coding: utf-8 -*- 能起作用呢？
# Python 其实还是没把这行当做代码处理，这种用法只是让字符格式被识别的一个方案

__author__ = 'Anliven'

# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
print "I could have code like this." # and the comment after is ignored
# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."
print "This will run."
print "Hi # there." # 这行代码里的 # 处于字符串内部，所以它就是引号结束前的字符串中的一部分，这时它只是一个普通字符，而不代表注解的意思。