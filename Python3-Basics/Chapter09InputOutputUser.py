# -*- coding: utf-8 -*-


def reverse(text):
    return text[::-1]


def is_palindrome(text):  # 判断是否是回文
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

# ### 用户交互
# - input()函数与print()函数分别实现与用户的交互，完成输入与输出；
# - 使用str类的方法可以操作输入的内容，可通过help(str)了解更多信息；
