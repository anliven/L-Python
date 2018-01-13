#! python3
# -*- coding: utf-8 -*-

listSample = [2 * x for x in range(3)]  # 创建列表
print("listSample: ", listSample)

geneSample = (2 * x for x in range(3))  # 创建生成器：把一个列表生成式的[]改成()
print("geneSample: ", geneSample)
print(next(geneSample), next(geneSample), next(geneSample))  # 依次访问生成器前3个元素
# print(next(gene))  # 上一步已经遍历完成，再次调用next()会报StopIteration的错误


def fib(x):
    """
    :param x:
    """
    n, a, b = 0, 0, 1
    while n < x:
        yield b
        a, b = b, a + b
        n += 1


fibSample = fib(6)  # f是生成器，斐波拉契数列的前6项
print("fibSample: ", fibSample)

print(next(fibSample))  # 输出斐波拉契数列的第1项
print(next(fibSample))
print(next(fibSample))
print(next(fibSample))
print(next(fibSample))
print(next(fibSample))  # 输出斐波拉契数列的第6项
# print(next(fibSample))  # 生成器f只有6个元素，继续调用next()会提示错误StopIteration


# ### 生成器（Generator）
# 利用生成器（实际上是某种算法）可以推导列表元素，就不用存储完整的列表，从而节省大量的空间；
#
# ### 创建生成器的两种方法
# 1.把一个列表生成式的[]改成()
# 2.在函数代码中添加yield关键字
#
# ### yield关键字???
# 在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值;
# 并在下一次执行next()方法时从当前位置继续运行;
#
# ### 访问
# 生成器可以利用for循环访问，也可以利用next()执行一次访问；
# 通过for循环访问：集合类数据类型（列表等）、生成器和迭代器；
# 通过next()访问：迭代器和生成器；

# for循环访问生成器???
