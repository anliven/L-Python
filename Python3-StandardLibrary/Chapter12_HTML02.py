# -*- coding: utf-8 -*-
from urllib.request import urlopen
from html.parser import HTMLParser


def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()


class Scraper(HTMLParser):
    in_link = False  # 使用布尔状态变量（属性）来跟踪是否位于相关的链接中

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)  # 参数attrs是形如(key,value)的元组组成的列表，这里使用dick函数转换为字典
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True  # 在事件处理程序中，检查并更新属性
            self.chunks = []

    def handle_data(self, data):  # 假定文本分成多个块，需要多次调用handle_data
        if self.in_link:  # 在事件处理程序中，检查并更新属性
            self.chunks.append(data)  # 属性chunks

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:  # 在事件处理程序中，检查并更新属性
            print('{} (http://python.org{})'.format(''.join(self.chunks), self.url))  # 合并所有的文本块并打印
            self.in_link = False  # 在事件处理程序中，检查并更新属性


text = urlopen('http://python.org/jobs').read().decode()
parser = Scraper()
parser.feed(text)  # 调用feed方法运行解析器
parser.close()

# ### 脚本说明
# 使用html.parser模块实现屏幕抓取（下载网页并从中提取和分析信息）；
#   - 无需实现所有的事件处理程序（解析器回调方法）；
#   - 也可能无需创建整个文档的抽象表示（例如文档树）就能找到所需的内容；
#   - 只需要跟踪找到目标内容所需的信息即可；
#
# ### 对比正则表达式
# 对于屏幕抓取而言，使用html.parser模块比使用正则表达式更健壮（应对输入数据变化的能力更强）；
# 但代码实现起来可能更繁琐，结构不清晰；
