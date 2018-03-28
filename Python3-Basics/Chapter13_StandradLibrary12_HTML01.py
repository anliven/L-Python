#! python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
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
parser.feed(h+h2)
print("###################")
parser.feed(h3)

# ### html package
# - HyperText Markup Language support
# - 官方文档：https://docs.python.org/3/library/html.html
#
# ### 标准库html.parser模块
# - Simple HTML and XHTML parser
# - 官方文档：https://docs.python.org/3/library/html.parser.html
