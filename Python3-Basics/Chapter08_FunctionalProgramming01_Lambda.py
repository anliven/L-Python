# -*- coding: utf-8 -*-


def func(x):  # 显式定义函数
    return x * x


print(list(map(func, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # 调用自定义函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # 匿名函数lambda的形式


def multiply(x, y):
    return x * y


print(multiply(16, 18))

func1 = (lambda x, y: x * y)  # 匿名函数赋值给一个变量，再利用变量来调用该函数
print(func1)  # 此时func1是一个匿名函数对象
print(func1(16, 18))


def func2():
    return lambda x, y: x * y  # 匿名函数作为返回值返回


f = func2()  # 变量f指向函数，此时f是一个匿名函数对象
print(f)
print(f(16, 16))


# ### 匿名函数（lambda）
# lambda函数是一种快速定义单行的最小函数，可以用于任何需要函数的地方；
# 如果函数比较简单且复用性很低，可以省去显式定义函数的过程，将其简洁地定义为匿名函数，让代码更加精简；
# 使用lambda不需要考虑函数命名的问题；
# 用lambda关键字来创建匿名函数，语法格式："lambda arg1,arg2,...: expression"；
#
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数;
# lambda的主体是一个表达式，而不是一个代码块，只能在lambda表达式中封装有限的逻辑;
# 匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果;
