#! python3
# -*- coding: utf-8 -*-

x = 1  # 初始值
Diff = 3  # 差值
Num = 1  # 数目
Sum = 1  # 相加之和

while Num < 100:
    x += Diff
    Num += 1
    Sum += x

print("Sum: ", Sum)

# 计算等差数列“1 4 7 10 13 16 19 ...”前 100 项的和;
