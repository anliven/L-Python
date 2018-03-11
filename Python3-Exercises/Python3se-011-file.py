#! python3
# -*- coding: utf-8 -*-
import time

input_content = input("Enter your words:")

localtime = time.strftime("%Y%m%d%H%M%S")
filename = localtime + "_Sample.txt"

f = open(filename, 'wt')
f.write("Some words : %s " % input_content)
f.close()

# 以文件形式保存输入内容, 文件名以日期时间作为前缀；
