# -*- coding: utf-8 -*-
__author__ = 'Anliven'

i = 0
numbers = []
while i < 3:
    print ("At the top i is %d." % i),
    numbers.append(i)
    i += 1
    print ("Current: %r." % numbers), ("At the bottom i is %d" % i)
print ("The numbers: %r" % numbers)
for num in numbers:
    print (num),

# while-loop会一直执行代码段，直到对应的布尔表达式为False；
# 为了避免While循环永不结束，必须保证布尔表达式最终会变成False，需要仔细检查并验证

# for-loop --- 只能对一些东西的集合进行循环；在循环的对象数量固定或者有限的情况下使用；
# while-loop --- 可以对任何对象，但使用时注意事项较多；在循环永不停止时使用；
# 建议尽量少用while-loop，一般任务用for-loop更简易；
