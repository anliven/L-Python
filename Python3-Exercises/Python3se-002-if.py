#! python3
# -*- coding: utf-8 -*-
from random import randint

a = randint(1, 1000)
b = randint(1, 1000)
c = randint(1, 1000)

print("There are 3 numbers : ", a, b, c)
print("Please select : (1)summary (2)average (X)exit :")
option = input()
if option == "1":
    print(a + b + c)
elif option == "2":
    print((a + b + c) / 5)
elif option == "X":
    print("None Selected!")
    exit()

# 实现菜单选项的功能：（1）求和、（2）求平均值、（X）退出；
