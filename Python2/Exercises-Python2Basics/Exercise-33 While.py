# -*- coding: utf-8 -*-
__author__ = 'Anliven'

i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num

# 在Python中如果某一行是以:（冒号colon）结尾，那就意味着接下来的内容是一个新的代码片段，新的代码片段是需要被缩进的。

# while-loop``（while 循环）会一直执行它下面的代码片段，直到它对应的布尔表达式为 False 时才会停下来。
# While 循环有一个问题，那就是有时它会永不结束。为了避免这样的问题，你需要遵循下面的规定：
#  1. 尽量少用 while-loop，大部分时候 for-loop 是更好的选择。
#  2. 重复检查 while 语句，确定测试的布尔表达式最终会变成 False 。
#  3. 如果不确定，就在 while-loop 的结尾打印出你要测试的值。看看它的变化。

#for-loop 和 while-loop 有何不同？
#for-loop 只能对一些东西的集合进行循环， while-loop 可以对任何对象进行驯化但使用时注意的地方较多。
#一般的任务用 for-loop 更容易一些。
