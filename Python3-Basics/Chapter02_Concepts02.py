#! python3
# -*- coding: utf-8 -*-


def is_palindrome(text):  # 判断是否是回文
    text2 = text[::-1]
    return text == text2


something = input("Enter text: ")  # Python交互式命令行：标准键盘输入
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

# ### 用户交互
# - input()函数与print()函数分别实现与用户的交互，完成输入与输出；
# - 使用str类的方法可以操作输入的内容，可通过help(str)了解更多信息；
#
# ### 标准键盘输入
# 内置函数input()来实现标准键盘输入。input()可以接收一行文本，并将返回该文本；
#
# ### 标准输出
# 内置函数print()来实现标准输出；
# print()函数默认会换行，可以使用语法print(str,end='')实现不换行输出；
