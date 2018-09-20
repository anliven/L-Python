# -*- coding: utf-8 -*-

x = 11  # 在主代码块中声明变量，全局变量
y = 22
z = 35


def test_func():  # 定义函数“def 函数名（参数列表）:”
    """This is an sample of docstrings."""
    print('Hello Python3!')  # 函数体


def change_global():
    global z  # global语句声明z是一个全局变量
    print('z is', z)
    z = 29
    print('Changed global z to', z)


def empty_function():  # 空函数
    """This is an sample of docstrings."""
    pass  # pass用来作为占位符，先让代码能运行起来


print("# Callable: ", callable(test_func))  # 判断对象是否是可调用的（函数或方法）

test_func()  # 调用函数
change_global()
empty_function()
print(empty_function.__doc__)  # 打印函数的文档字符串属性（__doc__）

f = abs  # 函数名其实就是指向一个函数对象的引用，这里将求绝对值的函数abs赋给一个变量，相当于给这个函数起了一个“别名”
print(f(-3))  # 通过变量调用abs函数
print("# Callable: ", callable(f))  # 判断对象是否是可调用的（函数或方法）


def print_max(a, b=7):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


print_max(5)  # 直接传递，并使用默认参数值
print_max(x, y)  # 以参数的形式传递
print_max(b=333, a=555)  # 使用命名（关键字）而非位置来指定函数中的参数；


def test_args(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def test_args2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def test_args3(name, age, *, city, job):  # 命名关键字参数
    print(name, age, city, job)


def test_args4(*items):
    for var in items:
        print("*: ", var)


def test_args5(a=5, *numbers, **phonebook):
    print('#a: ', a, ' #numbers: ', numbers, ' #other: ', phonebook)
    for single_item in numbers:  # 遍历元组中的所有项目
        print('single_item:', single_item)
    for first_part, second_part in phonebook.items():  # 遍历字典中的所有项目
        print(first_part, second_part)
    return "This is a test!"  # 函数的返回值


test_args(1, 2, 3, 'a', 'b', x=99)
test_args2(1, 2, d=99, ext=None)
test_args3('Anliven', 29, city='Chengdu', job='Engineer')  # 命名关键字参数，调用时必须指明参数名字
test_args4(111, 'aaa', "AAA")
print(test_args5(10, 1, 2, 3, Jack=11111, John=22222, Inge=33333))


def repeat(count, name):
    print('count:{}, name:{}'.format(count, name))


args1 = [3, "dogs"]
repeat(*args1)  # unpack
args2 = {'count': 3, 'name': 'pigs'}
repeat(**args2)


def return_two_values():  # 通过函数来返回不同的值
    return 123, 'test'  # 返回多个值


returnNum, returnStr = return_two_values()
print('Values-1:', returnNum, '\nValues-2:', returnStr)

# ### 函数（Functions）
# - 函数是指完成特定功能、可重复使用、具有指定名称的语句组（程序片段）；
# - 函数调用：通过函数名可以在程序的不同地方多次执行；
# - 通过关键字def定义函数，依次写出函数名、括号、括号中的参数和冒号“:”，然后在缩进块中编写函数体，函数的返回值用return语句返回；
# - 使用函数可以实现代码重用，并且降低编程的难度；
# - 所有的函数都有返回值，如果没有指定返回值，默认返回None；
#
# ### 函数参数
# - 函数参数在定义函数的一对圆括号中指定，并通过逗号予以分隔；
# - 形参（Parameters）：在定义函数时给定的名称；
# - 实参（Arguments）：在调用函数时所提供给函数的值；
# - 默认定义的参数都是位置参数，实参以参数位置来指定给形参；
# - 可以使用命名（关键字）而非位置来指定函数中的参数，也就是说只需在调用时指明参数名称及其值即可；
# - 特别注意：参数定义的顺序必须依次是必选参数、默认参数、可变参数、命名关键字参数、关键字参数；
#
# ### 默认参数
# - 默认参数值：在函数定义时通过赋值运算符（=）可以指定参数的默认值；
# - 有默认值的参数必须位于没有默认值的参数之后；
# - 特别注意：定义默认参数时，必须指向不可变对象！；
#
# ### 不定长参数
# - 可选参数可以通过星号来实现可变的参数数量；
# - 可变参数：类似“*param”，从此处开始直到结束的所有位置参数（Positional Arguments）被汇集成一个名为param的元组（Tuple）；
# - 关键字参数：类似“**param”，从此处开始直至结束的所有关键字参数被汇集成一个名为param的字典（Dictionary）；
#
# ### 命名关键字参数
# - 命名关键字参数，调用时必须指明参数名字；
# - 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数；
# - 如果函数定义中已有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*：
# - 命名关键字参数可以提供默认值；
#
# ### 变量
# - 所有变量的作用域（Scope）是其被定义的所在代码块；
# - 局部变量，例如：在一个函数或的定义中声明变量时，变量名只存在于函数这一局部（Local）；
# - 全局变量，利用global语句可以声明函数之外定义的变量，但不建议这样使用；
# - 可以在同一global语句中指定不止一个的全局变量，例如“global x, y, z”；
#
# ### return
# - 用于从函数中返回值，可以返回一个或多个值；同时返回多个值时，结果是一个tuple；
# - 返回值可以是任意类型，可以返回函数；
# - 如果return语句没有搭配任何一个值则代表着返回None，表示空值；
# - 如果没有return语句，函数执行完后会返回结果为None（可以理解为，每一个函数都在其末尾隐含了一句“return None”）；
# - return执行后，函数终止；
# - 特别注意：区分返回值和输出（例如：print）
#
# ### callable()
# https://docs.python.org/3/library/functions.html#callable
# 内置函数callable()可用来判断对象是否是可调用的（函数或方法）；
#
# ### pass
# - 用于指示一个没有内容的语句块；
# - 可以用来作为占位符，比如代替未完成的代码，就可以放一个pass，先让代码能运行起来；
#
# ### 文档字符串（Documentation Strings）
# - 函数的文档字符串（DocString）放置在函数的第一逻辑行；
# - 可以通过使用函数的“__doc__”属性来获取函数的文档字符串属性，例如：help()函数和pydoc命令；
# - 强烈建议为所有重要的函数配以文档字符串；
#
# ### 内置函数（Built-in Functions）
# https://docs.python.org/3/library/functions.html
# Python具有大量实现常用功能的内置函数，也可以自定义函数，建议尽可能使用内置函数；
