#! python3
# -*- coding: utf-8 -*-


def lazy_sum(*args):
    def sum():  # 内部求和函数sum可以引用外部函数lazy_sum的参数和局部变量
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum  # 外部函数lazy_sum返回函数sum时，相关参数和变量都保存在返回的新函数中


f = lazy_sum(1, 3, 5, 7, 9)
print(f)  # 调用lazy_sum()时，返回的是求和函数，不是计算结果
print(f())  # 调用函数f时，计算求和的结果

f2 = lazy_sum(1, 3, 5, 7, 9)
print(f == f2)  # 每次调用都会返回一个新的函数，即使传入相同的参数


def count():  # 实现一个计算1x1、2x2、3x3的函数；
    fs = []
    for i in range(1, 4):
        def f(m=i):  # 因为函数只在执行时才去获取外层参数i, 所以这里利用默认参数在函数定义时获取i值
            return m * m

        fs.append(f)
    return fs


func1, func2, func3 = count()
print(func1(), func2(), func3())


# ### 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回;
# 注意：返回的函数不会立刻执行，而是直到被调用时才执行；
#
# ### 闭包（Closure）
# 内层函数引用了外层函数的参数或局部变量，然后返回内层函数，相关参数和变量都保存在返回的内层函数中，这种情况称为闭包（Closure）;
# 简而言之，就是当一个外部函数返回了一个内部函数后，外部函数的局部变量还被新函数（返回的内部函数）引用；
# 由于返回的函数引用了外层函数的局部变量，要确保引用的局部变量在函数返回后不能变;
