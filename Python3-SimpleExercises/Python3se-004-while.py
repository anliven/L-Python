#! python3
# -*- coding: utf-8 -*-

try_number = int(input("please input a number between 1 and 100:"))
while try_number > 100 or try_number < 1:
    print("It's wrong.")
    try_number = int(input("please input a number between 1 and 100:"))
print("Right!")

# 输入一个100以内正整数，满足条件显示成功并退出，否则提示再次输入，直到满足条件为止；
