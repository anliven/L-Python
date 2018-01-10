#! python3
# -*- coding: utf-8 -*-

testSet = {'111', '222', '333'}
testSet.add('444')  # Add an element to a set.
if '444' in testSet:
    print(True)
print('testSet:', testSet)

testSet2 = testSet.copy()  # Return a shallow copy of a set.
print(testSet.issuperset(testSet2))  # Report whether this set contains another set.
testSet2.remove('444')
print('testSet2:', testSet2)

print('| : ', testSet | testSet2)  # Return the union of sets as a new set.
print('& : ', testSet & testSet2)  # Return the intersection of two sets as a new set.
print('& : ', testSet.intersection(testSet2))  # Return the intersection of two sets as a new set.
print('- : ', testSet - testSet2)  # Return the difference of two or more sets as a new set.

testSet3 = set()
testSet3.add('AAA')
print('testSet3:', testSet3)

# ### 集合（Set）
# - 集合（Set）是无序不重复元素的集（Collection）；
# - 通过集合可以进行资格和关系测试，消除重复元素等操作；
# - 使用set()函数或大括号声明集合，但创建空集合必须使用set()；
#
# ### 常用方法
# - 支持union(联合),intersection(交),difference(差)等数学运算；
# - help(set)获取Set类的更多信息；
