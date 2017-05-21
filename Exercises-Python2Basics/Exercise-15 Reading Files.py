# -*- coding: utf-8 -*-
__author__ = 'Anliven'

from sys import argv #引入sys库的argv功能
script, filename = argv
txt = open(filename) #open 打开文件，返回一个file object，此时并没有获取文件的内容
print "Here's your file %r:" % filename
print txt.read() #利用文件对象的read（）方法获取了文件内容
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()


#open方法
# C:\Users\Anliven>python -m pydoc open
# Help on built-in function open in module __builtin__:
#
# open(...)
#     open(name[, mode[, buffering]]) -> file object
#
#     Open a file using the file() type, returns a file object.  This is the
#     preferred way to open a file.  See file.__doc__ for further information.


#用下面的方法运行程序
# >python Exercise-15.py Exercise-15-sample.txt
#将看到下面的结果
# Here's your file 'Exercise-15-sample.txt':
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# Type the filename again:
# > Exercise-15-sample.txt
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.