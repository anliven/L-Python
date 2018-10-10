# coding=utf-8


class Rule:
    """
    所有规则的基类
    """

    def action(self, block, handler):  # 通用的操作
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):  # 标题规则
    """
    标题只包含一行，不多于70个字符且不以冒号结束
    """
    type = 'heading'  # type属性被从Rule类继承而来的方法action所使用

    def condition(self, block):
        return not ('\n' in block) and (len(block) <= 70) and not (block[-1] == ':')


class TitleRule(HeadingRule):  # 题目规则
    """
    题目是文档中的第一个文本块，前提条件是它属于标题
    """
    type = 'title'
    first = True  # 设置标志：此方法只使用一次

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):  # 列表项规则
    """
    列表项是以连字符开头的段落；
    在设置格式的过程中，将把连字符删除；
    """
    type = 'listitem'

    def condition(self, block):  # 以连字符开头的文本块
        return block[0] == '-'

    def action(self, block, handler):  # 重写方法action，删除文本块中第一个字符（连字符）并删除多余的空白
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):  # 列表规则
    """
    列表以紧跟在非列表项文本块后面的列表项开头，以相连的最后一个列表项结束
    """
    type = 'list'
    inside = False  # 当前是否位于列表内

    def condition(self, block):  # 检查所有的文本块
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):  # 段落规则
    """
    默认规则，处理不符合其他规则的文本块
    """
    type = 'paragraph'

    def condition(self, block):  # 默认使用的规则
        return True

# ### 规则
# 供主程序（解析器）使用，解析器依次尝试每个规则，并在触发一个规则后不再尝试；
# 对于每种文本块，都制定一条相应的规则（检测不同类型的文本块并相应地设置其格式），将规则定义为对象；
#   - 条件（condition）：明确适用的文本块，参数是待处理的文本块，返回布尔值（表明当前规则是否适用）
#   - 操作（action）：对文本块进行转换，参数是文本块，返回布尔值（是否结束对当前文本块的处理）
