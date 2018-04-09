#! python3
# -*- coding: utf-8 -*-


class SchoolMember:  # 基类（Base Class）或超类（Superclass）
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

    def who(self):
        print("This ia a school member.")


class Teacher(SchoolMember):  # 派生类（Derived Classes）或子类（Subclass）
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # 初始化基类，否则将无法继承基类的name和age属性
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):  # 重写方法
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

    def teahing(self):  # 在子类中增加方法
        print('This is a teacher! - Teaching!')


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        # SchoolMember.__init__(self, name, age)
        super(Student, self).__init__(name, age)  # 使用super()初始化基类，否则将无法继承基类的name和age属性
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)  # 直接调用父类的方法
        print('Marks: "{:d}"'.format(self.marks))

    def learning(self):
        print('This is a student! - Learning!')


class Master(Teacher, Student):  # 多重继承
    pass


t = Teacher('AAA', 29, 50000)
t.tell()
t.teahing()
t.who()
s = Student('BBB', 18, 85)
s.tell()
s.learning()
s.who()
m = Master('CCC', 35, 1000000)
m.teahing()
m.learning()

members = [t, s, m]
for member in members:
    member.tell()

print(isinstance(s, SchoolMember), isinstance(s, Student), isinstance(s, Master))


class MyList:
    __ml = []

    def __init__(self, *args):
        self.__ml = []
        for i in args:
            self.__ml.append(i)

    def __add__(self, x):  # 运算符“+”重载（重写）
        for i in range(0, len(self.__ml)):
            self.__ml[i] += x
        return self.__ml


la = MyList(1, 2, 3, 4, 5)
print(la + 10)

# ### 继承（Inheritance）
# - 通过继承机制可以重用（Reuse）代码，子类自动获得父类的全部属性和方法；
# - 继承是类之间实现类型与子类型（Type and Subtype）关系；
# - 定义派生类或子类时，需要在类后面跟一个包含基类名称的元组；
#
# ### __init__
# 如果在子类中定义了__init__ 方法，Python不会自动调用基类的构造函数，如果需要可以显式地调用；
# 如果子类中没有定义__init__ 方法，Python将会自动调用基类的构造函数；
#
# ### 新式类与经典类的区别
# 调用父类对的方式：
# - 经典类：父类.方法(self)
# - 新式类：父类.方法(self)和super(当前类,self).方法()
# 多继承属性搜索顺序：
# - 经典类：先深入继承树左侧，再返回，然后开始找右侧；
# - 新式类：先水平搜索，然后再向上搜索；
# 特别注意：在Python3中默认都是创建新式类，在Python2中只有继承自object类的才是新式类；
#
# ### super()
# 可以在__init__前加上父类名作为前缀，再传入self和其余变量，来初始化父类；
# 也可以使用super()来初始化父类；
# 示例： super(Student, self).__init__(name, age)
# - 函数super(Student, self)将返回当前类继承的父类，然后调用__init__()方法；
# - self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）；
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
# ### 方法重写（重载）
# - 子类继承会继承父类的所有方法，当父类方法无法满足需求，可在子类中定义一个同名方法覆盖父类的方法；
# - 当子类的实例调用该方法时，优先调用子类自身定义的同名方法；
#
# ### 运算符重写（重载）
# 通过重写Python内置魔法方法来实现运算符的重载；
# 例如，如果类重写了__add__方法，当类的对象出现在+运算符中时会调用这个方法；
# 类可以重载算术运算、打印、函数调用、索引、属性等魔法方法；
#
# ### isinstance()
# isinstance()判断是否是摸个指定类型的数据对象；
# 可以用在内置数据类型如str、list、dict等，也可以判断自定义的类，因为自定义类本质上都是数据类型；
# 父类的实例不能是子类类型，因为子类比父类多了一些属性和方法，而子类的实例可以看成它本身的类型，也可以看成它父类的类型；
