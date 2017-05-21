# -*- coding: utf-8 -*-
__author__ = 'Anliven'

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)  # seek() 函数的处理对象是字节,seek(0) 只是转到文件的 0 byte，也就是第一个 byte 的位置。

def print_a_line(line_count, f):
    print line_count, f.readline()
    # readline() 是怎么知道每一行在哪里的？
    # readline() 会扫描文件的每一个字节，直到找到一个 \n 为止，然后它停止读取文件，并且返回此前的文件内容。
    # 文件 f 会记录每次调用 readline() 后的读取位置，这样它就可以在下次被调用时读取接下来的一行。

current_file = open(input_file)
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

#rewind(current_file) # 将current_file的文件指针恢复到文件开头
# 将此行注释后，再对比下结果，理解此行的作用
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
# current_line += 1 # x += y 的意思和 x = x + y 是一样的。
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



# 用下面的方法运行程序
# >python Exercise-20 Functions and Files.py Exercise-20-sample.txt
# First let's print the whole file:
#
# This is a sample for exercise-20. Line-1
# This is a sample for exercise-20. Line-2
# This is a sample for exercise-20. Line-3
# To all the people out there.
# I say I don't like my hair.
# I need to shave it off.
# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 This is a sample for exercise-20. Line-1
#
# 2 This is a sample for exercise-20. Line-2
#
# 3 This is a sample for exercise-20. Line-3


# “+=”可以叫做加值符，可以这样使用“x += 1”，作用 和 “x = x + 1”是一样的。
# 类似的还有“-=”等等。