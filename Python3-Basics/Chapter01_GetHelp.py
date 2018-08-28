# -*- coding: utf-8 -*-

print("### Keywords List: ")
help("keywords")  # 查看所有的关键字

print("### The help information of function - print: ")
help("print")  # 查看print()函数的帮助信息

print("### A list of valid attributes of function - dir: \n", dir())  # 查看当前属性及方法
print(dir("__builtins__"))  # 查看BIF（built-in functions）信息

# ### help()
# 内置help()函数获得函数或语句的帮助信息，多用来查看对象的详细说明，按q键退出；
# 对于已定义或引入的对象，help([object])查询不使用单引号和双引号;
# 对于未引入的模块等对象，要使用单引号或双引号;
# - 查看对象信息：help([object])
# - 查看所有的keyword：help("keywords")
# - 查看所有的modules：help("modules")
# - 查看常见的topics： help("topics")
# - 查看模块,例如：help("sys")
# - 查看数据类型,例如: help("list")
# - 查看数据类型的成员方法,例如: help("list.append")
#
# ### dir()
# 内置dir()函数多用来查看对象的属性方法，输出的是列表；
# 查看当前属性及方法：dir()
# 查看对象的属性及方法(此时不使用单引号和双引号)：dir([object])
#
# ### 注意
# 使用help()和dir()之前，确定查询的对象已被定义或引入，否则会报错：“NameError: name is not defined”；
#
# ### Documentation
# - Docs：https://docs.python.org/
# - Wiki：https://wiki.python.org/moin/
