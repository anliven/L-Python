# -*- coding: utf-8 -*-
import os
import sys
import fileinput

testFile = 'test.txt'
f = open(testFile, 'w', encoding="utf-8")
print("This is a test!", file=f)  # 利用print函数的file参数，写入数据到文件
print('1st line', '111', file=f)
print('2nd line', '222', file=f)
print('3rd line', '333', 'Final', file=f)
f.close()

lines = list(open(testFile))  # 转换为字符串列表
print("# lines:", lines)

first, second, *third = open(testFile)  # 解包
print("# first:{} -- second:{} -- third:{}".format(first.strip(), second.strip(), third))

for line in open(testFile):  # 在不将文件对象赋给变量的情况下迭代文件
    print("## lines:", line.strip())


testFile2 = 'test2.txt'
testText = '''Action is the antidote to despair!'''
with open(testFile2, 'w', encoding="utf-8") as f:
    f.write(testText)
with fileinput.input(files=(testFile, testFile2)) as f:
    for line in f:
        print("# multi-files input: ", line.strip())

os.remove(testFile)
os.remove(testFile2)

print("## Enter something or quit: ")
for line in sys.stdin:  # 迭代标准输入
    print("# sys.stdin:", line)
    if str(line.strip()) == "quit":  # strip()删掉末尾的'\n'
        break

# ### 像迭代器一样操作文件
# 对迭代器的操作基本上也适用于文件对象；
#
# ### 标准库fileinput模块
# - Iterate over lines from multiple input streams
# - https://docs.python.org/3/library/fileinput.html
# - 源码文件: Python安装目录\Lib\fileinput.py；
# fileinput模块可以对一个或多个文件中的内容进行迭代、遍历等操作；
#
# ### 迭代标准输入（sys.stdin）
# 与文件一样，标准输入也是可迭代的；
