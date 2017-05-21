# -*- coding: utf-8 -*-
__author__ = 'Anliven'

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# True 和 False 没有加引号，不是字符串，而是 Python 的关键字，用来表示真假的意义。
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)

#单引号（single quotation），双引号（double quotation），多引号（triple quotes）区别
print 'hello,world',"hello,world",'''hello,world''',"""hello,world"""

print 'Let\'s go!' #字符串中有一个'，而字符串又是用'来表示，所以这个时候就要使用转义符 \
print "Let's go!" #用 " 来表示字符串,python就把字符串中的单引号 ' , 当成普通的字符处理.

print "hello,\
world" #写成多行，要使用\ (“连行符”).
print '''hello,
world''' #使用3个单引号或双引号的话，就可以直接写成多行
print """hello,
world"""
#''' 和 """：只是风格的区别，在基本使用上是一样的。