# -*- coding: utf-8 -*-
__author__ = 'Anliven'

from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename, 'w') # 'w'表示写入(write)模式，'r' 表示读取（read）， 'a' 表示追加(append)。
print "Truncating the file. Goodbye!"
target.truncate() #truncate – 清空文件，请小心使用该命令。
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3+"\n")
print "And finally, we close it."
target.close()

# 用下面的方法运行程序
# >python Exercise-16 Reading and Writing Files.py Exercise-16-sample.txt
# 将看到下面的结果
# We're going to erase 'Exercise-16-sample.txt'.
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# ?
# Opening the file...
# Truncating the file. Goodbye!
# Now I'm going to ask you for three lines.
# line 1: To all the people out there.
# line 2: I say I don't like my hair.
# line 3: I need to shave it off.
# I'm going to write these to the file.
# And finally, we close it.


# 文件相关操作
# • close – 关闭文件。跟编辑器的 文件->保存.. 一个意思。
# • read – 读取文件内容。把结果赋给一个变量。 open() 函数的默认工作方式。
# • readline – 读取文本文件中的一行。
# • truncate – 清空文件，请小心使用该命令。
# • write(stuff) – 将 stuff 写入文件。

