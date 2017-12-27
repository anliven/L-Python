
# -*- coding: utf-8 -*-
__author__ = 'Anliven'

filename = "Basics-sample01.txt"
txt = open(filename)  # open方法打开文件，返回一个file object，此时并没有获取文件的内容
print ("Here's your file %r." % filename)
print ("The contents of txt file are shown below : ")
print (txt.read())  # 利用文件对象的read方法获取文件内容

# 获取open方法的信息：“python -m pydoc open”
