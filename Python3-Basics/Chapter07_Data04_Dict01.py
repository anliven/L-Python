# -*- coding: utf-8 -*-

new_d1 = {}  # 创建空字典，使用{}或工厂函数dict()可以创建一个空字典
new_d2 = dict()  # 创建空字典
print("Dict1:", new_d1, "Dict2:", new_d2)
new_d3 = dict(aaa=333, ccc=333, bbb=111)  # 创建字典
new_d4 = dict([("abc", "123"), ('def', 456)])  # 从其它映射或键值对序列创建字典
print("Dict3:", new_d3, "Dict4:", new_d4)

testDict = {  # 创建字典
    'AAA': '11111',
    'BBB': '22222',
    'CCC': '33333',
    'DDD': '44444'
}

print(testDict)
print(testDict.items())  # 返回整个字典列表
print(testDict.keys())  # 输出所有的键，返回一个列表
print(testDict.values())  # 输出所有的值，返回一个列表

print("AAA's value is", testDict['AAA'])  # 注意：返回元素而不是列表，所以返回值没有中括号
print("AAA" in testDict)  # 通过in判断key是否存在
print(testDict.get('EEE', 'No key!'))  # 通过dict提供的get()方法，如果key不存在，可以返回None，或者自定义的value；

print("AAA's number is {AAA}.".format_map(testDict))  # 将字符串格式设置用于字典
template = """
<html>
    <head>
        <title>{CCC}</title>
    </head>
    <body>
        <h1>{BBB}</h1>
        <p>{AAA}</p>
    </body>
</html>
"""
print(template.format_map(testDict))

del testDict['DDD']  # 删除键值对
testDict.pop('CCC')  # pop(key)方法删除键值对
print('There are {} contacts in the testDict.'.format(len(testDict)))

for key, value in testDict.items():  # 遍历字典
    print('{} - {}'.format(key, value))

testDict['EEE'] = '55555'  # 添加键值对
if 'EEE' in testDict:
    print("EEE-value is", testDict['EEE'])

testDict['BBB'] = '77777'  # 重新赋值；一个key只能对应一个value，所以多次对同一个key赋值，以最后的赋值为准
print("BBB-value is", testDict['BBB'])

x, y, z = testDict  # 拆包字典时，将会得到键，而不是键值对
print("x - {}, y - {}, z - {}".format(x, y, z))
part, *rest = testDict
print("*rest -", *rest)

a = "abc"  # str是不可变对象；b本身是一个变量，它指向的对象内容是'abc'，'abc'才是字符串对象！
print(a)
print("method calls and call returns: ", a.replace("a", "A"))  # replace方法创建一个新字符串并返回，并没有改变原字符串的内容
print(a)  # 变量a仍指向原有的字符串

b = ['c', 'b', 'a']  # list是可变对象
print(b)
print("method calls and call returns: ", b.sort())  # sort方法改变原字符串的内容，没有返回值
print(b)

newDict = {'AAA': '123', 'BBB': '456', 'CCC': [777, 888, 999]}
newDict2 = newDict.copy()  # 浅复制
newDict2['AAA'] = 111
newDict2['CCC'].remove(777)  # 需特别注意此结果
print(newDict)
print(newDict2)

print(dict.fromkeys(['aaa', 'bbb'], ('unknown', 'test')))  # 创建一个包含指定键的新字典（所有键值默认都为None）

newDict3 = {'aaa': 123, 'bbb': 456}
newDict4 = {'aaa': "AAA", 'bbb': 456, 'ccc': 789}
newDict3.update(newDict4)  # 使用一个字典中的项来更新另一个字典；
print(newDict3)

# ### 字典（Dictionary）
# - 等同于其他编程语言中的“映射”、“散列”、“关联数组”等；
# - 字典将键（Keys）与值（Values）联立到一起，其中键必须是唯一的；
# - 使用花括号{}声明字典；键与值之间使用冒号分隔，每一对键与值用逗号区分；
# - 字典当中的元素是通过键来访问的，只能使用不可变的对象（例如字符串、元组、实数）作为字典的键；
# - 字典是无序的对象集合，内部存放的顺序和key放入的顺序无关，而且字典中的键值对不会以任何方式进行排序；
# 特别注意：ict的key必须是不可变对象，不可变的字符串和整数等可以作为key，而list是可变的，就不能作为key；
#
# ### dict()
# https://docs.python.org/3/library/functions.html#func-dict
# 内置函数dict()用来创建一个新字典；
#
# ### 不可变对象
# 不可变对象调用对象自身的方法，不会改变该对象自身的内容，而是创建新的对象并返回，这样就保证了不可变对象本身永远不可变；
# 可变对象调用对象自身的方法，会改变该对象自身的内容；
#
# ### 避免key不存在的错误
# - 使用in运算符来检查某对键值—值配对是否存在；；
# - 通过dict提供的get()方法，如果key不存在，可以返回None，或者自定义的value；
#
# ### 一些常用方法
# - 增加新键值对可以通过使用索引运算符访问一个键值并为其分配与之相应的值；
# - items：返回一个包含整个字典项的字典视图（列表中每个元素都为(key, value）形式）；
# - keys：返回一个包含所有键的字典视图；
# - values：返回一个包含所有值的字典视图；
# - del：删除某一键值对；
# - pop：获取指定键的值，并将此键值对从字典中删除；
# - popitem: 随机弹出一个字典项；
# - clear：就地删除所有字典项；
# - copy：返回一个字典，包含的键值对与原字典相同（浅复制，没有真正建立副本）；
# - fromkeys：创建一个包含指定键的新字典（所有键值默认都为None）；
# - setdefault：指定的键存在时，返回其值，并保持字典不变；如果指定的键不存在，就返回并添加指定的键值对到字典中；
# - update：使用一个字典中的项来更新另一个字典；
# - help(dict)获取dict类的更多信息；
#
# ### Dict与List对比
# Dict
#   - 查找和插入的速度极快，不会随着key的增加而变慢；
#   - 需要占用大量的内存，内存浪费多；
# List
#   - 查找和插入的时间随着元素的增加而增加；
#   - 占用空间小，浪费内存很少；
