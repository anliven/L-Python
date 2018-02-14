#! python3
# -*- coding: utf-8 -*-


def str_swap(in_string):
    out_string = ""
    for letter in in_string:
        if 97 <= ord(letter) <= 122:  # ord():以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值或者Unicode数值；
            out_string += chr(ord(letter) - 32)  # chr():用一个范围0～255的整数作参数，返回一个对应的字符；
        elif 65 <= ord(letter) <= 90:
            out_string += chr(ord(letter) + 32)
        else:
            out_string = out_string + letter
    return out_string


print("Input a string :")
input_string = input()
print(str_swap(input_string))  # 利用ASCII码
print(input_string.swapcase())  # 利用string的swapcase方法

# 编写一个函数：反转输入字符串的大小写
