#! python3
# -*- coding: utf-8 -*-


class SchoolMember:  # 基类（Base Class）或超类（Superclass）
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):  # 派生类（Derived Classes）或子类（Subclass）
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # 在方法名前加上基类名作为前缀，再传入self和其余变量，来调用基类的方法
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):  # 重写方法
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

    def teahing(self):  # 在子类中增加方法
        print('This is a teacher! - Teaching!')


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

    def learning(self):
        print('This is a student! - Learning!')


class Master(SchoolMember, Teacher):  # 多重继承
    pass


t = Teacher('AAA', 29, 50000)
t.tell()
t.teahing()
s = Student('BBB', 18, 85)
s.tell()
s.learning()

members = [t, s]
for member in members:
    member.tell()

# ### 继承（Inheritance）
# - 通过继承机制可以重用（Reuse）代码，子类自动获得父类的全部属性和方法；
# - 继承是类之间实现类型与子类型（Type and Subtype）关系；
# - 定义派生类或子类时，需要在类后面跟一个包含基类名称的元组；
#
# ### __init__
# 如果在子类中定义了__init__ 方法，Python不会自动调用基类的构造函数，如果需要可以显式地调用；
# 如果子类中没有定义__init__ 方法，Python将会自动调用基类的构造函数；
#
# ### 多重继承（Multiple Inheritance）
# - 除了从一个父类继承外，Python允许从多个父类继承；
# - 通过多重继承，一个子类可以同时获得多个父类的所有功能；
# - 请注意基类的排列顺序，当子类调用基类方法时，从左到右依次查找继承的基类中是否包含该方法，直到找到就停止，否则报错；
#
# ### MixIn
# - 在设计类的继承关系时，通常主线都是单一继承下来的，如果需要“混入”额外的功能，通过多重继承就可以实现，这种设计通常称之为MixIn;
# - MixIn的目的就是给一个类增加多个功能;
# - 在设计类的时候，优先考虑通过多重继承来组合不同类的功能，而不是设计多层次的复杂的继承关系;
#
# ### 方法重写
# - 子类继承会继承父类的所有方法，当父类方法无法满足需求，可在子类中定义一个同名方法覆盖父类的方法；
# - 当子类的实例调用该方法时，优先调用子类自身定义的同名方法；
