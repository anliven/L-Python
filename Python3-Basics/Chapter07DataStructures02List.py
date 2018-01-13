#! python3
# -*- coding: utf-8 -*-

L = []  # 创建空列表
listSample = ["Hello", "Python", 'World', 2018, '!']
print(" All elements: %s" % listSample)  # 打印所有元素
print(listSample[1])  # 打印索引为1的元素（注意：返回元素而不是列表，所以返回值没有中括号）
print(listSample[1:3])  # 打印索引为1到2的元素，作为一个列表返回
print(listSample[3:])  # 从索引为3的元素开始，打印后续的所有元素
print(listSample[:2])  # 从开始到第1个元素
listSample[4] = 2018  # 修改列表的元素值
print(listSample)

testList = ['apple', 'mango', 'carrot', 'banana']
print(testList * 2)  # list*n：列表重复，生成一个新列表
print(listSample + testList)  # list1+list2：列表拼接
print('apple' in testList)  # obj in list：判断元素是否在列表中
print(max(testList))  # max(list)：返回列表最大值
print(testList.count("orange"))  # list.count(obj)：计算obj在列表出现的次数

print('I have', len(testList), 'items to purchase.')  # len(list)：列表元素个数
print('These items are:', end=' ')
for item in testList:
    print(item, end=' ')  # 列表迭代

print('\nI also have to buy orange and rice.')
testList.insert(0, "orange")  # list.insert(index,obj)：在下标为index的位置，插入obj
testList.append('rice')  # list.append(obj)：列表尾部添加元素obj
print('My shopping list is now.', testList)

print('Sort list.')
testList.sort()
print('Sorted shopping list is', testList)

print('The first item I will buy is', testList[0])
oldItem = testList[0]
del testList[0]
print('I bought the', oldItem)
print('My shopping list is now.', testList)

# ### 列表（List）
# - 列表是一种用于保存一串元素的序列；
# - 使用方括号[]声明列表；定义格式：list = [obj1,obj2,obj3,…]；
# - 列表中元素的类型可以不相同，支持数字、字符串、列表（嵌套）；
# - 列表是一种可变的（Mutable）数据类型，可以添加、移除或搜索列表中的元素；
#
# ### 访问列表
# - 通过索引（Indexing）运算符访问列表中的元素（特别注意：Python从0开始计数！）；
# - 列表截取的语法格式：变量[头下标:尾下标]，范围是“前开后闭”（不包括尾下标的元素）；
#
# ### 列表常用方法
# - 使用for...in循环来遍历列表中的元素；
# - len(list)：列表元素个数
# - list.count(obj)：计算obj在列表出现的次数
# - list.insert(index,obj)：在下标为index的位置，插入obj
# - append方法向列表中添加元素；可以向列表中添加任何类型的对象，包括数字，甚至是其它列表；
# - sort方法对列表进行排序，影响列表本身，而不是返回一个修改过的列表；
# - del语句从列表中移除对应的元素；
# - help(list)获取List类的更多信息；
