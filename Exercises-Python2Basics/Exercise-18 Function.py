# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# this one is like your scripts with argv
def print_two(*args): #函数接受不定数目的参数，（*args）的功能把函数的所有参数都接受进来，然后放到名字叫 args 的列表中去。
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  # 函数接受两个参数
    print "arg1: %r, arg2: %r" % (arg1, arg2)
#在 Python 函数中可以跳过整个参数解包的过程，直接使用 () 里边的名称作为变量名。

# this just takes one argument
def print_one(arg1):  # 函数接受单个参数
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none(): # 函数可以不接受参数
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()


# 函数能提高应用的模块性，和代码的重复利用率。
#
# 定义一个函数
#   函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
#   函数名只以字母数字以及下划线组成，而且不是数字开始。
#   任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。不能使用重复的参数名。
#   函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
#   函数内容以冒号起始，并且缩进。
#   Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
#
# 语法
# def functionname( parameters ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
