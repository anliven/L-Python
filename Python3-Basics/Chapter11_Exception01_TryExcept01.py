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
            print(role, 'said: ', end='')
            print(line_spoken, end='')
        except ValueError:  # ValueError表示数据不符合期望的格式
            pass  # Python的空语句或null语句，什么也不做

    data.close()
except IOError as err:  # IOError表示数据无法正常访问；使用as关键字赋给一个标识符
    print('File error : The datafile is missing!' + str(err))  # 这里str()将异常对象转换为字符串

os.remove(testFile)

# ### 异常（Exception）
# 程序运行错误时会出现异常，并产生一个traceback（详细的错误描述）；
# 详细信息：https://docs.python.org/3/library/exceptions.html
#
# ### try/except语句
# try/except语句提供异常的处理机制（捕获异常并对其处理），从而保护可能导致运行时错误的某些代码行；
# try代码块存放可能引发异常或错误的语句，except代码块存放相应的错误或异常的处理器（Handler）；
# 必须至少存在一个except语句与try配合使用，而且需要明确指定对应的异常类型，避免一般化的处理；
# 如果没有指定错误或异常的处理方式，默认只会在终端打印出相应信息；
#
# ### BaseException类
# Python所有的错误都是从BaseException类派生的;
# 常见的错误类型和继承关系:https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#
# ### 一些常见的异常
# Exception            通用异常，是常规错误的基类
# AttributeError       引用属性或赋值失败时引发
# AssertionError       断言语句失败
# SyntaxError	       语法错误
# SyntaxWarning	       可疑的语法的警告
# IndentationError	   缩进错误
# NameError	           未声明/初始化对象 (没有属性)
# IOError	           输入/输出操作失败
# OSError	           操作系统错误，不能执行指定的任务
# TypeError	           对类型无效的操作
# ValueError	       传入无效的参数
# IndexError	       序列中没有此索引(index)
# KeyError	           映射中没有这个键
# NotImplementedError  尚未实现的方法
# TabError	           Tab和空格混用
# ImportError	       导入模块/对象失败
# RuntimeError	       一般的运行时错误
# SystemError	       一般的解释器系统错误
# UserWarning	       用户代码生成的警告
# ZeroDivisionError	   除法或求模运算的第二个参数为零时引发
# ......
#
# ### 复杂性
# 如果以“增加额外代码和逻辑”的方式来处理“所有必须考虑的错误”，那么代码必将越来越复杂，甚至会掩盖程序的本来作用；
# 如果以异常处理的方式，则不会掩盖程序的主要作用，真正关注代码的功能实现；
# 使用try/except语句可以关注代码真正的工作，避免增加不必要的代码和逻辑，让代码易读易写；
# 不需要在每个可能出错的地方去捕获异常，只需要在合适的层次去捕获，可以有效减少try...except的频率；
#
# ### 异常与函数
# 如果不处理函数中的异常，此异常将上传到上一层调用者；
# 如果上一层调用者也不处理此异常，此异常将继续上传，最终到达主程序（全局作用域）；
# 如果主程序也没有处理此异常，程序将终止，Python解释器会打印栈跟踪信息（Traceback）；
# 根据栈跟踪信息（Traceback），可以定位错误和分析异常；
