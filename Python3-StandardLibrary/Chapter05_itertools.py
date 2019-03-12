# -*- coding: utf-8 -*-
import itertools

print(dir(itertools))

for per in itertools.permutations([1, 2, 3]):  # 所有可能的顺序，没有重复的元素
    print("permutations:", per)

for com in itertools.combinations([1, 2, 3], 2):  # 长度为2的元组，按排序顺序，没有重复的元素
    print("combinations", com)

co = itertools.count(10, 2.5)  # count()创建一个无限的数值迭代器，此时只是创建了一个迭代对象，没有在内存中创建无限多个元素
for i in co:  # 无限序列只有在for迭代时才开始执行无限迭代
    print("count:", i)
    if i == 15:
        break
print("takewhile:", list(itertools.takewhile(lambda x: x <= 30, co)))  # takewhile()根据条件判断来截取出一个有限的序列

cy = itertools.cycle("a bc")  # cycle()无限重复一个序列
for i in cy:
    print("cycle:", i)
    if i == 'c':
        break

re = itertools.repeat('A BC', 3)  # repeat()重复同一元素
for i in re:
    print("repeat:", i)

for i in itertools.chain('M N', 'X', range(3)):  # chain()串联迭代对象
    print("chain:", i)

for key, group in itertools.groupby('A BBCCc'):  # groupby()归类迭代器中相邻的重复元素
    print("groupby:", key, list(group))

for key, group in itertools.groupby('AaBbcCc', lambda c: c.upper()):
    print("groupby:", key, list(group))

# 循环嵌套
x_list = [1, 2, 3]
y_list = ['a', 'b']
z_list = ['A']
for x, y, z in itertools.product(x_list, y_list, z_list):
    print(x, y, z)

# for x in x_list:
#     for y in y_list:
#         for z in z_list:
#             print(x, y, z)

# ### 标准库itertools模块
# - Functions creating iterators for efficient looping
# - https://docs.python.org/3/library/itertools.html
# - 常用来扩展迭代器的使用；
