# coding=utf-8
from xml.sax.handler import ContentHandler
from xml.sax import parse


class HeadlineHandler(ContentHandler):  # 简单的XML解析器，实现必要的事件处理
    """简单的内容处理"""
    in_headline = False  # 使用布尔变量来充当指示

    def __init__(self, headlines):
        super().__init__()
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):  # 元素开始（遇到起始标签）
        if name == 'h1':
            self.in_headline = True  # 发现标签为h1时设置为True

    def endElement(self, name):  # 元素结束（遇到结束标签）
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False  # 发现标签为h1时设置为False

    def characters(self, string):  # 普通文本（字符）
        if self.in_headline:
            self.data.append(string)


HeadLines = []
parse('website.xml', HeadlineHandler(HeadLines))  # 函数parse读取需要解析的XML文件并生成事件
print("The following <h1> elements were found:")
for h in HeadLines:
    print(h)

# ### XML
# XML是一组定义一类语言的规则，可用来表示各种类型的数据；
#
# ### XML Processing Modules
# https://docs.python.org/3/library/xml.html
# - xml.sax（Support for SAX2 parsers）：https://docs.python.org/3/library/xml.sax.html
# - xml.sax.handler（Base classes for SAX handlers）：https://docs.python.org/3/library/xml.sax.handler.html
#
# ### 操作XML的两种方法
# - DOM（文档对象模式）：将整个XML读入内存，解析为树，可以任意遍历树的节点；占用内存大，解析慢；
# - SAX（Simple API for XML）：流模式(边读边解析)，占用内存小，解析快；需要自己处理事件；
# - 正常情况下，优先考虑SAX；
# - 如果生成复杂的XML，建议使用JSON；
