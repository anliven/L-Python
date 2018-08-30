# -*- coding: utf-8 -*-
import string

print(string.digits)

test_string = "  # abc123ABC 123ABC ABC #  "
print("# center: ", test_string.center(30, "#"))
print("# find: ", test_string.find("ABC", 10, 20))  # 可指定搜索的起点和终点，默认是整个字符串

print("# join: ", "+".join(test_string))  # 可指定连接符
print("# split: ", test_string.split("123"))  # 可指定分隔符，默认为空白字符
print("# capwords: ", string.capwords(test_string, "123"))  # 实现词首大写，默认分隔符为空格

print("# lower: ", test_string.lower())
print("# upper: ", test_string.upper())

print("# strip: ", test_string.strip())
print("# strip: ", test_string.strip(" #"))  # 可指定删除字符

print("# replace: ", test_string.replace("ABC", "456"))
table = str.maketrans("123", "@@@")  # 使用translate前必须创建一个转换表
# print(table)  # 转换表的内容其实是Unicod编码之间的映射
print("# maketrans: ", test_string.translate(table))
print("# maketrans: ", test_string.translate(str.maketrans("123", "@@@", " #")))  # 可指定要删除的字符

print("# isspace: ", test_string.isspace())
print("# isdigit: ", test_string.isdigit())
print("# isupper: ", test_string.isupper())

# ### 字符串方法
# - 模块string：https://docs.python.org/3/library/string.html
# - help(str)获取String类的更多信息；
#
# ### 一些字符串常量
# - string.digits          ： 数字0到9
# - string.ascii_letters   ： 所有ASCII字母（大小写）
# - string.ascii_lowercase ： 所有ASCII字母（小写）
# - string.ascii_uppercase ： 所有ASCII字母（大写）
# - string.printable       ： 所有可打印的ASCII字符
# - string.punctuation     ： 所有ASCII标点字符
#
# ### 一些字符串方法
# - center : 通过在字符串前后填充字符（默认为空格）让字符串居中；
# - find ： 在字符串中查找子串，如果找到就返回子串的第一个字符的索引，否则返回-1；
# - join ： 用于合并序列的元素；
# - split : 将字符串拆分为序列；
# - capwords：将指定分隔符后每项的首字母大写，默认分隔符为空格
# - lower ： 返回字符串的小写版本；
# - upper ： 返回字符串的大写版本；
# - strip : 删除字符串开头和末尾的空白（但不包括中间的空白）；
# - replace : 将指定子串替换成另一个字符串；
# - translate : 单字符替换字符串中特定部分；
# - isspace: 是否全为空格；
# - isdigit: 是否全为数字；
# - isupper: 是否全为大写；
# - ......
