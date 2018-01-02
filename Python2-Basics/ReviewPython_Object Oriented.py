# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# Python面向对象（Object Oriented）


#####　概念简介
# 类(Class): --- 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 类变量： --- 类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员： --- 类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重载： --- 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重载。
# 实例变量： --- 定义在方法中的变量，只作用于当前实例的类。
# 继承： --- 即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
# 实例化： --- 创建一个类的实例，类的具体对象。
# 方法： --- 类中定义的函数。
# 对象： --- 通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

# ----------------------------------------------------------------------------------------------------------------------

##### 一个简单的Python类实例

class Employee:   # 使用class语句来创建一个新类，class之后为类的名称并以冒号结尾

    """Common base class for all employees"""  # 类的文档字符串（帮助信息），可以通过ClassName.__doc__查看。

    empCount = 0   # empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。可以在内部类或外部类使用Employee.empCount访问。

    def __init__(self, name, salary):   # __init__()方法被称为类的构造函数或初始化方法，当创建了类的实例时就会调用该方法。
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

##### 创建实例对象
emp1 = Employee("Zara", 2000)   # 创建一个类的实例，可以使用类的名称，并通过__init__方法接受参数。
emp2 = Employee("Manni", 5000)

##### 访问属性
emp1.displayEmployee()   # 使用点(.)来访问对象的属性。
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount   # 使用类的名称访问类变量。

##### 添加，删除，修改实例的属性
emp1.age = 7  # 添加一个 'age' 属性
print emp1.age
emp1.age = 8  # 修改 'age' 属性
print emp1.age
del emp1.age  # 删除 'age' 属性

##### 使用函数方式来访问属性：
#  getattr(obj, name[, default]) : 访问对象的属性。
#  hasattr(obj,name) : 检查是否存在一个属性。
#  setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
#  delattr(obj, name) : 删除属性。
setattr(emp2, 'age', 8)  # 添加属性 'age' 值为 8
print getattr(emp2, 'age')  # 返回 'age' 属性的值
print hasattr(emp2, 'age')  # 如果存在 'age' 属性返回 True。
delattr(emp2, 'age')   # 删除属性 'age'

# ----------------------------------------------------------------------------------------------------------------------

##### Python内置类属性
# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于某个导入模块mod中，那className.__module__ 等于mod）。
# __bases__ : 类的所有父类构成元素（用来处理继承,它包含了一个由所有父类组成的元组）

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
# print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

# ----------------------------------------------------------------------------------------------------------------------

##### python对象销毁(垃圾回收) ？？？

# Python使用"引用计数"来追踪内存中的对象。在Python内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。
# 但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数
del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数

# 垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
# 循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。
# 这种情况下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
# 作为引用计数的补充， 循环垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。
# 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。

# 析构函数 __del__在对象消逝的时候被调用，当对象不再被使用时，__del__方法运行：


class Point:

    def __init(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # 打印对象的id
del pt1
del pt2
del pt3

# 以上实例运行结果如下：
# 3083401324 3083401324 3083401324
# Point destroyed

# ----------------------------------------------------------------------------------------------------------------------

# 类的继承
# 通过继承机制可以实现代码的重用。继承也可以理解成类之间的类型和子类型关系。
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
# 不惜一切代价地避免多重继承，它带来的麻烦比能解决的问题都多。

# 1：在继承中基类的构造（__init__()方法）不会被自动调用，需要在其派生类的构造中亲自专门调用。
# 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
# 3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。

# 可以使用issubclass()或者isinstance()方法来检测类之间或者类与实例对象之间的关系。
#   issubclass(sub,sup) --- 布尔函数，判断一个类是否是另一个类的子类或者子孙类，如果是则返回True。
#   isinstance(obj, Class) --- 布尔函数，如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回True。


class Parent:        # 定义了一个基类（父类）

    parentAttr = 100

    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr


class Child(Parent):  # 定义了一个派生类（子类）。继承语法： class 派生类名（基类名），基类名写在括号里。

    def __init__(self):  # 在继承中基类的构造（__init__()方法）不会被自动调用，需要在其派生类的构造中亲自专门调用。???
        print "Calling child constructor"

    def childMethod(self):  # 定义了一个子类的方法
        print 'Calling child method'

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法

print issubclass(Child, Parent)  # 判断类Child是否是类Parent的子类，结果显示为True，证明是子类与父类的关系。
print isinstance(Parent, Child)  # 判断类Parent是否是类Child的子类，结果显示为False，证明不是子类与父类的关系。
print isinstance(c, Child)  # 判断c是不是类Child的实例对象，结果显示为True，证明c是类Child的实例对象。
print isinstance(c, Parent)  # 判断c是不是类Parent的实例对象，结果显示为True，证明c是类Parent的实例对象。

# ----------------------------------------------------------------------------------------------------------------------

##### 重载（Override）
# 如果父类方法的功能不能满足需求，可以通过在子类中覆写父类的方法，来实现新功能，因此也可叫做显式覆写（Explicit Override）。


class NewChild(Parent):  # 定义子类NewChild,父类是先前定义的Parent

    def __init__(self):  # 在继承中基类的构造（__init__()方法）不会被自动调用，需要在其派生类的构造中亲自专门调用。???
        print "Calling child constructor"

    def parentMethod(self):  # 这里重载了父类的parentMethod方法
        print 'Calling child method'  # 对print的内容作了改动"parent"变为"child"

nc = NewChild()  # 创建子类NewChild的实例对象nc
nc.parentMethod()  # 调用子类的重载方法parentMethod

##### 基础重载方法 ？？？
# __init__ ( self [,args...] )
# 构造函数-----简单的调用方法: obj = className(args)
# __del__( self )
# 析构方法, 删除一个对象-----简单的调用方法 : dell obj
# __repr__( self )
# 转化为供解释器读取的形式-----简单的调用方法 : repr(obj)
# __str__( self )
# 用于将值转化为适于人阅读的形式-----简单的调用方法 : str(obj)
# __cmp__ ( self, x )
# 对象比较-----简单的调用方法 : cmp(obj, x)

# ----------------------------------------------------------------------------------------------------------------------

##### 运算符重载 ？？？
# 了解Python的运算符，比如：__add__ 、__sub__、__eq__ 、__del__、__cmp__等等。
# 在Python中，每一个类都默认内置了所有可能的运算符方法，只要重写某个运算符方法，就可以实现针对该运算符的重载。


class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):  # 重载了__add__方法，也就是重写了+操作符号
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

# 执行结果为: Vector(7,8)

# ----------------------------------------------------------------------------------------------------------------------

##### 隐藏数据

# 在python中只要把类变量名或成员函数前面加两个下划线即可实现数据隐藏的功能。
# 对于类的实例来说，其实现数据隐藏的变量名和成员函数是不能使用的，对于其类的继承类来说，也是隐藏的。
# 但可以使用object._className__attrName的方式来访问属性。
# 在隐藏数据的情况下，其继承类可以定义其一模一样的变量名或成员函数名，而不会引起命名冲突。


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
# print counter.__secretCount   # 不允许实例化的类访问隐藏数据，因此会报错：no attribute。
print counter._JustCounter__secretCount   # 可以使用object._className__attrName访问属性。

# ----------------------------------------------------------------------------------------------------------------------