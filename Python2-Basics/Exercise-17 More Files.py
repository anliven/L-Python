# -*- coding: utf-8 -*-
__author__ = 'Anliven'

from sys import argv
from os.path import exists #exists将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False。
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
  #  we could do these two on one line too, how?
  #  in_file = open(from_file)
  #  indata = in_file.read()
indata = open(from_file).read()  #上两行合为这一行
print "The input file is %d bytes long" % len(indata)  #len()函数以数字的形式返回你传递的字符串的长度
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)
print "Alright, all done."
out_file.close()
#in_file.close()


# 用下面的方法运行程序
# >python Exercise-17 More Files.py Exercise-17-sample.txt Exercise-17-sample-copy.txt
# 将看到下面的结果
# Copying from Exercise-17-sample.txt to Exercise-17-sample-copy.txt
# The input file is 81 bytes long
# Does the output file exist? True
# Ready, hit RETURN to continue, CTRL-C to abort.
#
# Alright, all done.


#程序简写
#open(raw_input("to_file:"),'w').write(open(raw_input("from_file:")).read())