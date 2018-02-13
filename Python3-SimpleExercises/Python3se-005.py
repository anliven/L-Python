#! python3
# -*- coding: utf-8 -*-


def str_swap1(string):
    return string.swapcase()


def str_swap2(in_string):
    out_string = ""
    for letter in in_string:
        if 97 <= ord(letter) <= 122:
            out_string += chr(ord(letter) - 32)
        elif 65 <= ord(letter) <= 90:
            out_string += chr(ord(letter) + 32)
        else:
            out_string = out_string + letter
    return out_string


input_string = input('Input a string :')
print(str_swap1(input_string))
print(str_swap2(input_string))

# 编写函数：反转字符串的大小写；
