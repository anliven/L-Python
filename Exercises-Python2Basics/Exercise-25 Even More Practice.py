# -*- coding: utf-8 -*-
__author__ = 'Anliven'

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # 字符串的split（）函数：这里是' '为分割符切片字符串stuff，返回一组使用分隔符分割字符串形成的列表。
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # 用built-in函数sorted（）对列表进行排序

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # 列表的pop（） 函数：移除列表中的第一个元素，并且返回该元素的值
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # 列表的pop（） 函数：移除列表中的最后一个元素（默认最后一个元素），并且返回该元素的值
    return word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #调用了前面刚定义的break_words()函数
    return sort_words(words) #调用了前面刚定义的sort_words()函数

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    return print_first_word(words),print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    return print_first_word(words),print_last_word(words)

sentence = "All good things come to those who wait."
words = break_words(sentence)

print break_words(sentence)
print sort_words(words)
print print_first_word(words)
print print_last_word(words)
print sort_sentence(sentence)

print print_first_and_last(sentence)
print print_first_and_last_sorted(sentence)


# 命令行下执行help（模块名）或help（模块名.方法名）会得到对应的帮助文档信息
# 函数的帮助文档就是定义函数时放在 """ 之间的内容，也被称作 documentation comments （文档注解）。
# “from 模块名 import *”可以导入模块的所有函数方法

#如果函数打印出来的结果是None，请检查函数是否漏写了最后的return语句

#想要打印到屏幕，那就使用 print ，如果是想返回值，那就是用 return 。

# 关于split 和 join 方法
# 只针对字符串进行处理。split:拆分字符串、join连接字符串
# string.join(sep): 以string作为分割符，将sep中所有的元素(字符串表示)合并成一个新的字符串
# string.split(str=' ',num=string.count(str)): 以str为分隔，符切片string，如果num有指定值，则仅分隔num个子字符串。

# Python内置的排序函数sorted（）可以对list或者iterator（迭代器）进行排序。
