#! python3
# -*- coding: utf-8 -*-

print("Please input 3 numbers : ")
a, b, c = input(), input(), input()
if a >= b:
    first = a
    second = b
else:
    first = b
    second = a

if c >= first:
    third = second
    second = first
    first = c
else:
    if c >= second:
        third = second
        second = c
    else:
        third = c
print(first, second, third)
print(third, second, first)

# 不使用列表或排序算法，对输入的三个整数数排序；
