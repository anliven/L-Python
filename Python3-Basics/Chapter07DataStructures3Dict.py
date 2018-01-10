#! python3
# -*- coding: utf-8 -*-

testDict = {
    'AAA': '11111',
    'BBB': '22222',
    'CCC': '33333',
    'DDD': '44444'
}
print("AAA's value is ", testDict['AAA'], end=' ')

del testDict['DDD']  # 删除键值对
print('\nThere are {} contacts in the testDict.'.format(len(testDict)))

for key, value in testDict.items():  # 遍历字典
    print('{} - {}'.format(key, value))

testDict['EEE'] = '55555'  # 添加键值对
if 'EEE' in testDict:
    print("EEE's value  is", testDict['EEE'])

# ### 字典（Dictionary）
# - 字典将键（Keys）与值（Values）联立到一起，其中键必须是唯一的；
# - 只能使用不可变的对象作为字典的键；
# - 使用花括号{}声明字典；键与值之间使用冒号分隔，每一对键与值用逗号区分；
# - 字典中的键值对不会以任何方式进行排序；
# - 使用索引运算符来指定某一键值以访问相应的键值对；
#
# ### 字典常用方法
# - del语句删除某一键值对；
# - 增加新键值对可以通过使用索引运算符访问一个键值并为其分配与之相应的值；
# - item方法访问字典中的每一个键值对信息，将返回一份包含元组（相应的键值对信息）的列表；
# - 使用in运算符来检查某对键值—值配对是否存在；
# - help(dict)获取dict类的更多信息；
