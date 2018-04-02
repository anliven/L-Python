#! python3
# -*- coding: utf-8 -*-
import sys

L = []  # 创建空列表

test_List = ["Hello", "Python", 'World', 2018, '!']
print("All elements: %s" % test_List)  # 打印所有元素
print("# Elements: ", test_List[1])  # 打印索引为1的元素（注意：返回元素而不是列表，所以返回值没有中括号）
print("# Elements: ", test_List[1:3])  # 打印索引为1到2的元素，作为一个列表返回
print("# Elements: ", test_List[3:])  # 从索引为3的元素开始，打印后续的所有元素
print("# Elements: ", test_List[:2])  # 从开始到第1个元素
print("# Elements: ", test_List[:-1])  # 从开始到倒数第2个元素
print("# Elements: ", test_List[::-1])  # 反序打印所有元素
test_List[4] = 2018  # 直接赋值，修改列表的元素值
print(test_List)

test_List2 = ['apple', 'mango', 'carrot', 'banana']
a, b, c, d = test_List2
print(a, b, c, d)  # 列表的拆分
print(test_List2 * 2)  # list*n：列表重复，生成一个新列表
print(test_List + test_List2)  # list1+list2：列表拼接
print('apple' in test_List2)  # obj in list：判断元素是否在列表中
print(max(test_List2))  # max(list)：返回列表最大值
print(test_List2.count("orange"))  # list.count(obj)：计算obj在列表出现的次数
print(len(test_List2))  # len(list)：列表元素个数
test_List2.insert(0, "orange")  # list.insert(index,obj)：在下标为index的位置，插入obj
test_List2.append('rice')  # list.append(obj)：列表尾部添加元素obj
print(test_List2)
test_List2.sort()  # list.sort()：对列表进行排序，影响列表本身，而不是返回一个修改过的列表
print(test_List2)
del test_List2[0]
test_List2.pop(0)  # pop()方法删除元素
print(test_List2)
for item in test_List2:  # 列表迭代
    print(item, end=' ')
print('\n')

test_List3 = ["aaa", 111, ["BBB", ["CCC", "DDD"], "222"], "EEE"]  # 嵌套的列表
print(test_List3[2][1])  # 访问嵌套的列表
print(test_List3[-2][-2])


def print_lol(a_list, indent=False, level=0, fh=sys.stdout):  # 遍历嵌套的列表；sys.stdout是“标准输出”
    """Prints each item in a list, recursively descending into nested lists (if necessary)."""

    for each_item in a_list:
        if isinstance(each_item, list):  # isinstance()判断是否是某个指定类型的数据对象
            print_lol(each_item, indent, level + 1, fh)  # 调用自身
        else:
            if indent:
                for l in range(level):
                    print("\t", end='', file=fh)  # 每一层缩进显示一个TAB制表符
            print(each_item, file=fh)


print_lol(test_List3, True, 2)
print_lol(test_List3)

# ### 列表（List）
# - 列表是一种有序元素的集合，可以随时添加和删除其中的元素；
# - 使用方括号[]声明列表；定义格式：list = [obj1,obj2,obj3,…]；
# - 列表中元素的类型可以不相同，支持数字、字符串、列表（嵌套）；
# - 列表是一种可变的（Mutable）数据类型，可以添加、移除或搜索列表中的元素；
#
# ### 访问列表
# - 通过索引（Indexing）运算符访问列表中的元素（特别注意：Python从0开始计数！）；
# - 列表截取的语法格式：变量[头下标:尾下标]，范围是“前开后闭”（不包括尾下标的元素）；
# - 可以用负整数做索引，例如用-1做索引，直接获取最后一个元素；
# - 当索引超出了范围时会报IndexError错误，最后一个元素的索引是“len(list) - 1”；
#
# ### 列表常用方法
# - 使用for...in循环来遍历列表中的元素；
# - len(list)：列表元素个数
# - list.count(obj)：计算obj在列表出现的次数
# - list.insert(index,obj)：在下标为index的位置，插入obj
# - append()：向列表中添加元素；可以向列表中添加任何类型的对象，包括数字，甚至是其它列表；
# - sort()：对列表进行排序，影响列表本身，而不是返回一个修改过的列表；
# - del语句从列表中移除对应的元素；
# - pop()：删除list末尾的元素；pop(i)方法删除指定位置的元素，其中i是索引位置；
# - copy()：复制列表，得到一个相同内容的全新列表，等同于“L2=list(L)”；
# - help(list)：获取List类的更多信息；
#
# ### 递归嵌套列表
# 递归函数不需要任何改变就可以正确处理任意深度的嵌套列表；
# Python3默认递归深度不能超过100；
