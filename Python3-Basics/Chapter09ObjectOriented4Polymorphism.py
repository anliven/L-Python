#! python3
# -*- coding: utf-8 -*-


class People:
    def speak(self):
        print("people is speaking")


class Student(People):
    def speak(self):  # 重写父类的speak方法
        print("student is speaking")


class Teacher(People):
    pass


s = Student()  # 子类Student重写了父类People的speak()方法，当Student类的对象s调用speak()方法时优先调用Student的speak方法
s.speak()
t = Teacher()
t.speak()


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

eatting_double(animal)
eatting_double(dog)  # 接收的参数必须是拥有eat方法的对象，否则执行报错
eatting_double(cat)

# ### 方法重写
# - 子类继承会继承父类的所有方法，当父类方法无法满足需求，可在子类中定义一个同名方法覆盖父类的方法；
# - 当子类的实例调用该方法时，优先调用子类自身定义的方法；
#
# ### 多态 ???
# 多态意味着变量并不知道引用的对象是什么，根据引用对象的不同表现不同的行为方式；
