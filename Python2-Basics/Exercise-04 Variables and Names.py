# -*- coding: utf-8 -*-
__author__ = 'Anliven'

cars = 100  # "=(single-equal)" 的作用是将右边的值赋予左边的变量
space_in_a_car = 4.0  # 浮点数
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # 计算
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car  # 下划线(underscore) 字符通常被用来隔开单词
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey %s there." % "you"
