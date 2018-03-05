#! python3
# -*- coding: utf-8 -*-
import sys

print("Input your numbers and spaces are used between numbers: ")
in_numbers = list(map(int, sys.stdin.readline().split()))
print(sorted(in_numbers))
print(sorted(in_numbers, reverse=True))

# 对输入的整数进行正向和逆向排序；
