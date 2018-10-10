# coding=utf-8


class Handler:  # 处理程序的超类，负责处理一些管理性地细节
    """
    Parser将对每个文本块调用方法start和end，并将合适的文本块名称作为参数；
    方法sub将用于正则表达式替换，使用诸如‘emphasis’等名称调用时，这个方法将返回相应的替换函数；
    """

    def callback(self, prefix, name, *args):  # 负责根据指定的前缀和名称查找相应的方法
        method = getattr(self, prefix + name, None)  # 使用getattr并将默认参数设置为None
        if callable(method):
            return method(*args)  # 如果gettart返回的对象是可调用的，就通过参数*args来调用

    def start(self, name):  # 使用前缀start_调用callback
        self.callback('start_', name)  # 检查是否实现了相应的方法，如果没有实现，就什么都不做

    def end(self, name):  # 使用前缀end_调用callback
        self.callback('end_', name)

    def sub(self, name):  # 返回一个函数作为替换函数传递给re.sub
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                return match.group(0)  # 如果没有找到替换函数，原样返回匹配对象（匹配的文本）
            return result

        return substitution  # 返回一个函数substitution，可在re.sub语句中使用这个函数


class HTMLRenderer(Handler):  # 处理程序：生成带标记的文本并从解析器接受详细指令
    """
    用于渲染HTML；
    HTMLRenderer的方法实现了HTML文档的基本标记，可通过超类Handler的方法start、end、sub来访问；
    """

    def start_document(self):
        print('<html><head><title>This is a test!</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):  # 添加开始标签
        print('<p>')

    def end_paragraph(self):  # 添加结束标签
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):  # 处理要突出的内容
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):  # 向处理程序提供实际文本
        print(data)

# ### 处理程序
# 负责生成带标记的文本（每个处理程序都生成不同的标记），供解析器用来生成输出；
