# -*- coding: utf-8 -*-
import collections
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque
from collections import OrderedDict

print(dir(collections))

a = Counter('blue')
b = Counter('yellow')
print(a)
print(b)
print("Most common top-3:", (a + b).most_common(3))

c = Counter()  # 计数器
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    c[word] += 1
print(c)

d = Counter()
for ch in 'Core Python programming':
    d[ch] += 1
print(d)
print(d.most_common(3))

my_dict = defaultdict(lambda: 'DefaultValue')  # defaultdict()动态创建不存在的属性
my_dict['a'] = 123
print(my_dict['a'], my_dict['b'], my_dict['c'])

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

dic = dict(a=555, bbb=444, ddd=222, c=333)
dic['e'] = 111
print(OrderedDict(sorted(dic.items(), key=lambda t: t[0])))  # dictionary sorted by key
print(OrderedDict(sorted(dic.items(), key=lambda t: t[1])))  # dictionary sorted by value
print(OrderedDict(sorted(dic.items(), key=lambda t: len(t[0]))))  # dictionary sorted by length of the key string

# ### 标准库collections模块
# - Container datatypes
# - https://docs.python.org/3/library/collections.html
# - 主要用来扩展容器相关的数据类型；
#
# ### 一些方法
# namedtuple(): 用来创建一个自定义的tuple对象（具备tuple的不变性），并规定tuple元素的个数，并可以用属性引用tuple的某个元素；
# deque(): list是线性存储，数据量大的时候，插入和删除效率很低，利用deque()可以高效实现插入和删除操作的双向列表，适合用于队列和栈；
# OrderedDict(): dict是无序的，利用OrderedDict()可以对dict排序；
# Counter(): A Counter is a dict subclass for counting hashable objects；
