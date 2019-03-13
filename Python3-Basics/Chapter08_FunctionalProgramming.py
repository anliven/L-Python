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


def test(m, n, func):  # 定义一个接受函数作参数的函数
    return func(m) + func(n)


print(test([0, 0, 0], [1, 1, 1], len))  # 两个列表的长度之和
print(test(25, 9, math.sqrt))  # 两个数分别开平方后的和

# pow()
print("pow: {}".format(pow(12345, 67890, 123)))

# max() and set()
temp = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(temp), key=temp.count))  # # 查找列表中出现最频繁的数

# dict()
print(dict([('AAA', '123'), ('BBB', 456), ('CCC', '789')]))

sample_list = [1, 2, 3, 0]

# all()
if all(sample_list):
    print("All elements of the iterable are true (or if the iterable is empty)")
# any()
if any(sample_list):
    print("Any element of the iterable is true.")

# enumerate()
print("enumerate(): {}\ncontent: {}".format(enumerate(sample_list), list(enumerate(sample_list))))

# map()
x = [1, 2, 3]
y = map(lambda k: k + 1, x)  # map()对x中的每一个元素都应用lambda函数，返回一个map对象
print(list(y))  # map对象被转化成可迭代对象，如列表或者元组
nums = map(str, range(10))  # map()将内置函数类型str映射到迭代器range生成一个map对象
print("".join(nums))  # 创建一个连接从0到9的字符串

# zip()
l1 = ['AAA', 'BBB', 'CCC']
l2 = [111, 222, 333]
r1, r2 = zip(l1, l2), zip(*zip(l1, l2))
print("zip(): {}\n*zip(): {}".format(list(r1), list(r2)))

# isinstance()
if isinstance(sample_list, list):
    print("It's a list.")

sample_list2 = [1, 2, 3, 4, 5]
sample_list3 = ['A', 'B', 'C']
# 遍历列表
for i in sample_list2:
    print("Item:{}".format(i))
for i in reversed(sample_list2):  # 反向遍历
    print("Reversed Item:{}".format(i))
for i in sorted(sample_list2, reverse=True):  # 反向遍历
    print("Reversed Item:{}".format(i))
for index, element in enumerate(sample_list2):  # 遍历一个集合及其下标（通过enumerate函数获得元素的索引）
    print("Index:{} - Element:{}".format(index, element))
for num, letter in zip(sample_list2, sample_list3):  # 遍历两个集合，注意结果（最短匹配）
    print("num:{}-letter:{}".format(num, letter))
# 构建字典
print(dict(zip(sample_list2, sample_list3)))  # 注意结果（最短匹配）


def more_than_3(v):
    if v > 3:
        return v    


print(list(filter(more_than_3, sample_list2)))  # filter函数过滤列表

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
# https://docs.python.org/3/library/functions.html
# Python具有大量实现常用功能的内置函数，使用方便并且经过了优化，效率可能更高，建议尽可能使用内置函数；
# 建议尽可能的熟悉内置函数的文档；
#
# ### 一些内置函数：
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
# - sum()           : 总和
# - list()          : 变成列表可用于迭代
# - eval('3+4')     : 将字符串当表达式求值 得到7
# - exec 'a=100'    : 将字符串按python语句执行
# - tuple()         : 变成元组可用于迭代（一旦初始化便不能更改的数据结构,速度比list快）
# - zip()        : 返回一个合并后的列表
# - pow(x, y[, z])  计算x的y次方，以z为模
#
# all(iterable)  如果可迭代对象(数组，字符串，列表等)中的元素都是true(或者为空)的话返回True
# any(iterable)  如果可迭代对象中任何一个元素为true的话返回True，为空则返回False
# dict() 使用提供的条目生成一个新的字典
# enumerate(iterable, start=0)  返回一个枚举对象（索引位置和对应的值），iterable 必须是序列，iterator 或支持迭代的某个其他对象
# zip(*iterables)  创建一个迭代器，聚合来自每个迭代器的元素;与*运算符结合可用于解压缩列表
# isinstance(object, classinfo)  如果object参数是classinfo参数的实例，或者其子类的实例，则返回true，否则返回false
