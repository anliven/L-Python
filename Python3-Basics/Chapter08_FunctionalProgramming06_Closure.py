# -*- coding: utf-8 -*-


def fnA(num):
    def fnB(val):
        return num * val

    return fnB  # 函数作为返回值


t = fnA(8)
print(t(9))


# 示例-1
def hello_conf(prefix):
    def hello(name):
        return prefix, name

    return hello


a = hello_conf('Good Morning!')
print(a.__name__, id(a))
print(a('AAA'))

b = hello_conf('Good Afternoon!')
print(b.__name__, id(b))
print(b('bbb'))


# 示例-2
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


# 示例-3
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
# 词法闭包（Lexical Closure）简称为闭包，是由函数和与其相关的引用环境组合而成的实体，也就是引用了自由变量的函数；
# 被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外；
# 简而言之，就是当一个外部函数返回了一个内部函数后，外部函数的局部变量还被新函数（返回的内部函数）引用；
# 确切的说，内层函数引用了外层函数的参数或局部变量，内层函数作为返回时，相关参数和变量都保存在返回的内层函数中；
# 由于返回的函数引用了外层函数的局部变量，要确保引用的局部变量在函数返回后不能变；
#
# ### 创建闭包必须满足的条件
# 当一个内嵌函数引用其外部作作用域的变量，就会得到一个闭包；
# - 必须有内嵌函数；
# - 内嵌函数必须引用外部函数中的变量；
# - 外部函数的返回值必须是内嵌函数；
#
# ### 闭包的作用
# 闭包是函数式编程的重要的语法结构和代码组织结构，可以提高代码的可重复使用性；
