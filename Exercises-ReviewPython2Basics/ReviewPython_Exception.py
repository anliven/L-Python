# -*- coding: utf-8 -*-
__author__ = 'Anliven'

##### 异常（Exception）

# ----------------------------------------------------------------------------------------------------------------------

# 在编写和调试代码的过程中，如果Python无法正常处理程序时，Python会抛出一个异常，表示一个错误。
# 如果这种异常没有被处理或者捕捉，程序就会终止运行，抛出异常信息来提醒用户处理这些错误。
# 一个异常可以是一个字符串，类或对象。 Python的内核提供的异常，大多数都是实例化的类。

##### 了解python标准异常有哪些？
# Exception  ----- 常规错误的基类
# Warning 	----- 警告的基类
# SyntaxWarning	----- 可疑的语法的警告
# RuntimeError 	----- 一般的运行时错误
# SyntaxError	----- Python 语法错误
# IndentationError	----- 缩进错误
# TabError	----- Tab 和空格混用
# 等等

# ----------------------------------------------------------------------------------------------------------------------

##### 捕捉异常
# try/except语句用来捕捉异常，检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 对于每个try从句，至少都有一个相关联的except从句。
# 如果当try语句执行时发生异常，python执行第一个匹配该异常的except子句，处理异常。
# 可以try/except语句关联上一个else从句。当没有异常发生的时候，else从句将被执行。
# 如果异常没有匹配的except子句，异常将被递交到上层的try来捕捉，直到默认的Python处理器被调用，终止程序运行，并且打印一个异常消息。

try:  # 通常的语句放在try-块中
    a = 10
    b = 0
    print a / b  # 因分母可以为零，会产生“ZeroDivisionError: integer division or modulo by zero”的异常错误
except ZeroDivisionError:  # 错误处理语句放在except-块中
    print "除零错误，已经捕获！"

# 如果使用except而不带任何异常类型，没有给出异常的名称，try-except语句捕获所有发生的异常。
# 不建议使用此方式，因为不能识别出具体的异常信息。

# except从句可以专门处理单一的异常，或者一组包括在圆括号内的异常。
# 如果需要同时捕捉多个可能的异常，可以把异常的类型，放入一个元组中，举例说明：except (ZeroDivisionError, TypeError）

# ----------------------------------------------------------------------------------------------------------------------

##### try-finally语句
# try-finally语句无论是否发生异常都将执行最后的代码。
# 注意：except语句和finally语句两者不能同时和try语句搭配使用。
# else语句不能与finally语句同时使用。

try:
    k1 = 123
    try:
        k1 = 321
    finally:  # 无论是否发生异常都将执行最后的代码。
        print "try-finally is running"
        print k1 / 0
except ZeroDivisionError:  # finally块中的所有语句执行后，异常被再次提出，并执行except块代码。
    print "try-except is running"
# ----------------------------------------------------------------------------------------------------------------------

##### 触发异常
# 可以使用raise语句来主动的触发Python程序的异常。
# 可以引发的异常应该是典型的继承自Error或Exception类，通过直接或间接的方式。
# 为了能够捕获异常，"except"语句必须用相同的异常类来捕获抛出的类对象或者字符串。


class ShortInputException(Exception):  # 定义一个子类ShortInputException，是Exception类的派生类。
    """A user-defined exception class."""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = raw_input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)  # raise语句来主动的触发
except EOFError:  # 指明错误/异常的名称。这里直接使用EOFError。
    print '\nWhy did you do an EOF on me?'  # 伴随异常 触发的 异常对象。
except ShortInputException, x:  # 在except从句中，提供了错误类和用来表示错误/异常对象的变量。这与函数调用中的形参和实参概念类似。
    print 'ShortInputException: The input was of length %d, was expecting at least %d' % (x.length, x.atleast)
else:
    print 'No exception was raised.'

# ----------------------------------------------------------------------------------------------------------------------

##### 异常的参数 ？？？
# 一个异常可以带上参数来输出异常信息。通过except语句来捕获异常的参数。
# 这个参数是用来表示错误/异常对象的变量，可以接收一个或者多个异常值，通常包含错误字符串，错误数字，错误位置等。

# Define a function here.


def temp_convert(var):
    try:
        print int(var)
    except ValueError, Argument:  # 一个异常可以带上参数来输出异常信息。通过except语句来捕获异常的参数。
        print "The argument does not contain numbers \n"
        print "The argument does not contain numbers \n", Argument  # 对比理解Argument的作用

# Call above function here.
temp_convert("xyz")

# ----------------------------------------------------------------------------------------------------------------------

##### 用户自定义异常
# 通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。


class NetworkWrongError(RuntimeError):  # 创建了一个子类，基类为RuntimeError,用于在异常触发时输出更多的信息。
    def __init__(self, arg):
        self.arg = arg
# 在定义以上类后，可以触发该异常，如下所示：
try:  # 在try语句块中，用户自定义的异常后执行except块语句
    raise NetworkWrongError("Bad hostname")
except NetworkWrongError, e:  # 在这里，变量 e 是NetworkWrongError类的实例。
    print e.arg

# ----------------------------------------------------------------------------------------------------------------------
