#! python3
# -*- coding: utf-8 -*-

x = 11  # 在主代码块中声明变量，全局变量
y = 22
z = 35


def say_hello():  # 定义函数“def 函数名（参数列表）:”
    print('Hello!')  # 函数体


say_hello()  # 调用函数


def print_max(a, b=7):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


def changed_global():
    global z  # global语句声明z是一个全局变量
    print('z is', z)
    z = 29
    print('Changed global z to', z)


def print_para(*items):
    for var in items:
        print("*: ", var)


def total(a=5, *numbers, **phonebook):
    print('a:', a)

    for single_item in numbers:  # 遍历元组中的所有项目
        print('single_item:', single_item)

    for first_part, second_part in phonebook.items():  # 遍历字典中的所有项目
        print(first_part, second_part)

    return "This is a test!"  # 函数的返回值


def empty_function():
    """This is an sample of docstrings."""
    pass


print_max(5)  # 直接传递，并使用默认参数值
print_max(x, y)  # 以参数的形式传递
print_max(b=333, a=444)  # 使用命名（关键字）而非位置来指定函数中的参数；

changed_global()
print('Value of z is', z)

print_para(1, 'aaa', "AAA")
print(total(10, 1, 2, 3, Jack=11111, John=22222, Inge=33333))

empty_function()
print(empty_function.__doc__)  # 打印函数的文档字符串属性（__doc__）


def get_two_values():  # 通过函数来返回不同的值
    return 123, 'test'


returnNum, returnStr = get_two_values()
print('Values-1:', returnNum, '\nValues-2:', returnStr)


# ### 函数（Functions）
# - 函数是指可重复使用的程序片段；
# - Python具有大量实现常用功能的内置函数，也可以自定义函数，建议尽可能使用内置函数；
# - 通过关键字def定义函数，并具有固定格式；
#
# ### 函数参数
# - 函数参数在定义函数的一对圆括号中指定，并通过逗号予以分隔；
# - 形参（Parameters）：在定义函数时给定的名称；
# - 实参（Arguments）：在调用函数时所提供给函数的值；
# - 默认参数值：在函数定义时通过赋值运算符（=）可以指定参数的默认值；
# - 有默认值的参数必须位于没有默认值的参数之后；
# - 使用命名（关键字）而非位置来指定函数中的参数，也就是说只需在调用时指明参数名称及其值即可；
#
# ### 可变参数（不定长参数）
# - 函数里的参数数量是可变的，通过使用星号来实现；
# - 类似“*param”星号参数，从此处开始直到结束的所有位置参数（Positional Arguments）被汇集成一个名为param的元组（Tuple）；
# - 类似“**param”双星号参数，从此处开始直至结束的所有关键字参数被汇集成一个名为param的字典（Dictionary）；
#
# ### 变量
# - 所有变量的作用域（Scope）是其被定义的所在代码块；
# - 局部变量，例如：在一个函数或的定义中声明变量时，变量名只存在于函数这一局部（Local）；
# - 全局变量，利用global语句可以操作函数之外定义的变量，但不建议这样使用；
# - 可以在同一global语句中指定不止一个的全局变量，例如“global x, y, z”；
#
# ### return
# - 用于从函数中返回一个值；
# - 如果return语句没有搭配任何一个值则代表着返回None，代表着虚无；
# - 每一个函数都在其末尾隐含了一句“return None”；
#
# ### pass
# - 用于指示一个没有内容的语句块；
#
# ### 文档字符串（Documentation Strings）
# - 函数的文档字符串（DocString）放置在函数的第一逻辑行；
# - 可以通过使用函数的“__doc__”属性来获取函数的文档字符串属性，例如：help()函数和pydoc命令；
# - 强烈建议为所有重要的函数配以文档字符串；
