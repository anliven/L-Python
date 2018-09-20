# -*- coding: utf-8 -*-
import keyword

m = r'\n'  # 输出时原型打印
n = u'中文'  # 定义为unicode编码
print('m:', m, 'n:', n)

x = 0 or 2 or 1  # 布尔运算赋值，x值为2
print('x:', x)

y = "hi"  # Python中的变量不需要声明类型，但在使用前必须赋值
if not isinstance(y, (int, float)):  # 内置函数isinstance()实现数据类型检查
    print('Bad operand type.')

a = b = c = 1
i, j, k = 3.5, 'hello', "python"  # 多个变量同时赋值
print(a, b, c, i, j, k)
print(id(a) == id(b) == id(c), id(i) == id(j) == id(k))  # id()查看在内存中的地址

a = 555  # 重新赋值
b = 888
a, b = b, a  # the fastest way to swap two variables in Python
print('a:', a, 'b:', b)

print(keyword.iskeyword(str))  # "str"是否为python关键字
print(keyword.kwlist)  # 返回python所有关键字
print(locals())  # 所有局部变量组成的字典
print(locals().values())  # 所有局部变量值的列表

x: int = 123  # 给变量赋值时同时提示数据类型
y: str = "abc123ABC"
z: bool = True
print(type(x), type(y), type(z))
t: float = 'test'  # 特别注意：仅仅是具备了“提示”功能，对于不符合期望的数据类型并不会报错
print(type(t))  # 真实数据类型是由实际赋值决定的

# ### 变量（Variables）
# 变量不需要声明类型，但在使用前必须赋值；
# 允许多个变量同时赋值;
# 等号“=”是赋值语句，可以把任意数据类型赋值给变量，可以反复赋值，而且可以赋不同类型的值；
# 注意：
# - 变量其实是值的“标签”，值才是内存中的数据，而“赋值”实际是建立“标签”和“内存数据”的关系；
# - 一个“内存数据”可以有多个“标签”（利用id()函数可以查看到，这些“标签”都指向同一个内存地址）；
#
# ### 变量的标识符（Identifiers）
# 变量的标识符也就是变量的名字，必须遵循如下规则：
# - 由字母、下划线（_）、数字（0~9）组成；
# - 不能以数字开头，也就是说，首字符必须是字母或下划线（_）；
# - 区分大小写；
# - 不能使用关键字；
#
# ### 数据类型（Data Type）
# - 变量可以将各种形式的值保存为不同的数据类型；
# - Python具有基本的数据类型，也可以通过类（Classes）创建自定义的数据类型；
# - 内置的数据类型转换函数：int(),str(),chr(),float(),bool(),hex()等；
# - 内置函数isinstance()实现数据类型检查；
# - 内置函数id()查看变量的值在内存中的地址；
#
# ### 指定变量类型
# Python是动态编程语言，不需要在创建变量时声明变量类型:
# 在PEP526中阐述了指定变量类型的方法：https://www.python.org/dev/peps/pep-0526/
# 特别注意：仅仅是具备了“提示”功能，对于不符合期望的数据类型并不会报错；
#
# ### isinstance()
# https://docs.python.org/3/library/functions.html#isinstance
# 内置函数isinstance()用来判断一个对象是否是一个类的实例，多用于数据类型检查；
#
# ### id()
# https://docs.python.org/3/library/functions.html#id
# 内置函数id()返回一个对象的标识（内存地址）；
#
# ### locals()
# 内置函数locals()用来返回局部名字空间的一个拷贝，返回值是字典形式；
# 详细信息：https://docs.python.org/3/library/functions.html#locals
#
# ### type()
# https://docs.python.org/3/library/functions.html#type
# 内置函数type()用来返回对象的类型；
