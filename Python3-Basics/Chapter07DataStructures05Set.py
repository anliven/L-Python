#! python3
# -*- coding: utf-8 -*-

sample_set = set(['AAA', 'BBB', 'AAA', 'BBB', 111, 222])  # 重复元素在set中自动被过滤
print(sample_set)
sample_set1 = {'Dog', 'Sheep', 'Pig'}
print(sample_set1)
sample_set2 = set('Dog Sheep Pig')
print(sample_set2)

testSet = {'111', '222', '333'}
testSet.add('444')  # add(key)方法添加元素到set中，可以重复添加，但会自动被过滤
if '444' in testSet:  # 检测成员关系
    print(True)
print('testSet:', testSet)

testSet2 = testSet.copy()  # Return a shallow copy of a set.
print(testSet.issuperset(testSet2))  # Report whether this set contains another set.
testSet2.remove('444')
print('testSet2:', testSet2)

print('| : ', testSet | testSet2)  # A | B：并集，在A或B中的对象
print('& : ', testSet & testSet2)  # A & B：交集，同时在A和B中的对象
print('& : ', testSet.intersection(testSet2))
print('- : ', testSet - testSet2)  # A – B：差集，在A中且不在B中
print('^ : ', testSet ^ testSet2)  # A ^ B：对称集，在A或B中的对象但不同时在A和B中

testSet3 = set()
testSet3.add('AAA')
print('testSet3:', testSet3)

# ### 集合（Set）
# - 集合（Set）是无序不重复的序列；
# - 重复元素在set中自动被过滤;
# - 通常用来进行成员关系测试和删除重复元素，且支持集合运算（并交差等）；
# - 使用set()函数或大括号{}声明集合，但创建空集合必须使用set()；
#
# ### 集合的定义
# {}定义：每个元素就是obj1,obj2,...，“s1 = {obj1,obj2,obj3,…}”；
# set()定义：每个元素为obj拆分的单个字符列表，“s2 = set(obj)”；
#
# ### 常用方法
# - 支持union(联合),intersection(交),difference(差)等数学运算；
# - help(set)获取Set类的更多信息；
