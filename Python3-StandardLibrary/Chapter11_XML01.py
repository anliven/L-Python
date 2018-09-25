# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate


# SAX解析XML


def start_element(name, attrs):
    print('Start element:', name, attrs)


def end_element(name):
    print('End element:', name)


def char_data(data):
    print('Character data:', repr(data))


xml = r"""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>"""

parser = ParserCreate()
parser.StartElementHandler = start_element
parser.EndElementHandler = end_element
parser.CharacterDataHandler = char_data
parser.Parse(xml, 1)

# 通过拼接字符串生成XML内容
x = []
x.append(r'<?xml version="1.0"?>')
x.append(r'<root>')
x.append('  some & data')
x.append(r'</root>')
print('\n'.join(x))

# ### xml package
# - XML Processing Modules
# - https://docs.python.org/3/library/xml.html
#
# ### 标准库xml.parsers.expat模块
# - Fast XML parsing using Expat
# - https://docs.python.org/3/library/pyexpat.html
#
# ### 操作XML的两种方法
# - DOM：将整个XML读入内存，解析为树，可以任意遍历树的节点；占用内存大，解析慢；
# - SAX：流模式(边读边解析)，占用内存小，解析快；需要自己处理事件；
# - 正常情况下，优先考虑SAX；
# - 如果生成复杂的XML，建议使用JSON；
