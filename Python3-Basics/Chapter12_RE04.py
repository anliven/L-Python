# coding=utf-8
import fileinput
import re

lines = []
for line in fileinput.input(files=('Chapter12_RE04_magus.txt', 'Chapter12_RE04_template.txt')):  # 逐行读取所有行
    lines.append(line)  # 以扩展方式放置在同一个列表
text = ''.join(lines)  # 合并为一个字符串

field_pat = re.compile(r'\[(.+?)\]')  # 定义一个用于匹配字段的模式：匹配方括号中的字段
scope = {}  # 创建一个用作模板作用域的字典：存储变量


def replacement(match):  # 定义一个替换函数
    code = match.group(1)  # 从match中获取与编组1匹配的内容，并存储到变量code中
    # print("# code: ", code)
    try:
        # print("# eval: ", str(eval(code, scope)))
        return str(eval(code, scope))  # 将作用域字典scope作为命名空间，并尝试计算code，然后将结果以字符串形式返回
    except SyntaxError:  # code不是表达式，引发SyntaxError异常
        # print("# exec: ", exec(code, scope))
        exec(code, scope)  # 在作用域字典scope中执行这个字段
        return ''  # 赋值语句没有结果，返回空字符串


print(field_pat.sub(replacement, text))  # 在re.sub中使用替换函数来替换所有与field_pat匹配的字段，并打印结果

# ### 模板（template）
# 可在模板文件中插入具体的值来获得最终符合需求的文本；
# 通过字符串格式设置和正则表达式可以定制功能更为实用的模板；
#
# ### 命令行运行示例
# 在fileinput.input()不使用files参数指定文件；
# >>python Chapter12_RE04.py Chapter12_RE04_sample.txt
# >>python Chapter12_RE04.py Chapter12_RE04_magus.txt Chapter12_RE04_template.txt
