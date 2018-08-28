# -*- coding: utf-8 -*-

test_str = "aaa,111,---,###"
print(list(test_str))  # 字符串转换为列表 - list()函数
print(test_str.strip().split(','))  # 字符串转换为列表 - 字符串的strip().split()方法

testlist = list("ABC")
testlist[3:] = list("123")  # 切片赋值
testlist[3:3] = ['a', 'b', 'c']  # 使用切片赋值来插入新元素
testlist[1:8] = []  # 使用切片赋值来删除元素
print(testlist)

test_list = ["Hello", "Python", '!']
print("".join(test_list))  # 列表转换为字符串 - 针对所有元素为str类型的列表
print(" ".join(test_list))  # 用空格分割

test_list2 = ["Hello", "Python", 2018, '!']
out_str = ""
for item in test_list2:  # 列表转换为字符串
    out_str = out_str + str(item) + " "
print(out_str)

test_list3 = [2222, 555, 777, 333, 6666, 999, 4444, 111, 8888]
print(sorted(test_list3, reverse=True))  # 获得排序后列表的副本
print("# test_list: ", test_list3)
test_list3.sort()  # 就地排序列表中的元素
print("# test_list: ", test_list3)
test_list3.reverse()  # 就地反序列表中的元素
print("# test_list: ", test_list3)

str1 = "2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22"
str2 = "2.59,2.11,2:11,2:23,3-10,2-23,3:10,3.21,3-21"
str3 = "2:22,3.01,3:01,3.02,3:02,3.02,3:22,2.49,2:38"


def sanitize(time_string):  # 字符替换
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    mins, secs = time_string.split(splitter)
    return mins + '.' + secs


def test(in_str):  # 字符串转换成有序列表
    return sorted([sanitize(t) for t in in_str.strip().split(',')])


def unique_top3_items(in_list):  # 列表去重
    unique_items = []
    for i in in_list:
        if i not in unique_items:
            unique_items.append(i)
    return unique_items[0:3]


print(unique_top3_items(test(str1)))
print(unique_top3_items(test(str2)))
print(unique_top3_items(test(str3)))

print(sorted(set([sanitize(t) for t in str1.strip().split(',')]))[0:3])  # 利用set()去除列表的重复项
print(sorted(set([sanitize(t) for t in str2.strip().split(',')]))[0:3])
print(sorted(set([sanitize(t) for t in str3.strip().split(',')]))[0:3])

print(list(set(['123', 'abc', '123', '123'])))  # 通过集合set()去除列表的重复项

for i, n in enumerate(['aaa', 'bbb', 'ccc']):  # enumerate函数得到索引值和对应值
    print(i, n)

# ### 方法串链（method chaining）
# 多个方法串联在一起，可以简化代码书写；
#
# ### 列表排序方式
# 原地排序（In-place sorting）：排序后的数据替换原来的数据，sort()方法实现；
# 复制排序（Copied sorting）: 排序后返回的是原数据的一个有序副本，原数据不发生改变，内置sorted()函数实现；
# sort()方法和sorted()内置函数的参数reverse可以指定升序降序，默认都按升序排列（reverse=False）；
