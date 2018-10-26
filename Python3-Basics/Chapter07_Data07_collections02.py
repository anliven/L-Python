# -*- coding: utf-8 -*-
from collections import deque

q = deque(range(5))
print("Deque: ", q)

q.append(5)
q.appendleft(6)
print("Deque: ", q)

q.pop()
q.popleft()
print("Deque: ", q)

q.extend([7, 8])
q.extendleft([9, 10, 11])  # 参数是可迭代对象，其中的元素将按相反的顺序出现在双端队列中
print("Deque: ", q)

q.rotate(3)  # 将双端队列的元素向右移位
print("Deque: ", q)
q.rotate(-1)  # 将双端队列的元素向左移位
print("Deque: ", q)

# ### 双端队列
# 双端队列可以高效地进行如下操作：
#   - 在队首（左端）附加和弹出元素；
#   - 旋转元素（将元素向左或向右移位，并在到达一端时环绕到另一端）
# 使用collections模块的deque类型可实现双端队列；
