# -*- coding: utf-8 -*-
__author__ = 'Anliven'

people = 20
cats = 30
dogs = 15
if people < cats:
    print "Too many cats! The world is doomed!"
if people > cats:
    print "Not many cats! The world is saved!"
if people < dogs:
    print "The world is drooled on!"
if people > dogs:
    print "The world is dry!"

dogs += 5
if people >= dogs:
    print "People are greater than or equal to dogs."
if people <= dogs:
    print "People are less than or equal to dogs."
if people == dogs:
    print "People are dogs."

# Python 编程中 if 语句用于控制程序的执行，基本形式为：
# if 判断条件：
#    执行语句……
# 其中"判断条件"成立时（为真），则执行后面的语句，否则就跳过这一段。执行内容可以多行，以缩进来区分表示同一范围。
