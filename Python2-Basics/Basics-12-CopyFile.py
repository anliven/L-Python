
# -*- coding: utf-8 -*-
from os.path import exists  # exists方法将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False

__author__ = 'Anliven'

from_file = "Basics-sample01.txt"
to_file = "Basics-sample02.txt"

print ("Copying from %s to %s" % (from_file, to_file))
inData = open(from_file).read()
print ("The input file is %d bytes long" % len(inData))  # len()函数以数字的形式返回传递的字符串的长度
print ("Does the output file exist? %r" % exists(to_file))
out_file = open(to_file, 'w')
out_file.write(inData)
print ("Alright, all done.")
out_file.close()

# 程序简写：open(raw_input("to_file:"),'w').write(open(raw_input("from_file:")).read())

txt = open(to_file)
print ("Here's your file %r." % to_file)
print ("The contents of txt file are shown below : ")
print (txt.read())
