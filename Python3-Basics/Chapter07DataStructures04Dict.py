#! python3
# -*- coding: utf-8 -*-

testDict = {
    'AAA': '11111',
    'BBB': '22222',
    'CCC': '33333',
    'DDD': '44444'
}

print(testDict.keys())  # 输出所有的键，返回一个列表
print(testDict.values())  # 输出所有的值，返回一个列表
print("AAA's value is", testDict['AAA'], end=' ')  # 注意：返回元素而不是列表，所以返回值没有中括号

del testDict['DDD']  # 删除键值对
print('\nThere are {} contacts in the testDict.'.format(len(testDict)))

for key, value in testDict.items():  # 遍历字典
    print('{} - {}'.format(key, value))

testDict['EEE'] = '55555'  # 添加键值对
if 'EEE' in testDict:
    print("EEE-value is", testDict['EEE'])

testDict['CCC'] = '77777'  # 修改键值对的值
print("CCC-value is", testDict['CCC'])

# ### 字典（Dictionary）
# - 字典将键（Keys）与值（Values）联立到一起，其中键必须是唯一的；
# - 使用花括号{}声明字典；键与值之间使用冒号分隔，每一对键与值用逗号区分；
# - 字典当中的元素是通过键来访问的，只能使用不可变的对象作为字典的键；
# - 字典是无序的对象集合，字典中的键值对不会以任何方式进行排序；
#
# ### 字典常用方法
# - 增加新键值对可以通过使用索引运算符访问一个键值并为其分配与之相应的值；
# - del语句删除某一键值对；
# - item方法访问字典中的每一个键值对信息，将返回一份包含元组（相应的键值对信息）的列表；
# - 使用in运算符来检查某对键值—值配对是否存在；
# - help(dict)获取dict类的更多信息；
