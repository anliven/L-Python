# -*- coding: utf-8 -*-
__author__ = 'Anliven'

from sys import argv
script, user_name = argv
prompt = '>'
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#用下面的方法运行程序（注意必须传递一个参数）
# >python Exercise-14 argv.py liven   #当运行这个脚本时， argv 参数接收到脚本名称Exercise-14 argv.py和名称liven。
#将看到下面的结果
# Hi liven, I'm the Exercise-14 argv.py script.
# I'd like to ask you a few questions.
# Do you like me liven?
# > yes
# Where do you live liven?
# > chengdu
# What kind of computer do you have?
# > asus
#
# Alright, so you said 'yes' about liking me.
# You live in 'chengdu'. Not sure where that is.
# And you have a 'asus' computer. Nice.