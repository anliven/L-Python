#! python3
# -*- coding: utf-8 -*-

print("Input a number between 1 and 100: ")
try_number = int(input())
while try_number > 100 or try_number < 1:
    print("Wrong Number! Input a number between 1 and 100: ")
    try_number = int(input())
print("Right Number!")

# 输入一个1和100之间的整数，如果满足条件显示成功并退出，否则显示错误并提示输入，直到满足条件为止;
