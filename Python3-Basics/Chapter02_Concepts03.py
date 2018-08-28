# -*- coding: utf-8 -*-
import sys
import os


def is_palindrome(text):  # 判断是否是回文
    text2 = text[::-1]
    return text == text2


something = input("Enter text: ")  # Python交互式命令行：标准键盘输入
# print(type(something))  # 内置函数type()查看对象类型
if is_palindrome(something):
    print("Yes, it is a palindrome.")
    with open("test.log", "w") as f:
        print("Yes, it is a palindrome.", file=f)
else:
    print("No, it is not a palindrome.", file=sys.stderr)

os.remove("test.log")

# ### input()与print()
# 使用内置input()函数与print()函数可以分别实现输入与输出；
# - input()：实现标准键盘输入，可以接收一行文本并返回该文本(注意：返回的是str类型)；
# - print()：实现打印输出，可通过file参数指定输出流；
