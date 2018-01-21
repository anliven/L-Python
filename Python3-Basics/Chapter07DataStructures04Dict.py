#! python3
# -*- coding: utf-8 -*-

testDict = {
    'AAA': '11111',
    'BBB': '22222',
    'CCC': '33333',
    'DDD': '44444'
}

print(testDict)
print(testDict.keys())  # 输出所有的键，返回一个列表
print(testDict.values())  # 输出所有的值，返回一个列表
print("AAA's value is", testDict['AAA'])  # 注意：返回元素而不是列表，所以返回值没有中括号

print("AAA" in testDict)  # 通过in判断key是否存在
print(testDict.get('EEE', 'No key!'))  # 通过dict提供的get()方法，如果key不存在，可以返回None，或者自定义的value；

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

a = "abc"  # str是不可变对象；b本身是一个变量，它指向的对象内容是'abc'，'abc'才是字符串对象！
print(a)
print("method calls and call returns: ", a.replace("a", "A"))  # replace方法创建一个新字符串并返回，并没有改变原字符串的内容
print(a)  # 变量a仍指向原有的字符串

b = ['c', 'b', 'a']  # list是可变对象
print(b)
print("method calls and call returns: ", b.sort())  # sort方法改变原字符串的内容，没有返回值
print(b)

# ### 字典（Dictionary）
# - 字典将键（Keys）与值（Values）联立到一起，其中键必须是唯一的；
# - 使用花括号{}声明字典；键与值之间使用冒号分隔，每一对键与值用逗号区分；
# - 字典当中的元素是通过键来访问的，只能使用不可变的对象作为字典的键；
# - 字典是无序的对象集合，内部存放的顺序和key放入的顺序无关，而且字典中的键值对不会以任何方式进行排序；
# 特别注意：ict的key必须是不可变对象，不可变的字符串和整数等可以作为key，而list是可变的，就不能作为key；
#
# ### 不可变对象
# 不可变对象调用对象自身的方法，不会改变该对象自身的内容，而是创建新的对象并返回，这样就保证了不可变对象本身永远不可变；
# 可变对象调用对象自身的方法，会改变该对象自身的内容；
#
# ### 避免key不存在的错误
# - 通过in判断key是否存在；
# - 通过dict提供的get()方法，如果key不存在，可以返回None，或者自定义的value；
#
# ### 字典常用方法
# - 增加新键值对可以通过使用索引运算符访问一个键值并为其分配与之相应的值；
# - del语句删除某一键值对；
# - item方法访问字典中的每一个键值对信息，将返回一份包含元组（相应的键值对信息）的列表；
# - 使用in运算符来检查某对键值—值配对是否存在；
# - help(dict)获取dict类的更多信息；
#
# ### Dict与List对比
# Dict
# - 查找和插入的速度极快，不会随着key的增加而变慢；
# - 需要占用大量的内存，内存浪费多；
# List
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少；
