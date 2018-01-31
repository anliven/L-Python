#! python3
# -*- coding: utf-8 -*-

import json

d = dict(name='AAA', age=11, score=99)
print(json.dumps(d))

json_str = '{"name": "BBB", "age": 22, "score": 88}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('CCC', 23, 77)

print(json.dumps(s, default=student2dict))  # Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(std):
    return Student(std['name'], std['age'], std['score'])


print(json.loads(json_str, object_hook=dict2student))  # JSON反序列化为一个Student对象实例
# loads()方法首先转换出一个dict对象，然后传入的object_hook函数负责把dict转换为Student实例

# ### JSON
# JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式；
# 采用完全独立于编程语言的文本格式来存储和表示数据，表示出来就是一个字符串，可以被所有语言读取，也易于存储和通过网络传输；
# JSON编码是UTF-8，所以总是能正确地在Python的str与JSON字符串之间转换;
#
# ### json模块
# 内置json模块可以完成Python对象和JSON格式之间的转换；
# dumps()方法返回一个标准JSON的str，dump()方法直接把JSON写入一个file-like Object；
# loads()方法把JSON的字符串反序列化，load()方法从file-like Object中读取字符串并反序列化;
#
# ### 定制JSON序列化
# 默认情况下，dumps()方法无法将class的实例对象变为一个JSON的对象；
# 利用dumps()方法的可选参数default，可以把任意一个对象变成一个可序列为JSON的对象；
# dumps()的可选参数：https://docs.python.org/3/library/json.html#json.dumps
