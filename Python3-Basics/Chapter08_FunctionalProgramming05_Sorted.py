#! python3
# -*- coding: utf-8 -*-

list_sample = [666, 555, -111, 999, -222]
print(sorted(list_sample))
print(sorted(list_sample, key=abs))  # ？
print(list_sample)

list_sample2 = ['bbb', 'aaa', 'ccc', 'ZZZ', 'XXX', 'YYY']
print(sorted(list_sample2))
print(sorted(list_sample2, key=str.lower))  # 忽略大小写排序
print(sorted(list_sample2, key=str.lower, reverse=True))  # 忽略大小写反向排序

list_sample3 = [('BBB', 77), ('AAA', 99), ('RRR', 66), ('LLL', 88)]

s = 'asdf234GDSdsf23'  # 自定义规则对字符串排序：小写<大写<奇数<偶数；
print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))))
# Boolean值的排序：False在前，True在后
# x.isdigit()  把数字放前,字母放后；
# x.isdigit() and int(x) % 2 == 0  奇数在前，偶数在后；
# x.isupper()  字母小写在前，大写在后；
# x  对所有类别数字或字母排序；


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


print('Sorted by name: ', sorted(list_sample3, key=by_name))
print('Sorted by score: ', sorted(list_sample3, key=by_score, reverse=False))  # reverse=False为升序排序

# ### sorted函数
# Python内置的sorted()函数可以对list进行排序,返回一个新的列表，不改动原先列表；
# 可以接收一个key函数来实现自定义的排序，key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序；
# 对字符串排序，默认是按照ASCII的大小进行比较，但可以通过key函数实现自定义的排序；
# 使用sorted()排序的关键在于实现一个映射函数；
#
# ### 对比sort()函数
# - 对于一个无序的列表a，调用a.sort()，对a进行排序后返回a，sort()函数修改原列表内容；
# - 对于一个无序的列表a，调用sorted(a)，对a进行排序后返回一个新的列表，而对原列表内容不产生影响；
#
# - 当列表由list（或者tuple）组成时，默认情况下，sort和sorted都会根据list[0]（或者tuple[0]）作为排序的key，进行排序;
