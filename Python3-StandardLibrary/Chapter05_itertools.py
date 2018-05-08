#! python3
# -*- coding: utf-8 -*-
import itertools

co = itertools.count(10, 2.5)  # count()创建一个无限的数值迭代器，此时只是创建了一个迭代对象，没有在内存中创建无限多个元素
for i in co:  # 无限序列只有在for迭代时才开始执行无限迭代
    print("co:", i)
    if i == 15:
        break
print(list(itertools.takewhile(lambda x: x <= 30, co)))  # 通过takewhile()等函数根据条件判断来截取出一个有限的序列

cy = itertools.cycle("a bc")  # cycle()无限重复一个序列
for i in cy:
    print("cy:", i)
    if i == 'c':
        break

re = itertools.repeat('A BC', 3)  # repeat()重复同一元素
for i in re:
    print("re:", i)

for i in itertools.chain('M N', 'XY'):  # chain()串联迭代对象
    print("ch:", i)
    if i == 'Z':
        break

for key, group in itertools.groupby('A BBCCc'):  # groupby()归类迭代器中相邻的重复元素
    print("gr:", key, list(group))

for key, group in itertools.groupby('AaBbcCc', lambda c: c.upper()):
    print("gr:", key, list(group))

# ### 标准库itertools模块
# - Functions creating iterators for efficient looping
# - 官方文档：https://docs.python.org/3/library/itertools.html
