# -*- coding: utf-8 -*-
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):  # 使用HTMLParser类来派生子类，并重写各种事件处理方法

    def handle_starttag(self, tag, attrs):  # 遇到开始标签时调用，attrs是一个由形如(name, value)的元组组成的序列
        print('<%s>' % tag)

    def handle_endtag(self, tag):  # 遇到结束标签时调用
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):  # 遇到空标签时调用，默认分别处理开始标签和结束标签
        print('<%s/>' % tag)

    def handle_data(self, data):  # 遇到文本数据时调用
        print(data)

    def handle_comment(self, data):  # 遇到注释时，只对注释内容调用
        print('<!--', data, '-->')

    def handle_entityref(self, name):  # 遇到形如“&name;”的实体引用时调用
        print('&%s;' % name)

    def handle_charref(self, name):  # 遇到形如“&#ref;”的字符引用时调用
        print('&#%s;' % name)


h = '<html><head><title>Test</title></head>'
h2 = '<body><h1>Parse me!</h1></body></html>'
h3 = r'''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''

parser = MyHTMLParser()
parser.feed(h + h2)  # 调用feed方法运行解析器
print("###################")
parser.feed(h3)

# ### html package
# - HyperText Markup Language support
# - https://docs.python.org/3/library/html.html
#
# ### 标准库html.parser模块
# Simple HTML and XHTML parser
# https://docs.python.org/3/library/html.parser.html
# 使用html.parser的HTMLParser类可以对格式良好的HTML和XHTML进行解析；
# 使用HTMLParser类需要派生子类，并重写各种事件处理方法；
#
# ### HTMLParser类的解析器回调方法（事件处理程序）：
#  - handle_starttag(tag, attrs): 遇到开始标签时调用，attrs是一个由形如(name, value)的元组组成；
#  - handle_endtag(tag): 遇到结束标签时调用；
#  - handle_startendtag(tag, attrs): 遇到空标签时调用，默认分别处理开始标签和结束；
#  - handle_data(data): 遇到文本数据时调用；
#  - handle_comment(data): 遇到注释时，只对注释内容调用；
#  - handle_entityref(name): 遇到形如“&name;”的实体引用时调用；
#  - handle_charref(name): 遇到形如“&#ref;”的字符引用时调用；
#  - handle_pi(data): 用于处理指令；
#  - handle_decl(decl): 遇到形如“<!...#>”声明时调用；
#  - unknown_decl(data): 遇到未知声明时调用；
#
# ### HTML和XHTML
# - XHTML比HTML更为严格，要求显示地结束所有的元素；
# - XHTML可以被XML的各种工具（例如：XPath）来处理；
