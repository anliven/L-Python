# coding=utf-8
from xml.sax.handler import ContentHandler
from xml.sax import parse


class PageMaker(ContentHandler):
    """创建HTML页面"""
    pass_through = False  # 布尔变量指示是否在page元素内，拼在进入和离开page元素时修改

    def startElement(self, name, attrs):
        """
        在每个page元素的开头，打开一个给定名称的新文件，并在其中吸入合适的HTML首部（包括自动的标题）；
        在page元素内部，遍历所有的标签和字符而不修改（原样写入文件）；
        """
        if name == 'page':
            self.pass_through = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head><body>\n')
        elif self.pass_through:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')

    def endElement(self, name):
        """
        在每个page元素的末尾，将合适的HTML尾部写入文件，再将文件关闭；
        在page元素外部，忽略所有的标签；
        """
        if name == 'page':
            self.pass_through = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.pass_through:
            self.out.write('</{}>'.format(name))

    def characters(self, chars):
        """
        普通文本（字符）；
        """
        if self.pass_through:
            self.out.write(chars)


parse('website.xml', PageMaker())

# ### 程序说明
# - 使用单个XML文件描述各个网页和目录的信息；
# - 根据此XML文件创建网页和目录，进而生成完整的网站；
