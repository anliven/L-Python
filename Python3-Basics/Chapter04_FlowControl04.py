# -*- coding: utf-8 -*-


def check_exits(obj: str) -> bool:  # 判断变量是否存在
    return obj in locals() or obj in globals()  # 内置函数locals()与globals()返回值是字典形式


x = 666
y = x
print(check_exits('x'), check_exits('y'))
del x
print(check_exits('x'), check_exits('y'))

try:
    x
except NameError:
    print("Variable is not exist.")
else:
    print("Variable is exist.")

exec("print('Hello, Python3')")  # 将字符串作为代码执行

n1 = 111
exec('n1 = 333')
print(n1)  # 执行字符串代码其实污染了当前的命名空间（也称为作用域，是用来放置变量的一个字典）
n2 = 555
scope = {}
exec('n2 = 777', scope)  # 指定代码字符串的命名空间，用来存放通过exec语句创建的变量
print(n2, scope['n2'])
print(scope.keys())  # 其中“__builtins”字典包含了所有内置函数和值

print(eval("3 + 8 - 2 * 3"))
scope['x'] = 2
scope['y'] = 3
print(eval('x *y ', scope))  # 同一个命名空间可用于多次调用exec或eval，但不推荐这样做
print(scope.keys())

# ### locals()
# https://docs.python.org/3/library/functions.html#locals
# 内置函数locals()用来返回局部名字空间的一个拷贝，返回值是字典形式；
#
# ### globals()
# https://docs.python.org/3/library/functions.html#globals
# 内置函数globals()用来返回实际的全局名字空间，返回值是字典形式；
# 特别注意：对globals所返回的dictionary的任何改动都会直接影响到全局变量的取值；
#
# ### 使用del删除
# 通常Python解释器会自动删除不再使用的对象（没有任何变量或数据结构成员指向此对象），这个过程被称为垃圾收集；
# 使用del语句删除对象引用的同时也会删除对象本身；
#
# ### exec()
# https://docs.python.org/3/library/functions.html#exec
# 内置函数exec()用来将字符串作为代码执行，主要用于动态地创建代码字符串；
# 特别注意：执行存储在字符串中的代码，可能会带来严重的隐患，一般不建议这样做；
#
# ### eval()
# https://docs.python.org/3/library/functions.html#eval
# 内置函数eval()用来计算用字符串表示的Python表达式的值，并返回结果；
