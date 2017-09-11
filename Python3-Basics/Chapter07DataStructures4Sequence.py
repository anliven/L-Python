# -*- coding: utf-8 -*-

testList = ['111', '222', '333', '444']
testString = '1234567890'

# 索引操作（下标操作）
print('Item 0:', testList[0], ' Item 1:', testList[1], ' Item 2:', testList[2], ' Item 3:', testList[3])
print('Item -1:', testList[-1], ' Item -2:', testList[-2], ' Item -3:', testList[-3], ' Item -4:', testList[-4])
print('Character 0:', testString[0])

# 列表切片
print('List - Item 1 to 3:', testList[1:3])
print('List - Item 2 to end:', testList[2:])
print('List - Item start to -1:', testList[:-1])
print('List - Item 1 to -1:', testList[1:-1])
print('List - Item start to end:', testList[:])

# 字符串切片
print('Strings - characters 1 to 3:', testString[1:3])
print('Strings - characters 2 to end:', testString[2:])
print('Strings - characters start to -1:', testString[:-1])
print('Strings - characters 1 to -1:', testString[1:-1])
print('Strings - characters start to end:', testString[:])

# 指定步长切片
print('List Step 1 : ', testList[::1], ' Step 2 : ', testList[::2], ' Step 3 : ', testList[::3])
print('List Step -1 : ', testList[::-1], ' Step -2 : ', testList[::-2], ' Step 3 : ', testList[::-3])
print('Strings Step 1 : ', testString[::1], ' Step 2 : ', testString[::2], ' Step 3 : ', testString[::3])
print('Strings Step -1 : ', testString[::-1], ' Step -2 : ', testString[::-2], ' Step -3 : ', testString[::-3])

# ### 序列（ Sequence）
# - 序列的三种形态：列表、元组与字符串；
#
# ### 资格测试
# - 可以进行资格测试（Membership Test，也就是in与not in表达式）；
#
# ### 索引操作
# - 通过索引操作（Indexing Operations）或下标操作（Subscription Operation），获取序列中的项目；
# - 可以使用负数，位置计数将从队列的末尾开始，此时从-1开始计数；
#
# ### 切片操作
# - 通过切片（Slicing）运算符能够获取序列中的部分片段；
# - 获得的片段包括起始位置，但不包括结束位置；
# - 可以使用负数，位置计数将从队列的末尾开始，此时从-1开始计数；
# - 可以设定第三个参数作为切片的步长（Step），默认步长大小为1；
#
# ### 引用
# - 如果希望创建一份诸如序列等复杂对象的副本，必须使用切片操作来生成一份序列的副本；
# - 如果仅仅是将一个变量名赋予给另一个名称，实际上都将“查阅”同一个对象；
