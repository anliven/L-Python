#! python3
# -*- coding: utf-8 -*-

listSample = [2 * x for x in range(3)]  # 使用列表解析来创建列表
print("listSample: ", listSample)
listSample2 = [m + n for m in 'ABC' for n in 'abc']  # 使用两层循环的列表解析来创建列表
print("listSample2: ", listSample2)

geneSample = (2 * x for x in range(3))  # 创建生成器geneSample：把一个列表生成式的[]改成()
print("geneSample: ", geneSample)
print(next(geneSample), next(geneSample), next(geneSample))  # 依次访问生成器前3个元素
# print(next(gene))  # 上一步已经遍历完成，再次调用next()会报StopIteration的错误

geneSample2 = (x * x for x in range(5))
for n in geneSample2:  # 通过for循环来迭代生成器
    print("x*x:", n)

geneSample3 = (x * x for x in range(5))
print("Type:", type(geneSample3))  # 生成器是迭代器，而迭代器是一次性的，不能重新加载，也就是说同一个迭代器对象无法多次迭代
print("Sum:", sum(geneSample3))
print("Sum:", sum(geneSample3))  # 内部工具(for循环、sum、min、max等)使用迭代器协议访问对象


def fib(x):  # 斐波拉契数列
    """
    :param x:
    """
    k, a, b = 0, 0, 1
    while k < x:
        yield b
        a, b = b, a + b
        k += 1


fibSample = fib(6)  # fibSample是生成器，斐波拉契数列的前6项
print("fibSample: ", fibSample)

print("Fib: ", next(fibSample))  # 输出斐波拉契数列的第1项
print("Fib: ", fibSample.__next__())  # 使用__next__()逐项访问，这里输出斐波拉契数列的第2项
print("Fib: ", fibSample.__next__())
print("Fib: ", next(fibSample))
print("Fib: ", next(fibSample))
print("Fib: ", next(fibSample))  # 输出斐波拉契数列的第6项
# print(next(fibSample))  # 生成器f只有6个元素，继续调用next()会提示错误StopIteration

for n in fib(6):  # 通过for循环来迭代生成器
    print("# fib: ", n)

# ### 列表解析（List Comprehensions）
# 运用列表解析可以直接快速生成list，也可以通过一个list推导出另一个list，而代码却十分简洁；
# 受到内存限制，列表容量是有限的，一个庞大的列表将占用很大的存储空间，很可能会造成浪费；
#
# ### 生成器（Generator）
# 利用生成器（实际上是某种算法）可以推导列表元素，就不用存储完整的列表，从而节省大量的存储空间；
# 生成器一般用来产生序列类型的值，可以在for循环中迭代，也可以通过next方法调用;
#
# ### 生成器的作用
# - 减少内存占用，例如可以使用迭代器方式打开文件；
# - 提高运行效率；
# - 延迟运行，仅当需要运行的地方才开始执行；
#
# ### 创建生成器的两种方法
# 1.把一个列表生成式的[]改成()，就创建了一个generator；
# 2.在函数代码中添加yield关键字
#
# ### yield关键字
# 如果一个函数定义中包含yield关键字，那么这个函数就是一个generator；
# 在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值;
# 并在下一次执行next()方法时从当前位置继续运行;
#
# ### 访问
# 生成器可以利用for循环访问，也可以利用next()执行一次访问；
# 使用for循环能够避免StopIteration错误，推荐使用；不建议也基本上永远不会使用next()方式；
#
# 通过for循环访问：集合类数据类型（列表等）、生成器和迭代器；
# 通过next()访问：迭代器和生成器；
