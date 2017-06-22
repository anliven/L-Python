# -*- coding: utf-8 -*-
__author__ = 'Anliven'

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Pydoc is a documentation module for the programming language Python
# 在window系统命令行执行“python -m pydoc 函数名或模块名”,可以看到自动生成的介绍资料。
#
# C:\Users\Anliven>python -m pydoc raw_input
# Help on built-in function raw_input in module __builtin__:
#
# raw_input(...)
#     raw_input([prompt]) -> string
#
#     Read a string from standard input.  The trailing newline is stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.
