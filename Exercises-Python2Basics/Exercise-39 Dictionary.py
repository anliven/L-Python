# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# create a mapping of state to abbreviation
# 创建字典states{}
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
# 创建字典cities{}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# 以增加新的键值对的形式，向字典cities{}添加新内容
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
# 通过使用键名的方式，访问字典里的对应的值
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']] # 先获取了states['Michigan']的值MI，然后获取cities['MI']
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items(): # dict.items()以列表返回可遍历的(键, 值) 元组数组
    print "%s is abbreviated %s" % (state, abbrev)
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
print '-' * 10

# safely get a abbreviation by state that might not be there
state = states.get('Texas', None) # dict.get()宽松访问字典的key值，访问的key不存在时，返回None,可自定义None
if not state:
    print "Sorry, no Texas."
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


# Python 字典(Dictionary)的定义、常规用法、常用内置函数等等