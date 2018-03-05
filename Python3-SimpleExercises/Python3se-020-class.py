#! python3
# -*- coding: utf-8 -*-


class Person(object):
    count = 0

    def __init__(self, name):
        Person.count += 1
        self.name = name


p1 = Person('AAA')
print(Person.count)

p2 = Person('BBB')
print(Person.count)

p3 = Person('CCC')
print(Person.count)

# 创建一个类，可以统计出一共创建了多少个类的实例；
