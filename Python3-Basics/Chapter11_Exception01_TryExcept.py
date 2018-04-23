#! python3
# -*- coding: utf-8 -*-
import os

testText = '''
Man: Action is the antidote to despair!
(pause)
Other Man: There are two best times to plant a tree: one is ten years ago, and the other is now!
(pause)
'''
testFile = 'test.txt'

f = open(testFile, 'w', encoding="utf-8")
f.write(testText)
f.close()

try:
    data = open('test.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)  # 分解字符串并分别赋值给多个变量
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:  # ValueError表示数据不符合期望的格式
            pass  # Python的空语句或null语句，什么也不做

    data.close()
except IOError as err:  # IOError表示数据无法正常访问；使用as关键字赋给一个标识符
    print('File error : The datafile is missing!' + str(err))  # 这里str()将异常对象转换为字符串

os.remove(testFile)

# ### 异常（Exception）
# 程序运行错误时会出现异常，并产生一个traceback（详细的错误描述）；
# try/except语句提供了一个异常处理机制，从而保护可能导致运行时错误的某些代码行；
# 使用except语句，需要明确指定对应的异常类型，避免一般化的处理；
#
# ### 复杂性
# 如果以“增加额外代码和逻辑”的方式来处理“所有必须考虑的错误”，那么代码必将越来越复杂，甚至会掩盖程序的本来作用；
# 如果以异常处理的方式，则不会掩盖程序的主要作用，真正关注代码的功能实现；
# 使用try/except语句可以关注代码真正的工作，避免增加不必要的代码和逻辑，让代码易读易写；
#
# ### 有关异常的信息
# https://docs.python.org/3/library/exceptions.html
