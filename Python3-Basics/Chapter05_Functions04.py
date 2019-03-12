# coding=utf-8

sample_list = [1, 2, 3, 0]

# all()
if all(sample_list):
    print("All elements of the iterable are true (or if the iterable is empty)")
# any()
if any(sample_list):
    print("Any element of the iterable is true.")

# dict()
print(dict([('AAA', '123'), ('BBB', 456), ('CCC', '789')]))

# enumerate()
print("enumerate(): {}\ncontent: {}".format(enumerate(sample_list), list(enumerate(sample_list))))
for i, item in enumerate(sample_list, start=3):
    if i > 4:
        print(i, item)

# isinstance()
if isinstance(sample_list, list):
    print("It's a list.")

# pow()
print("pow(): {}".format(pow(12345, 67890, 123)))

# zip()
l1 = ['AAA', 'BBB', 'CCC']
l2 = [111, 222, 333]
r1, r2 = zip(l1, l2), zip(*zip(l1, l2))
print("zip(): {}\n*zip(): {}".format(list(r1), list(r2)))

# ### 内置函数（Built-in Functions）
# https://docs.python.org/3/library/functions.html
# Python具有大量实现常用功能的内置函数，使用方便并且经过了优化，效率可能更高，建议尽可能使用内置函数；
# 建议尽可能的熟悉内置函数的文档；
#
# ### 一些内置函数
# all(iterable)  如果可迭代对象(数组，字符串，列表等)中的元素都是true(或者为空)的话返回True
# any(iterable)  如果可迭代对象中任何一个元素为true的话返回True，为空则返回False
# dict() 使用提供的条目生成一个新的字典
# enumerate(iterable, start=0)  返回一个枚举对象。 iterable 必须是序列，iterator 或支持迭代的某个其他对象
# isinstance(object, classinfo)  如果object参数是classinfo参数的实例，或者其子类的实例，则返回true，否则返回false
# pow(x, y[, z])  计算x的y次方，以z为模
# zip(*iterables)  创建一个迭代器，聚合来自每个迭代器的元素;与*运算符结合可用于解压缩列表
