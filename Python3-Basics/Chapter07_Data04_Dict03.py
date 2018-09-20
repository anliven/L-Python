# coding=utf-8
from collections import ChainMap

a = {'aaa': 111, 'bbb': 222}
b = {'bbb': 2, 'ccc': 333}
c = {'ddd': 444, 'bbb': 555}

# 方法1
d = ChainMap(a, b, c)
print(d)
print("keys:", list(d.keys()), "values:", list(d.values()))
print("key-bbb:", d['bbb'])  # 如果字典中有相同的键，默认使用第一个字典中的键值
d['aaa'] = 100  # 改变合并后键的值，合并前字典中的值也会改变
print("dict-a:", a)

# 方法2
e = {**a, **b, **c}
print(e)
e['aaa'] = 666  # 改变合并后键的值，合并前字典中的值不会改变
print("dict-a:", a)


# 方法3
def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


print(merge_dicts(a, b))
print(merge_dicts(a, b, c))

# ### 合并字典
# 方法1：使用collections模块中的ChainMap合并多个字典
# - 可在逻辑上将多个字典合并为一个字典；
# - 没有真正创建字典，只是在内部创建了一个列表来容纳这些字典并重新定义了一些常见的字典操作；
# - 如果合并前字典中有相同的键，合并后默认使用第一个字典中的键值；
# - 改变合并后键的值，合并前字典中的值也会改变；
#
# 方法2：简便方式（Python3.5及以后版本）
# - 创建了一个新的字典；
# - 如果合并前字典中有相同的键，合并后默认使用最后一个字典中的键值；
# - 改变合并后键的值，合并前字典中的值不会改变;
#
# 方法3：利用update方法
# - 创建了一个新的字典；
# - 如果合并前字典中有相同的键，合并后默认使用最后一个字典中的键值；
# - 改变合并后键的值，合并前字典中的值不会改变;
