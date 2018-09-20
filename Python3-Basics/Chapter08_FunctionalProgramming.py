# -*- coding: utf-8 -*-
import math

print(abs(-123))  # 对函数abs进行调用
print(abs)

f = abs  # 变量f指向函数，此时f是一个函数对象
print(f(-123))  # 此时f(-123)与abs(-123)作用相同
print(f)

abs = len  # 变量abs指向len
print(abs([1, 2, 3]))
print(abs)  # 函数名其实就是指向函数的变量


def test(x, y, func):  # 定义一个接受函数作参数的函数
    return func(x) + func(y)


print(test([0, 0, 0], [1, 1, 1], len))  # 两个列表的长度之和
print(test(25, 9, math.sqrt))  # 两个数分别开平方后的和

# ### 函数式编程的特点
# - 将计算视为函数而非指令
# - 纯函数式编程：不需要变量，没有副作用，测试简单
# - 支持高阶函数，代码简洁
#
# ### Python支持的函数式编程
# - 不是纯函数编程：允许有变量
# - 支持高阶函数：函数可以作为变量传入
# - 支持闭包：可以返回函数
# - 有限度地支持匿名函数
#
# ### 高阶函数
# - 变量可以指向函数，函数的参数也可以指向函数
# - 一个函数可以接受另一个函数作为参数，能够接受函数作参数的函数就是高阶函数
#
# ### 内置函数（Built-in Functions）
# 善于利用内置函数，将会极大地提高编程效率；
# https://docs.python.org/3/library/functions.html
# 一些常用内置函数：
# - dir(sys)        : 显示对象的属性
# - help(sys)       : 交互式帮助
# - int(obj)        : 转型为整形
# - str(obj)        : 转为字符串
# - len(obj)        : 返回对象或序列长度
# - open(file,mode) : 打开文件 #mode (r 读,w 写, a追加)
# - range(0,3)      : 返回一个整形列表
# - input("str:")   : 用户输入
# - type(obj)       : 返回对象类型
# - abs(-123)       :  绝对值
# - divmod(x,y)     : 函数完成除法运算，返回商和余数。
# - round(x[,n])    : 函数返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
# - max()           : 字符串中最大的字符
# - min()           : 字符串中最小的字符
# - sorted()        : 对序列排序
# - reversed()      : 对序列倒序
# - enumerate()     : 返回索引位置和对应的值
# - sum()           : 总和
# - list()          : 变成列表可用于迭代
# - eval('3+4')     : 将字符串当表达式求值 得到7
# - exec 'a=100'    : 将字符串按python语句执行
# - tuple()         : 变成元组可用于迭代（一旦初始化便不能更改的数据结构,速度比list快）
# - zip()        : 返回一个合并后的列表
# - isinstance(object,int): 测试对象类型是否为int
# - ......
