# -*- coding: utf-8 -*-
# 输入三个数值 分别将它们保存到不同的变量中。不使用列表或排序算法，对这三个数进行正向和逆向排序。
import sys
print "please input the numbers"
a, b, c = map(int, sys.stdin.readline().split())
if a >= b:
    first = a
    second = b
else:
    first = b
    second = a
if c >= first:
    third = second
    second = first
    first = c
else:
    if c >= second:
        third = second
        second = c
    else:
        third = c
print first, second, third
print third, second, first


# 提示用户输入一个1 和 100 之间的数，如果满足条件，显示成功并退出。否则显示错误再次提示输入，直到满足条件为止。
print "please input a number between 1 and 100"
try_number = input()
while try_number > 100 or try_number < 1:
    print "wrong"
    try_number = input()
print "right"


# 判断给定年份是否是闰年
print "please input a particular year"
your_year = input()
test_year = (your_year % 4 == 0 and your_year % 100 != 0) or your_year % 400 == 0
if test_year:
    print "this is a leap year"
else:
    print "this is not a leap year"


# 写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转.
# 比如,输入"Mr.Ed",应该返回"mR.eD"作为输出
def str_swap(in_string):
    out_string = ""
    for letter in in_string:
        if 97 <= ord(letter) <= 122:
            out_string += chr(ord(letter) - 32)
        elif 65 <= ord(letter) <= 90:
            out_string += chr(ord(letter) + 32)
        else:
            out_string = out_string + letter
    return out_string

print "Please input a string :"
input_string = raw_input()
print str_swap(input_string)  # 利用ASCII码
print input_string.swapcase()  # 利用string的swapcase方法

# ord()函数:以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，
# chr()函数:用一个范围在range（256）内的（就是0～255）整数作参数，返回一个对应的字符。


# 在Linux系统上, 进行数据库查询, 并将查询结果以文件形式保存, 文件名以日期时间作为前缀.
# #!/usr/bin/env python
# import time
# import MySQLdb
# db = MySQLdb.connect(host='localhost', user='', passwd='', db='ppg_ett')
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# localtime = time.strftime("%Y%m%d%H%M%S")
# filename = localtime+"_DBcheck.txt"
# f = open(filename, 'wt')
# f.write("Database version : %s " % data)
# f.close()
