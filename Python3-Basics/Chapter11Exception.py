#! python3
# -*- coding: utf-8 -*-


class ShortInputException(Exception):  # 自定义异常类型
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something : ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:  # 文件结尾（End of File）符号，按下[ctrl-d]实现
    print('Why did you do an EOF on me?')
except ShortInputException as ex:  # 将自定义异常类型存储为错误名或异常名
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
finally:
    print("Done.")

testList = ['item']
assert len(testList) >= 1
# testList.pop()
# assert len(testList) >= 1

# ### 异常（Exception）
# - 程序出现例外情况时就会发生异常（Exception）;
# - 使用try..except语句处理异常状况，必须至少存在一个except语句与try配合使用；
# - try代码块存放可能引发异常或错误的语句，except代码块存放相应的错误或异常的处理器（Handler）；
# - 通过raise语句来引发一次异常；能够引发的错误或异常必须是直接或间接从属于Exception类的派生类；
# - 如果没有指定错误或异常的处理方式，默认只会在终端打印出相应信息；
# - 可以将一个else子句与try..except代码块相关联，在没有发生异常的时候执行；
# - finally子句总会得到执行，常见做法是在try块中获取资源，然后在finally块中释放资源；
#
# ### 断言（Assert）
# - assert 语句用以断言某事是否为真，如果不是真的，就抛出一个断言失败错误AssertionError；
