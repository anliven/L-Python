# -*- coding: utf-8 -*-
import random

str1 = "AAA aaa,2018-12-31,2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22,2-01,2.01,2:16"
str2 = "BBB bbb,2017-12-31,2.59,2.11,2:11,2:23,3-10,2-23,3:10,3.21,3-21,3.01,3.02,2:59"
str3 = "CCC ccc,2016-12-31,2:22,3.01,3:01,3.02,3:02,3.02,3:22,2.49,2:38,2:40,2.22,2-31"


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    mins, secs = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(in_str):  # 字符串转换为字典
    try:
        temp_list = in_str.strip().split(',')
        return ({'Name': temp_list.pop(0),
                 'Age': temp_list.pop(0),
                 'Times': str(sorted(set([sanitize(t) for t in temp_list]))[0:3])})
    except TypeError as typeerr:
        print('Type error: ' + str(typeerr))
        return (None)


print(get_coach_data(str1)['Name'] + "'s fastest times are: " + get_coach_data(str1)['Times'])
print(get_coach_data(str2)['Name'] + "'s fastest times are: " + get_coach_data(str2)['Times'])
print(get_coach_data(str3)['Name'] + "'s fastest times are: " + get_coach_data(str3)['Times'])

# 将字典当做“分支语法结构”来使用
x = random.randint(10, 100)
y = random.randint(1, 10)
operator = {"+": x + y,  # 值可以存储表达式
            "-": x - y,
            "*": x * y,
            "/": x / y}
op_list = list(operator.keys())
o = random.choice(op_list)
# print(x, o, y, "=", operator[o])
print(x, o, y, "=", operator.get(o, "Operator must be +|-|*|/"))  # 对比了解get()的用法

# ### get方法
# - 方法get可以访问字典项；
# - 如果字典包含指定的键，get的作用与普通字典查找相同；
# - 如果访问不存在的键时，不会引发异常，而是默认返回None；
