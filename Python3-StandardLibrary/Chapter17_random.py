# coding=utf-8
import random
import time
import pprint

# 示例-1：获取时间段的某一时间
date1 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = time.mktime(date1)
date2 = (2018, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = time.mktime(date2)
random_time = random.uniform(time1, time2)
print(time.asctime(time.localtime(random_time)))

# 示例-2: 扑克发牌
values = list(range(1, 11)) + "Jack Queen King".split()
suits = "diamonds clubs hearts spades".split()
deck = ["{} of {}".format(v, s) for v in values for s in suits]
random.shuffle(deck)
pprint.pprint(deck[:6])
print("# Start conveying a card: ")
while deck:
    input(deck.pop())  # 按一次回车发一张牌

# ### 标准库random模块
# - Generate pseudo-random numbers
# - 官方文档：https://docs.python.org/3/library/random.html
#
# ### 一些常用的函数
# - random()：返回一个0~1（包含1）的随机实数
# - getrandbits(n)：以长整数方式返回n个随机的二进制位
# - uniform(a, b)：返回一个a~b（包含b）的随机实数
# - randrange([start], stop, [step])：从range([start], stop, [step])中随机选择一个数
# - choice(seq)：从序列seq中随机选取一个元素
# - shuffle(seq[, random])：就地打乱序列seq
# - sample(seq, n)：从序列seq中随机选择n个不同的元素
