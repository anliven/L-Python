#! python3
# -*- coding: utf-8 -*-


def multiply(x, y):  # 显式定义一个求两数乘积的函数
    return x * y


print(multiply(16, 18))

func1 = lambda x, y: x * y  # 匿名函数实现"求两数乘积"，但PEP8不建议这样的写法
print(func1(16, 18))


def func2():
    return lambda x, y: x * y  # 匿名函数实现"求两数乘积"，并作为返回值返回


f = func2()  # ???
print(f(16, 16))

# 如果函数比较简单且复用性很低，可以将其简洁地定义为匿名函数，不需要显式定义；
# 用lambda关键字来创建匿名函数，语法格式："lambda arg1,arg2,...: expression"；
#
# 1.lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数;
# 2.lambda的主体是一个表达式，而不是一个代码块，只能在lambda表达式中封装有限的逻辑;
