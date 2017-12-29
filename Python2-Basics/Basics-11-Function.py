# -*- coding: utf-8 -*-
__author__ = 'Anliven'


def print_two(*args):  # 接受不定数目的参数，（*args）接受函数的所有参数然后放到名为args的列表中
    """

    :param args:
    """
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))


def print_two_again(arg1, arg2):  # 接受两个参数
    """

    :param arg1:
    :param arg2:
    """
    print ("arg1: %r, arg2: %r" % (arg1, arg2))


def print_one(arg1):  # 接受单个参数
    """

    :param arg1:
    """
    print ("arg1: %r" % arg1)


def print_none():  # 不接受参数
    """
    no args
    """
    print ("No args.")


str1 = "AAA"
str2 = "BBB"
print_two("AAA", "BBB")
print_two_again(str1, str2)  # 可以在函数里用变量名
print_two_again(str1 + str2, str1 + str2)  # 可以在函数里做运算
print_two_again(str1 + str2 + "CCC", str1 + str2 + "CCC")  # 可以将变量和运算结合起来
print_one("AAA")
print_none()

# 函数能提高应用的模块性，和代码的重复利用率
# 定义函数:
#   函数代码块以def关键词开头，后接函数标识符名称和圆括号();
#   函数名只以字母数字以及下划线组成，而且不是数字开始;
#   任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。不能使用重复的参数名;
#   函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明;
#   函数内容以冒号起始，并且缩进;
#   Return[expression]结束函数，选择性地返回一个值给调用方;不带表达式的return相当于返回 None;

# 函数的帮助文档
# 函数的帮助文档就是定义函数时放在"""之间的内容，也被称作 documentation comments （文档注解）
# 命令行下执行help（模块名）或help（模块名.方法名）会得到对应的帮助文档信息