# -*- coding: utf-8 -*-

SL = [[1, 2], [3, 4], [5]]
SL2 = ['AAA', ['BBB', ['CCC']]]


def func(obj):
    for sublist in obj:
        for element in sublist:
            yield element  # 包含yield语句的函数


g = func(SL)
print(type(g), g)
for num in g:  # 对生成器进行迭代
    print(num)
print(list(func(SL)))  # 对生成器进行迭代

g2 = (i ** 2 for i in range(10, 20))  # 使用圆括号创建生成器推导
print(next(g2))
print(sum(i ** 2 for i in range(10, 20)))  # 直接在一对既有的圆括号内（如在函数调用中），无需再添加一对圆括号


def func2(obj):
    try:
        try:
            obj + ''  # 如果对象不是字符串或类似字符串对象，将引发TypeError异常
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in obj:
            for element in func2(sublist):
                yield element
    except TypeError:
        yield obj  # 基线条件：函数展开


print(list(func2(SL2)))
for i in func2(SL2):
    print(i)

# ### 生成器（Generator）与yield
# 生成器是包含yield语句的函数，可以生成多个值，每次一个；
# 每次使用yield生成一个值后，函数都将冻结（再次等待停止执行），等待被重新唤醒，被重新唤醒后，函数将从停止的地方开始继续执行；
#
# ### 生成器推导（生成器表达式）
# 必须使用圆括号来创建，其工作原理与列表推导相同，但返回的是一个逐步执行计算的迭代器；
#
# ### 递归式生成器
# 使用递归来处理任意层嵌套的列表；
