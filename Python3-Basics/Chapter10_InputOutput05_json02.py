# -*- coding: utf-8 -*-
import json
from datetime import date
from datetime import datetime


class Student(object):  # 自定义数据类型
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return 'Student [name: %s, age: %d, score: %d]' % (self.name, self.age, self.score)


def stu2dict(std):  # 自定义数据类型的序列化转换函数
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2stu(std):  # 自定义数据类型的反序列化转换函数
    return Student(std['name'], std['age'], std['score'])


test_data = Student('AAA', 23, 99)
print("New Data Type: ", test_data)
# print(json.dumps(test_data))  # 自定义数据类型默认不能直接json序列化，会引发TypeError错误

print(json.dumps(test_data, default=stu2dict))
print(json.dumps(stu2dict(test_data)))  # 序列化的转换过程：“Python对象 --> dict --> JSON object”
print(json.dumps(test_data, default=lambda obj: obj.__dict__))

test_data2 = '{"name": "BBB", "age": 22, "score": 88}'
print(json.loads(test_data2, object_hook=dict2stu))  # object_hook函数将dict转换为Python对象
print(dict2stu(json.loads(test_data2)))  # 反序列化的转换过程：“JSON object -> dict --> Python对象”


class MyJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


test_data3 = datetime.now()
print("DateTime Type: ", test_data3)
# print(json.dumps(test_data3))  # datetime类型数据默认不能直接json序列化，会引发TypeError错误
print(json.dumps(test_data3, cls=MyJsonEncoder))

# ### 自定义数据类型
# 实现自定义数据类型的序列化与反序列化有两种方式：
# - 编写转换函数；
# - 继承JSONEncoder和JSONDecoder类；
