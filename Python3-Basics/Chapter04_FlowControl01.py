# -*- coding: utf-8 -*-

x, y, z = 111, 222, 333  # 同时给多个变量赋值
x, y, z = z, y, x  # 同时交换多个变量的值
print("x:{} --- y:{} --- x:{}".format(x, y, z))

values = 123, 456, 789  # 创建元组
a, b, c = values  # 元组解包
print("values:{} --- a:{} --- b:{} --- c:{}".format(values, x, y, z))

values2 = {'AAA': 123, 'BBB': 456, 'CCC': 789}
k, v = values2.popitem()  # 随机获取字典的一个键值对，以元组形式返回，然后进行序列解包赋值
print("k:{} --- v:{}".format(k, v))

L1, L2, *L3 = [111, 222, 333, 444, 555]  # 列表解包
print("L1:{} --- L2:{} --- L3:{}".format(L1, L2, L3))
S1, *S2, S3 = "abc123ABC"  # 字符串解包
print("S1:{} --- S2:{} --- S3:{}".format(S1, S2, S3))

V1 = V2 = V3 = "test"  # 链式赋值
print("V1:{} --- V2:{} --- V3:{}".format(V1, V2, V3))

T = "Test"
T += "Me"  # 增强赋值，适用于所有标准运算符
T *= 2
print(T)

list1 = list2 = [111, 222, 333]
list3 = [111, 222, 333]
print(list1 == list2, list1 is list2, list1 == list3, list1 is list3)  # “==”与“is”的区别

num = 666
assert 0 < num < 1000, ""
assert num < 500, "The number is bigger than 500."  # 可添加说明字符串

# ### 序列解包(可迭代对象解包)
# 将一个序列（或任何可迭代对象）解包，并将得到的值存储到一系列变量中；
# - 进行解包的序列元素个数必须与变量个数相同；
# - 使用星号运算符可收集余下的值（序列元素个数可以与变量的个数不同）；
# - 特别注意：带星号的变量是一个列表；
#
# ### 链式赋值
# 简捷地将多个变量关联到同一个值；
#
# ### 增强赋值
# 简化标准运算符的使用，使代码更加简洁紧凑，可读性强；
#
# ### 比较运算符
# < （小于）：返回x是否小于y；所有的比较运算符返回的结果均为首字母大写的True或False；
# > （大于）：返回x是否大于y；
# <= （小于等于）：返回x是否小于或等于y；
# >= （大于等于）：返回x是否大于或等于y；
# == （等于）：比较两个对象是否相等；
# != （不等于）：比较两个对象是否不相等；
# 同一性测试（是否是同一个对象）：is, is not;
# 成员测试（是否是容器的成员）：in, not in;
# 特别注意：“==”检查两个对象是否相等，“is”检查两个对象是否相同（同一个对象）；
#
# ### 布尔运算符
# not （布尔“非”）：如果x是True，则返回False；如果x是False，则返回True；
# and （布尔“与”）：如果x是False，则返回False，否则返回y的计算值；适用短路计算（Short-circuit Evaluation）；
# or （布尔“或”）：如果x是True，则返回True，否则它将返回y的计算值；适用短路计算；
#
# ### 断言（assert）
# 可使用关键字assert来验证指定条件是否得到满足，充当检查点；
