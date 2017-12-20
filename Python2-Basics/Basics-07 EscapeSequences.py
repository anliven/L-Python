# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 转义字符：反斜杠 \(back-slash)；双反斜杠(double backslash)“\\”会打印出一个反斜杠
print "I am 6'2\" tall."  # 双引号转义
print 'I am 6\'2" tall.'  # 单引号转义
print "\\"

tabby_cat = "\tI'm tabbed in."  # \t ASCII --- HorizontalTab (TAB) 水平制表符
persian_cat = "I'm split\non a line."  # \n --- ASCII Linefeed(LF) 换行符
backslash_cat = "I'm \\ a \\ cat."  # 输出反斜杠
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
# 一组三引号(triple-quotes)之间放入任意多行文字
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 转义序列(escape sequences)
# 转义符功能
# \\ --- Backslash (\)反斜杠
# \' --- Single quote(‘) 单引号
# \" --- Double quote(”) 双引号
# \a --- ASCII Bell(BEL) 响铃符
# \b --- ASCII Backspace(BS) 退格符
# \f --- ASCII Formteed(FF) 进纸符
# \n --- ASCII Linefeed(LF) 换行符
# \N{name}--- Unicode 数据库中的字符名，其中 name 就是它的名字(Unicode only)
# \r ASCII --- CarriageReturn (CR)回车符
# \t ASCII --- HorizontalTab (TAB) 水平制表符
# \uxxxx --- 值为 16 位十六进制值xxxx 的字符(Unicode only)
# \Uxxxxxxxx --- 值为 32 位十六进制值xxxx 的字符(Unicode only)
# \v --- ASCIIVertical Tab(VT) 垂直制表符
# \ooo --- 值为八进制值ooo 的字符
# \xhh --- 值为十六进制 数 hh 的字符
