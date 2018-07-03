#! python3
# -*- coding: utf-8 -*-


class Animal:
    def eat(self):
        print("animal is eatting")


class Dog(Animal):
    def eat(self):  # 重写Animal的eat方法
        print("dog is eatting")


class Cat(Animal):
    def eat(self):  # 重写Animal的eat方法
        print("cat is eatting")


def eatting_double(animal_eat):
    animal_eat.eat()
    animal_eat.eat()


animal = Animal()
dog = Dog()
cat = Cat()
print(isinstance(animal, Animal), isinstance(dog, Dog), isinstance(cat, Cat))  # 可以用isinstance()判断是否属于某个类型

eatting_double(animal)
eatting_double(dog)  # 接收的参数必须是拥有eat方法的对象，否则执行报错
eatting_double(cat)


class Someone(object):
    def eat(self):
        print('Someone is eatting...')


s = Someone()
eatting_double(s)

# ### 多态
# 当定义一个class的时候，实际上是定义了一种数据类型；
# 对于一个变量，只需知道它的父类型，就可以放心地调用父类的方法，而具体调用的方法是作用在子类对象上，由运行时该对象的确切类型决定；
# 多态: 传入的任意类型，只要是父类或者子类，就会自动调用实际类型的属性方法；
# 多态意味着调用方只管调用，不管细节，只需要确保相关的属性方法编写正确，不用管原来的代码是如何调用的；
# 简而言之，同一个方法在不同的类中，实现不同的作用；
#
# 著名的“开闭”原则
# - 对扩展开放：允许新增子类；
# - 对修改封闭：不需要修改依赖父类型的属性方法；
#
# ### 静态语言 vs 动态语言
# - 对于静态语言（例如Java）来说，如果需要传入父类型，则传入的对象必须是父类型或者它的子类，否则将无法调用属性方法；
# - 对于动态语言（例如Python）来说，则不一定需要传入父类型，只需要保证传入的对象有一个对应的属性方法就可以；
