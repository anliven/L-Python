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
except (TypeError, NameError) as e:  # 可在一个元组中指定多个异常
    print('Catch TypeError or NameError:', e)
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

# ### 同时捕获多个异常
# 可以使用多个except子句来捕获不同类型的异常；
# 也可以在一个except子句通过元组同时指定多个异常；
#
# ### finally子句
# finally子句总会得到执行，常见做法是在try块中获取资源，然后在finally块中释放资源；
#
# ### 自定义异常
# 必要时可以自定义异常，但建议尽量使用Python内置的错误类型；
#
# ### logging
# Python内置的logging模块可以非常容易地记录错误信息，程序打印完错误信息后会继续执行，并正常退出；
# 通过配置logging可以把错误记录到日志文件里，方便事后排查；
