#! python3
# -*- coding: utf-8 -*-


def format_name(s):
    return s[:1].upper() + s[1:].lower()


print(list(map(format_name, ['aaa', 'BBB', '1CC', '2dd', '333'])))

# 将一个list所有元素的首字母大写；
