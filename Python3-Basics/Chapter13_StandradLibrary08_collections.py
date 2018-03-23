#! python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from collections import deque
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
po = Point(111, 222)
print(po.x, po.y)
print(isinstance(po, tuple))  # 验证创建的对象是否是tuple的子类

tl = ['a', 'b', 'c']
de = deque(tl)
de.pop()
de.append('x')
de.appendleft('y')
de.popleft()
print(de)

d = dict(a=555, bbb=444, ddd=222, c=333)
d['e'] = 111
print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))  # dictionary sorted by key
print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))  # dictionary sorted by value
print(OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))))  # dictionary sorted by length of the key string

co = Counter()  # 计数器
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    co[word] += 1
print(co)

co_2 = Counter()
for ch in 'Core Python programming':
    co_2[ch] += 1
print(co_2)
print(co_2.most_common(3))

# ### 标准库collections模块
# - Container datatypes
# - 官方文档：https://docs.python.org/3/library/collections.html
#
# ### 一些方法
# namedtuple(): 用来创建一个自定义的tuple对象（具备tuple的不变性），并规定tuple元素的个数，并可以用属性引用tuple的某个元素;
# deque(): list是线性存储，数据量大的时候，插入和删除效率很低，利用deque()可以高效实现插入和删除操作的双向列表，适合用于队列和栈：
# OrderedDict(): dict是无序的，利用OrderedDict()可以对dict排序；
# Counter(): A Counter is a dict subclass for counting hashable objects.
