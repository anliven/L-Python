# coding=utf-8
from xml.sax.handler import ContentHandler
from xml.sax import parse
import os


class Dispatcher:
    """分派器类"""

    def dispatch(self, prefix, name, attrs=None):
        """查找对应的处理程序、创建参数元素并调用处理程序；"""
        manual_name = prefix + name.capitalize()  # 根据前缀和标签名生成处理程序的名称
        default_name = 'default' + prefix.capitalize()  # 根据前缀生成默认处理程序的名称
        method = getattr(self, manual_name, None)  # 尝试使用getattr获取处理程序，并将默认值设置为None
        if callable(method):
            args = ()  # 如果method是可调用的，就将args设置为空元组
        else:
            method = getattr(self, default_name, None)
            args = name,  # 设置为只包含标签名的元组
        if prefix == 'start':
            args += attrs,  # 如果调用的是起始处理程序，就将属性添加到参数元组中
        if callable(method):
            method(*args)  # 如果method是可调用的，就使用正常的参数调用它

    def startElement(self, name, attrs):
        """被调用时，查找并提供属性来调用事件处理程序start<name>"""
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        """被调用时，查找并提供属性来调用事件处理程序end<name>"""
        self.dispatch('end', name)


class WebsiteConstructor(Dispatcher, ContentHandler):
    """分派器混合类，用来处理管理性细节:收集字符数据、管理布尔状态变量、分派事件给自定义事件处理程序等；"""
    pass_through = False  # 布尔状态变量

    def __init__(self, directory):
        self.directory = [directory]  # 目录名列表用来存储当前目录路径
        self.ensureDirectory()

    def ensureDirectory(self):
        """确保当前目录已创建"""
        path = os.path.join(*self.directory)  # 合并多条路径，传递目录列表时使用星号运算符进行拆分
        os.makedirs(path, exist_ok=True)  # 创建必要的目录

    def characters(self, chars):
        """普通文本（字符）；"""
        if self.pass_through:
            self.out.write(chars)

    def defaultStart(self, name, attrs):
        """默认处理程序"""
        if self.pass_through:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')

    def defaultEnd(self, name):
        """默认处理程序"""
        if self.pass_through:
            self.out.write('</{}>'.format(name))

    def startDirectory(self, attrs):
        """事件处理：进入目录"""
        self.directory.append(attrs['name'])  # 将目录名称附加到目录列表末尾
        self.ensureDirectory()

    def endDirectory(self):
        """事件处理：离开目录"""
        self.directory.pop()  # 将目录名称从目录列表中弹出

    def startPage(self, attrs):
        """事件处理：处理页面"""
        filename = os.path.join(*self.directory + [attrs['name'] + '.html'])  # 合并路径和文件名
        self.out = open(filename, 'w')
        self.writeHeader(attrs['title'])
        self.pass_through = True

    def endPage(self):
        """事件处理：处理页面"""
        self.pass_through = False
        self.writeFooter()
        self.out.close()

    def writeHeader(self, title):
        """首部写入文件"""
        self.out.write('<html>\n  <head>\n    <title>')
        self.out.write(title)
        self.out.write('</title>\n  </head>\n  <body>\n')

    def writeFooter(self):
        """尾部写入文件"""
        self.out.write('\n  </body>\n</html>\n')


parse('website.xml', WebsiteConstructor('public_html'))

# ### 程序说明
# 网站生成器(webstie.py)：
#   - 使用单个XML文件描述各个网页和目录的信息；
#   - 根据此XML文件创建网页和目录，进而生成完整的网站；
# 生成的目录及文件
# public_html/:
# - index.html
# - interests:
#   - eating.html
#   - shouting.html
#   - sleeping.html
