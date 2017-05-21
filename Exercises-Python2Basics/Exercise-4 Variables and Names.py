# -*- coding: utf-8 -*-
__author__ = 'Anliven'

cars = 100 # "=(single-equal)" 的作用是将右边的值赋予左边的变量名。
space_in_a_car = 4.0 #这里的4.0是使用了浮点数
#space_in_a_car = 4 #这里的4是使用了整数。
drivers = 30 #操作符两边加上空格会让代码更容易阅读。
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
# space_in_a_car 中的 _ 是 下划线(underscore) 字符。这个符号在变量里通常被用作假想的空格，用来隔开单词。
average_passengers_per_car = passengers / cars_driven
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey you there."
print "Hey %s there." % "you"