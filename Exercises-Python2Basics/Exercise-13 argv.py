# -*- coding: utf-8 -*-
__author__ = 'Anliven'

from sys import argv # “import”语句引入所需要的模块。需要什么就调用什么，程序保持精简。
# argv 是“参数变量(argument variable)”，这个变量包含了要传递给 Python 的参数
script, first, second, third = argv #将 argv“解包(unpack)”，将每个参数赋予一个变量名： script, first, second, 以及 third。
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#用下面的方法运行程序（注意必须传递*三*个参数）
# >python "Exercise-13 argv.py" first 2nd 3rd
#将看到下面的结果
# The script is called: Exercise-13 argv.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
#
# >python Exercise-13 argv.py cheese apples bread
# The script is called: Exercise-13 argv.py
# Your first variable is: cheese
# Your second variable is: apples

# argv 和 raw_input() 有什么不同？
# 不同点在于用户输入的时机。
# 如果参数是在用户执行命令时就要输入，那就是 argv，
# 如果是在脚本运行过程中需要用户输入，那就使用 raw_input()。