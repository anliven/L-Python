# -*- coding: utf-8 -*-
import sys

test_List = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
print("All elements: %s" % test_List)  # 打印所有元素
print("# Elements[0]: ", test_List[0])  # 打印索引为0的元素（注意：返回元素而不是列表，所以返回值没有中括号）
print("# Elements[1:3]: ", test_List[1:3])  # 第二个索引指定的元素不包含在切片内，这里是将索引为1到2的元素作为一个列表返回
print("# Elements[3:]: ", test_List[3:])  # 切片结束于序列末尾，可省略第二个索引
print("# Elements[:2]: ", test_List[:2])  # 切片开始于序列开头，可省略第一个索引
print("# Elements[-1]: ", test_List[-1])  # 可使用负数索引从列表末尾开始计数，从右往左，“-1”是最后一个元素的索引
print("# Elements[-3:-1]: ", test_List[-3:-1])  # 第二个索引指定的元素不包含包含在切片内
print("# Elements[:-1]: ", test_List[:-1])  # 排除最后一个元素（打印从开始到倒数第2个元素）
print("# Elements[0:10:2]: ", test_List[0:10:2])  # 显示指定切片的起点、终点和步长，步长默认为1
print("# Elements[2::2]: ", test_List[2::2])  # 从第2个索引开始每隔2个元素打印
print("# Elements[:8:2]: ", test_List[:8:2])  # 从序列开头到第8个索引之间，每隔2个元素打印
print("# Elements[::4]: ", test_List[::4])  # 从序列开头每隔3个元素打印
print("# Elements[0:10:-2]: ", test_List[0:10:-2])  # 步长为负数时，第一个索引必须比第二个索引大，否则将为空序列
print("# Elements[0:10:-2]: ", test_List[10:0:-2])  # 步长为负数时，从右向左提取元素
print("# Elements[5::-2]: ", test_List[5::-2])  # 省略结束索引
print("# Elements[:5:-2]: ", test_List[:5:-2])  # 省略起始索引
print("# Elements[:]: ", test_List[:])  # 复制整个序列，可省略两个索引
print("# Elements[-3:0]: ", test_List[-3:0])  # 空序列（第一个索引位于第二个索引之后）
print("# Elements[::-1]: ", test_List[::-1])  # 反序打印所有元素

test_List2 = ['AAA', 'BBB', 'CCC', 'DDD']
a, b, c, d = test_List2  # 列表的拆分
e, *f, g = test_List2  # 列表的拆分
print("# list split: ", a, b, c, d, e, f, g)
print("# list*n: ", test_List2 * 2)  # 列表重复，生成一个新列表
print("# list1 + list2: ", test_List + test_List2)  # 列表拼接
print("# obj in list: ", 'EEE' in test_List2)  # 成员资格：判断元素是否在列表中
print("# max(list): ", max(test_List2))  # 列表中最大的元素
print("# min(list): ", min(test_List2))  # 列表中最小的元素
print("# len(list): ", len(test_List2))  # 列表包含的元素个数
print("# list.count(obj)：", test_List2.count("AAA"))  # 计算元素在列表出现的次数
for _ in test_List2:  # 列表迭代
    print("item:", _)
for item in test_List2:  # 列表迭代
    print("item:", item, sep="-", end=' ')
print('\n')

test_List3 = []  # 创建空列表
test_List3.insert(0, "bbb")  # 在指定下标位置，插入元素
test_List3.append('aaa')  # 列表尾部添加元素
test_List3.sort()  # 对列表进行排序，影响列表本身，而不是返回一个修改过的列表
print("All elements: %s" % test_List3)
del test_List3[1]  # 删除元素
test_List3.pop(0)  # 删除元素
print("All elements: %s" % test_List3)

test_List4 = [None] * 10  # 创建包含10个None元素的列表
test_List4[0] = 111  # 通过索引直接修改元素值
print("All elements: %s" % test_List4)

test_List5 = ["aaa", 111, ["BBB", ["CCC", "DDD"], "222"], "EEE"]  # 嵌套的列表
print(test_List5[2][1])  # 访问嵌套的列表
print(test_List5[-2][-2])


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


print_lol(test_List5, True, 2)
print_lol(test_List5)

# ### 列表（List）
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
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
# - count(obj)：计算obj在列表出现的次数
# - insert(index,obj)：在下标为index的位置，插入obj
# - append()：添加元素到列表末尾；可以向列表中添加任何类型的对象，包括数字，甚至是其它列表；
# - clear()：就地清空列表内容；
# - sort()：对列表进行排序，影响列表本身，而不是返回一个修改过的列表；
# - del语句从列表中移除对应的元素；
# - extend()：可将多个值组成的序列附加到列表末尾，返回一个全新的列表；
# - index()：在列表中查找指定值第一次出现的索引；
# - pop()：删除list末尾的元素；pop(i)方法删除指定位置的元素，其中i是索引位置；
# - remove()：删除第一个为指定值的元素；
# - copy()：复制列表，得到一个相同内容的全新列表，等同于“L2=list(L)”；
# - help(list)：获取List类的更多信息；
#
# ### “_”符号的用法
# - 表示交互解释器中最后一次执行语句的返回结果；
# - 作为名称使用，例如在循环中作为特定名称；
# - 作为函数名，但可能会和上一种用法冲突，应避免同时使用；
# 
# ### 递归嵌套列表
# 递归函数不需要任何改变就可以正确处理任意深度的嵌套列表；
# Python3默认递归深度不能超过100；
