# coding=utf-8
import sys
import re
import simple_util

print('<html><title>This is a test!</title><body>')

title = True
for block in simple_util.blocks(sys.stdin):  # 从标准输入sys.stdin读取
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)  # 调用re.sub实现过滤器
    if title:
        print('<h1>')  # 打印一级标题标签
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')  # 打印段落标签
        print(block)
        print('</p>')

print('</body></html>')


# ### 脚本实现的功能
# 给纯文本文件添加格式，得到可作为网页的文档，在Web浏览器中正常显示；
# - 将文本内容分成可独立处理的文本块（block）
# - 再依次对每个文本块应用一个过滤器（通过调用re.sub实现）
#
# ### 脚本使用方式
# >python simple_markup.py <test_input.txt> test_output.html
#
# ### 一种扩展方式
# 可在for循环中添加检查，以确定文本块是否是标题、列表项等，并添加其他的正则表达式实现内容过滤；
# 但此扩展方式可能会导致代码混乱，而且无法输出其他格式的文档；
