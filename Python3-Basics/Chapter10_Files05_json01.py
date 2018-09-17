# -*- coding: utf-8 -*-
import json

test_data = dict(name='测试', age=29, sex="男")
print("json.dumps: ", json.dumps(test_data, indent=4, ensure_ascii=False))  # indent参数：格式化保存，默认为None(零个空格)

test_data2 = [{'name': '开发', 'age': 30, 'sex': '男'}, {'name': '运维', 'age': 28, 'sex': '女'}]
with open("test.json", "w", encoding='utf-8') as f:
    json.dump(test_data2, f, sort_keys=True, indent=4, ensure_ascii=False)  # sort_keys参数：是否对dict的key进行排序

with open("test.json", "r", encoding='utf-8') as f:
    print("json.dump: ", f.read())
    f.seek(0)
    aaa = json.loads(f.read())
    f.seek(0)
    bbb = json.load(f)
print("json.loads: ", aaa)
print("json.load: ", bbb)

# ### JSON
# JSON(JavaScript Object Notation, JS对象标记) 是一种轻量级的数据交换格式，相对于XML而言，更加简洁、易于读写，也易于解析和生成；
# 采用完全独立于编程语言的文本格式来存储和表示数据，表示出来就是一个字符串，可以被所有语言读取，易于存储和通过网络传输；
# JSON编码是UTF-8，所以总是能正确地在Python的str与JSON字符串之间转换;
#
# ### 标准库json模块
# https://docs.python.org/3/library/json.html;
# 内置json模块可以完成Python对象和JSON格式之间的转换；
# - json.dumps()：无文件操作；将Python对象转换成json字符串；
# - json.dump()：序列化并写入文件；必须传文件描述符，直接将Python对象转换成json字符串并存储到文件中；
# - json.loads()：无文件操作；将json字符串转换成Python对象，也就是json字符串反序列化；
# - json.load()：读文件并反序列化；只接收文件描述符，从指定文件中读取json字符串并反序列化;
#
# ### 中文编码
# 在dumps()或dump()函数中设置“ensure_ascii=False”参数，可以避免在序列化时中文被转换为unicode码；
