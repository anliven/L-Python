# -*- coding: utf-8 -*-
import heapq
import random

data = list(range(10))
random.shuffle(data)
print(data)

heap = []
for n in data:
    heapq.heappush(heap, n)  # 通过heapq.heappush()来创建堆
print(heap)

heapq.heappush(heap, 0.5)  #
print(heap)

heapq.heappop(heap)
heapq.heappop(heap)
print(heap)

heapq.heapreplace(heap, 8)  # 从堆中弹出最小的元素，再压入一个新元素
heapq.heapreplace(heap, 9)
print(heap)

heap2 = [6, 5, 3, 2, 1, 4, 0]
print(heap2)
heapq.heapify(heap2)  # 通过执行移位操作将普通列表转换成为合法的堆
print(heap2)

print(heapq.nlargest(3, heap2))
print(heapq.nsmallest(3, heap2))
print(heap2)

# ### 堆（Heap）
# 堆（Set）是一种优先序列，能够以任意顺序添加对象并随时找出并删除最小的元素；
# 比列表方法min的效率高；
#
# ### 标准库模块heapq
# - Heap queue algorithm
# - https://docs.python.org/3/library/heapq.html
# Python没有独立的堆类型，而是通过标准库模块heapq进行一些堆操作；
# 使用列表来表示堆对象本身；
#
# ### 堆特征（heap property）
# 堆中元素的排列顺序遵循：位置i处的元素总是小于位置“2*i”处和“2*i+1”处的元素；
# 位于索引0处的元素总是最小的元素；
#
# ### 常用方法
# - heapify(heap)：让列表具备堆特征，应在heappush和heappop之前使用；
# - heappush(heap, x)：将x压入堆中，此函只能用于使用堆函数创建的列表，不能用于普通列表；
# - heappop(heap)：从堆中弹出最小的元素（总是位于索引0处），并确保位于索引0处是最小的元素；
# - heapreplace(heap, x)：弹出最小的元素，并将x压入堆中；
# - nlargest(n, iter)：返回可迭代对象iter中的n个最大的元素；
# - nsmallest(n, iter)：返回可迭代对象iter中的个最小的元素；
# 相比使用函数sorted和切片，nlargest(n, iter)和nsmallest(n, iter)的速度更快，使用内存更少，也更直接；
