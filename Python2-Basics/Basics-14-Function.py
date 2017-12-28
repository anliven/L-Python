# -*- coding: utf-8 -*-
__author__ = 'Anliven'


def print_all(f):
    """

    :param f:
    """
    print (f.read())


def rewind(f):
    """

    :param f:
    """
    f.seek(0)  # seek(0)转到文件的 0 byte(第一个 byte 的位置)


def print_a_line(line_count, f):
    """

    :param line_count:
    :param f:
    """
    print (line_count), (f.readline())  # readline()扫描并返回文件的每一个字节，直到遇到“\n”为止
    # 文件f会记录每次调用readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行


input_file = "Basics-sample03.txt"
current_file = open(input_file)
print ("First let's print the whole file:\n")
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")
rewind(current_file)  # 将current_file的文件指针恢复到文件开头;将此行注释后，再对比下结果，理解此行的作用

print ("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
