#! python3
# -*- coding: utf-8 -*-


try:
    print('# This is try...')
    # r = 10 / int('2')
    # r = 10 / 0  # 抛出异常ZeroDivisionError
    r = 10 / int('test')  # int()函数抛出异常ValueError
    print('Result:', r)
except ValueError as e:
    print('Catch ValueError:', e)
except ZeroDivisionError as e:  # 可以有多个except来捕获不同类型的错误
    print('Catch ZeroDivisionError:', e)
else:
    print('# This is else... No error!')
finally:
    print('# This is finally...')
print('# END.')


class ShortInputException(Exception):  # 自定义异常类型
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something(more than 3 characters): ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:  # 文件结尾（End of File）符号，按下[ctrl-d]实现
    print('Why did you do an EOF on me?')
except ShortInputException as ex:  # 将自定义异常类型存储为错误名或异常名
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:  # 没有错误发生时，自动执行else语句
    print('No exception was raised.')
finally:
    print("Done.")


# ### 异常（Exception）
# - 程序出现例外情况时就会发生异常（Exception）;
# - 使用try..except语句处理异常状况，必须至少存在一个except语句与try配合使用；
# - try代码块存放可能引发异常或错误的语句，except代码块存放相应的错误或异常的处理器（Handler）；
# - 如果没有指定错误或异常的处理方式，默认只会在终端打印出相应信息；
# - 可以将一个else子句与try..except代码块相关联，在没有发生异常的时候执行；
# - finally子句总会得到执行，常见做法是在try块中获取资源，然后在finally块中释放资源；
# - 不需要在每个可能出错的地方去捕获错误，只需要在合适的层次去捕获错误，可以有效减少try...except...finally的频率；
#
# ### 主动抛出异常
# - 通过raise语句来引发一次异常；能够引发的错误或异常必须是直接或间接从属于Exception类的派生类；
# - 如果当前函数不知道如何处理某个异常，可以继续往上抛，让上层调用者来处理；
# - raise语句如果不带参数，会把当前错误原样抛出；
#
# ### BaseException类
# Python所有的错误都是从BaseException类派生的;
# 常见的错误类型和继承关系:https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#
# ### 调用栈
# 如果不捕获错误，Python解释器会打印出错误的调用栈信息，可以用来定位错误的位置和分析异常；
#
# ### logging
# Python内置的logging模块可以非常容易地记录错误信息，程序打印完错误信息后会继续执行，并正常退出；
# 通过配置logging可以把错误记录到日志文件里，方便事后排查；
#
# ### 自定义异常
# 必要时可以自定义异常，但建议尽量使用Python内置的错误类型；
