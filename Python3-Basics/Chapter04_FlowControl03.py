# -*- coding: utf-8 -*-

L1 = ['aaa', 'bbb', 'ccc']
L2 = [111, 222, 333]
print(zip(L1, L2), list(zip(L1, L2)))  # zip函数的返回值是一个迭代对象，可用list将其转换为列表
for k, v in zip(L1, L2):
    print("{} --- {}.".format(k, v))

S = "abc123ABC123abcABC"
for index, string in enumerate(S):  # 使用内置函数enumerate()可在迭代时同时获取索引
    if 'B' in string:
        print("string:{} - index:{}".format(string, index))

L = ['aaa', 'bbb', 'ccc', 'ddd', 'ccc']
for index, value in enumerate(L):
    print("index:{} - value:{}".format(index, value))
    if 'ccc' in value:
        print("# Found:", value, index)

print(list(reversed("Hello, Python3!")))  # 内置函数reversed()支持反向迭代
print("".join(reversed("Python3")))

# ### 并行迭代
# 内置函数zip支持并行迭代，可将两个序列“缝合”并返回一个有元组组成的序列；
# 内置函数zip可“缝合”任意数量的序列；
# 特别注意：序列的长度不同时，内置函数zip将在最短的序列用完后停止“缝合”；
#
# ### 迭代时获取索引
# 使用内置函数enumerate可在迭代时同时获取索引；
#
# ### zip()
# https://docs.python.org/3/library/functions.html#zip
# 内置函数zip()用于创建一个迭代器，聚合来自每个迭代器的元素；
#
# ### list()
# https://docs.python.org/3/library/functions.html#func-list
# 内置函数list()用于将一个可迭代对象转换为列表；
#
# ### enumerate()
# https://docs.python.org/3/library/functions.html#enumerate
# 内置函数enumerate()用于返回一个枚举对象(enumerate object);
#
# ### reversed()
# https://docs.python.org/3/library/functions.html#reversed
# 内置函数reversed()用于返回一个方向的迭代器，可用于任何序列和可迭代对象，而且不就地修改原对象；
