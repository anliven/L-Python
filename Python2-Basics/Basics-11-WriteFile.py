
# -*- coding: utf-8 -*-
__author__ = 'Anliven'

filename = "Basics-sample01.txt"
print ("Opening the file : %s" % filename)
target = open(filename, 'w')  # 'w'表示写入(write)模式；'r'读取（read）；'a'追加(append)
target.truncate()  # truncate方法清空文件，小心使用

print ("Enter three lines in the file.")
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.close()

txt = open(filename)
print ("Here's your file %r." % filename)
print ("The contents of txt file are shown below : ")
print (txt.read())

# 文件相关操作
# close – 保存并关闭文件
# read – 读取文件内容；open()方法的默认工作方式
# readline – 读取文本文件中的一行
# truncate – 清空文件，小心使用
# write(stuff) – 将stuff写入文件
