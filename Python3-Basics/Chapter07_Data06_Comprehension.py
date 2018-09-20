# -*- coding: utf-8 -*-


def squared(x):
    return x * x


# 示例：列表推导式及生成器
li = range(1, 15)
test_list = [i * 2 for i in li if i % 3 == 0]  # 先满足if语句，然后满足for语句，最后满足元素表达式
print(test_list)
test_list2 = [squared(i) for i in li if i % 3 == 0]
print(test_list2)
test_list3 = (squared(i) for i in li if i % 3 == 0)  # 使用()得到生成器generator
print(test_list3)

# 示例：字典推导式
di = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
test_dict = {v: k for k, v in di.items()}  # 使用大括号{}，这里实现了交换字典的键值
print(test_dict)

# 示例：集合推导式
se = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]  # 列表
test_set = {i * 2 for i in se}  # 使用大括号{}，返回一个不包含重复元素的集合
print(test_set)

# ### 推导式（Comprehension）
# 推导式，也称为解析式，是一种简洁方便创建列表、字典、集合的方法；
# 对应的，推导式可分为列表推导式、字典推导式、集合推导式三种；
# 对整个列表、字典、集合的全部内容依次做相同的操作，并返回一个新的列表、字典、集合；
#
# ### 集合推导式（set comprehension）与列表推导式的区别
# - 表达式使用大括号；
# - 返回一个不包含重复元素的集合；
