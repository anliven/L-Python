#! python3
# -*- coding: utf-8 -*-


def toUppers(L):
    return [x.upper() for x in L if type(x) == str]


print(toUppers(['Hello', 'world', 101]))

# 编写一个函数：接受一个list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略;
