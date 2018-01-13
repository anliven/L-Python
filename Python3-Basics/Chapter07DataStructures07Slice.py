#! python3
# -*- coding: utf-8 -*-

# 字符串
testString = '1234567890'
print(testString)
print('Strings--Index 0:', testString[0])

print('Strings--Index 1 to 3:', testString[1:3])
print('Strings--Index start to 3:', testString[:3])
print('Strings--Index -2 to end:', testString[-2:])
print('Strings--Index start to -1:', testString[:-1])
print('Strings--Index 1 to -1:', testString[1:-1])
print('Strings--Index start to end:', testString[:])

print('Strings--Step 1 : ', testString[::1], ' Step 2 : ', testString[::2])
print('Strings--Step -1 : ', testString[::-1], ' Step -2 : ', testString[::-2])

# 列表
testList = ['111', '222', '333', '444']
print(testList)
print('List--Index 0:', testList[0], ' Index 1:', testList[1])
print('List--Index -1:', testList[-1], ' Index -2:', testList[-2])

print('List--Index 1 to 3:', testList[1:3])
print('List--Index start to 3:', testList[:3])
print('List--Index 2 to end:', testList[2:])
print('List--Index start to -1:', testList[:-1])
print('List--Index 1 to -1:', testList[1:-1])
print('List--Index start to end:', testList[:])

print('List--Step 1 : ', testList[::1], ' Step 3 : ', testList[::3])
print('List--Step -1 : ', testList[::-1], ' Step 3 : ', testList[::-3])

# ### 序列（Sequence）
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
# - 通过切片（Slicing）能够截取指定索引范围的序列，可以很方便地获取序列的子序列；
# - 语法格式：data[i:j]，i为起始下标，j为终止下标；
# - 特别注意，“前开后闭”：获得的片段包括起始位置，但不包括结束位置；
# - 可以使用负数，位置计数将从队列的末尾开始，此时从-1开始计数；
# - 可以设定第三个参数作为切片的步长（Step），默认步长大小为1；
#
# ### 引用
# - 如果希望创建一份诸如序列等复杂对象的副本，必须使用切片操作来生成一份序列的副本；
# - 如果仅仅是将一个变量名赋予给另一个名称，实际上都将“查阅”同一个对象；
