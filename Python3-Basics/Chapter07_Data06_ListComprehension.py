#! python3
# -*- coding: utf-8 -*-

r = range(0, 4)  # 生成列表[0,1,2,3]
for x in r:  # 利用for循环来访问
    print(x)

print("List : ", list(range(0, 6, 2)))  # 利用list()将range转为列表对象
print("Tuple : ", tuple(range(2, 9, 3)))  # 利用tuple()将range转为元组对象


def func(i):
    """
    :param i:
    :return:
    """
    return i * i


# 列表解析（List Comprehension）
sampleList1 = [1, 2, 3, 4]
print("new list: ", [func(x) for x in sampleList1])  # 使用列表解析产生新列表
print("old list: ", sampleList1)  # 原始列表保持不变

sampleList2 = ["AAA", "bbb", "CCC"]
print("new list: ", [x.lower() for x in sampleList2])  # 将所有的字符串变成小写
print("old list: ", sampleList2)

listOne = [1, 2, 3, 4, 5]
listTwo = [2 * i for i in listOne if i > 2]  # 直接使用表达式;增加判断条件
print('list_1:', listOne)
print('list_2:', listTwo)
print('list_3:', [(x + 1, y + 1) for x in range(3) for y in listOne])  # 多个for循环嵌套
print('list_x:', [j for i in listOne for j in range(i * 2, 20, i)])  # 复杂示例
print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))  # 复杂示例：1000以内所有是3和5倍数的自然数之和

words = "this is a test!".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]  # 复杂示例
# stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)  # 对应的map()实现
for i in stuff:
    print(i)

# 列表生成（List Generation）
list_g = (func(x) for x in sampleList1)
print(type(list_g), list_g)  # 对比查看类型信息
list_g2 = []
for i in list_g:
    list_g2.append(i)
print(type(list_g2), list_g2)  # 对比查看类型信息

# ### range() 函数
# 内置range()函数可以生成一个规律的整数序列，一般用在for循环中；
# 语法格式： range(start,end[,step])；
# start：起始下标（可选），默认为0；end：终止下标；step：步长（可选），默认为1；
# 特别注意：下标的实际有效范围是“前开后闭”的，也就是不包括终止下标的元素。
#
# 可以使用列表解析和生成表达式操作和处理一个序列（或其他的可迭代对象）来创建一个新的列表；
#
# ### 列表解析（List Comprehension）
# 也称为列表推导，是一种从其它列表来创建新列表的方式；
# 适用于根据旧表建立新表的场景（也就是必须对原列表的每一项就进行转换），有效减少代码数量；
# 列表解析表达式为：
# - [expr for iter_var in iterable]
# - [expr for iter_var in iterable if cond_expr]
# 如果表达式expr较为复杂，可以使用预先定义的function()
# 特别注意：
# - 列表解析可以转换为for循环或者map表达式；
# - 实现相同功能，列表解析的性能比map好，更为简单明了，for循环效率最差；
#
# ### 列表生成（List Generation）
# 当序列过长， 而每次只需要获取一个元素时，应当考虑使用生成器表达式；
# 列表生成器表达式为：
# - (expr for iter_var in iterable)
# - (expr for iter_var in iterable if cond_expr)
# 如果表达式expr较为复杂，可以使用预先定义的function()；
# 特别注意：
# - 生成器表达式是被（）括起来的，而不是[]；
# - 生成器表达式使用“惰性计算”，并不真正创建列表，而是返回一个生成器，只有在检索时才被赋值；
# - 适用在列表较长而每次只需要获取一个元素的情况，节省内存；
#
# ### 其它
# 类似sorted()的方法是对整个列表的排序操作，不是针对列表中的单个数据项，因此不能在列表推导中使用；
