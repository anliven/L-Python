# coding=utf-8
import sys
import re
import handlers
import util
import rules


class Parser:  # 解析器，使用一个处理程序和一系列规则和过滤器将纯文本文件转换为带标记的文件
    """
    读取文本文件，应用规则并控制处理程序的解析器
    """

    def __init__(self, hand):  # 构造函数完成准备工作
        self.handler = hand
        self.rules = []
        self.filters = []

    def add_rule(self, rule):  # 添加规则
        self.rules.append(rule)

    def add_filter(self, pattern, name):  # 添加过滤器
        def filtering(block, hand):
            return re.sub(pattern, hand.sub(name), block)

        self.filters.append(filtering)

    def parse(self, file):  # 对文件进行解析
        self.handler.start('document')
        for block in util.blocks(file):  # 迭代文本文件中多有文本块
            for f in self.filters:  # 应用过滤器，调用函数filter
                block = f(block, self.handler)  # 以文本块和处理程序作为参数赋值给变量block
            for rule in self.rules:  # 应用规则
                if rule.condition(block):  # 检查规则是否适用
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')


class BasicTextParser(Parser):  # 使用正则表达式来处理内嵌元素
    """
    在构造函数中添加规则和过滤器的Parser子类
    """

    def __init__(self, hand):
        Parser.__init__(self, hand)
        self.add_rule(rules.ListRule())
        self.add_rule(rules.ListItemRule())
        self.add_rule(rules.TitleRule())
        self.add_rule(rules.HeadingRule())
        self.add_rule(rules.ParagraphRule())

        self.add_filter(r'\*(.+?)\*', 'emphasis')  # 过滤器（正则表达式），找出要突出的内容
        self.add_filter(r'(http://[\.a-zA-Z/]+)', 'url')  # 过滤器（正则表达式），找出URL
        self.add_filter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')  # 过滤器（正则表达式），找出Email


handler = handlers.HTMLRenderer()
parser = BasicTextParser(handler)  # 创建一个Parser对象并添加相关的规则和过滤器
parser.parse(sys.stdin)  # 解析sys.stdin

# ### 程序说明
# 将功能放在独立的组件中，可以调高程序的模块化程度，进而提高可扩展性；
# 采取面向对象设计，进行一些抽象，可以让复杂的程序易于管理；
# - 处理程序：handlers.py，供解析器来生成输出，生成不同的标记
# - 文本块生成：util.py
# - 规则：rules.py，对于不同类型的文本块制定并应用相应的规则
# - 过滤器：未实现单独的类，用一个正则表达式和名称表示一个过滤器
# - 主程序（解析器）：markup.py，添加一个读取文本并管理其他类的对象，
#
# ### 主程序（解析器）
# 根据给定的文本块选择合适的规则来对其进行必要的装换
#
# ### 脚本使用方式
# >python simple_markup.py <test_input.txt> test_output.html
