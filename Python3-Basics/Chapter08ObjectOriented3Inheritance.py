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

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('AAA', 29, 50000)
s = Student('BBB', 18, 85)
members = [t, s]
for member in members:
    member.tell()

# ### 继承（Inheritance）
# - 通过继承机制可以重用（Reuse）代码；
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
