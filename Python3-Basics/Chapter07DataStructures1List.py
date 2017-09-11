# -*- coding: utf-8 -*-

testList = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(testList), 'items to purchase.')
print('These items are:', end=' ')
for item in testList:
    print(item, end=' ')

print('\nI also have to buy rice.')
testList.append('rice')
print('My shopping list is now.', testList)

print('I will sort my list now.')
testList.sort()
print('Sorted shopping list is', testList)

print('The first item I will buy is', testList[0])
oldItem = testList[0]
del testList[0]
print('I bought the', oldItem)
print('My shopping list is now.', testList)

# ### 列表（List）
# - 列表是一种用于保存一串项目的序列；
# - 使用方括号[]声明列表；
# - 列表是一种可变的（Mutable）数据类型，可以添加、移除或搜索列表中的项目；
# - 通过索引（Indexing）运算符访问列表中的项目（注意Python从0开始计数）；
#
# ### 列表常用方法
# - 使用for...in循环来遍历列表中的项目；
# - append方法向列表中添加项目；可以向列表中添加任何类型的对象，包括数字，甚至是其它列表；
# - sort方法对列表进行排序，影响列表本身，而不是返回一个修改过的列表；
# - del语句从列表中移除对应的项目；
# - help(list)获取List类的更多信息；
