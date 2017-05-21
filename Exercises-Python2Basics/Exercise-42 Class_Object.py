# -*- coding: utf-8 -*-
__author__ = 'Anliven'

## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None  # 确保类的 self.pet 属性被设置为 None

class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name) # 将父类的 __init__ 方法运行起来
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")


# 了解类的继承(inheritance)与多重继承(multiple inheritance)