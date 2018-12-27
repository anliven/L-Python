# coding=utf-8
import glob

file_list = glob.glob(r'./*.py')
print(type(file_list), file_list)  # 返回的数据类型是列表

file_list2 = glob.iglob(r'./*.py')
print(type(file_list2))  # 返回的数据类型是迭代器，适用于大量文件的场景，节省内存
for file_name in file_list2:
    print(file_name)

file_list3 = glob.glob('**/*.py', recursive=True)
print(file_list3)

file_list4 = glob.glob('../[0-9].*')  # 使用相对路径和指定范围字符
print(file_list4)

# ### 标准库glob模块
# - Unix style pathname pattern expansion
# - https://docs.python.org/3/library/glob.html
# 模块glob实现了对指定路径内容进行匹配的功能；
#
# ### glob(pathname, recursive=False)
# 该函数返回一个符合条件的路径字符串列表，如果在Windows系统下，返回内容中“\”符号会自动加上转义符号变为“\\”
# - 参数pathname：需要匹配的路径字符串（支持绝对路径和相对路径），建议加上r前缀以免发生不必要的错误
# - 参数recursive：代表递归调用，与特殊通配符“**”一同使用，默认为False
#
# ### iglob(pathname, recursive=False)
# 与glob()函数作用基本相同，但返回的数据类型是迭代器，适用于大量文件的场景，节省内存；
#
# ### glob模块支持的通配符
# * 	    匹配0或多个字符
# ** 	    匹配所有文件、目录、子目录和子目录里的文件，需要设置参数“recursive=True”
# ? 	    匹配1个字符
# [exp] 	匹配指定范围内的字符，如：[1-9]匹配1至9范围内的字符
# [!exp] 	匹配不在指定范围内的字符
