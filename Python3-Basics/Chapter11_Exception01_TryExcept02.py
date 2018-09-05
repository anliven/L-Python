# -*- coding: utf-8 -*-


class TestException():
    muffled = False  # 关闭抑制异常

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:  # 判断是否抑制异常，如果启用则打印指定信息，否则异常继续传播
                print("### Division by zero is illegal.")
            else:
                raise  # 调用raised且不提供任何参数，可重新引发异常（继续向上传播）


t = TestException()
print(t.calc('6/2'))
t.muffled = True  # 启用
print(t.calc('6/0'))

try:
    1 / 0
except ZeroDivisionError:
    raise ValueError from None  # 使用None来禁用异常上下文，这里except子句的异常将不出现最终的错误消息中

# ### raise语句（主动抛出异常）
# - 通过raise语句来引发一次异常；能够引发的错误或异常必须是直接或间接从属于Exception类的派生类；
# - 如果当前函数不知道如何处理某个异常，可以使用不带参数的raise语句继续往上抛，让上层调用者来处理；
# - raise语句如果不带参数，会把当前错误原样抛出；
#
# ### 异常上下文
# - 如果想在except子句中引发其他异常，可能会导致except子句的异常和其他异常都出现最终的错误消息中；
# - 可以使用raise...from...语句来提供自己的异常上下文，也可使用None来禁用上下文；
