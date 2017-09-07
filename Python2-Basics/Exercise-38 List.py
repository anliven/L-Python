# -*- coding: utf-8 -*-
__author__ = 'Anliven'

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # string.split()分割字符串成列表,默认是以空格作为分隔符
more_stuff =["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # list.pop()移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    print "Adding: ", next_one
    stuff.append(next_one) # list.append()在列表末尾添加新的对象
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # 读取列表的第一个元素内容
print stuff[-  1] # whoa! fancy # 读取列表最后一个元素内容
print stuff.pop() # list.pop()移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print stuff[-  1]

# string.join（）用来连接字符串
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
