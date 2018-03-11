#! python3
# -*- coding: utf-8 -*-

# Solution - 1 - proposal
print(2 ** 38)

# Solution - 2
print(pow(2, 38))

# Solution - 3
k = 1
for i in range(1, 39):
    k *= 2
print(k)

# Solution - 4
count = 1
n = 38
while n > 0:
    count *= 2
    n -= 1
print(count)

# Solution Link : http://www.pythonchallenge.com/pcc/def/map.html
