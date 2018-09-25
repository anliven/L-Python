# -*- coding: utf-8 -*-
from urllib import request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.event_info = []
        self.temp_dict = {}
        self.flag = 0

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.flag = 1
        if 'time' == tag:
            self.flag = 2
        if ('class', 'event-location') in attrs:
            self.flag = 3

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, content):
        if self.flag == 1:
            self.temp_dict['name'] = content
            self.flag = 0

        if self.flag == 2:
            self.temp_dict['date'] = content
            self.flag = 0

        if self.flag == 3:
            self.temp_dict['address'] = content
            self.flag = 0
            self.event_info.append(self.temp_dict)
            self.temp_dict = {}

    def handle_comment(self, content):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

    def print_info(self):
        for n in self.event_info:
            print('-----------------------------------------------------')
            print('Events: %s' % n['name'])
            print('Date: %s' % n['date'])
            print('Address: %s' % n['address'])


if __name__ == '__main__':
    proxy_handler = request.ProxyHandler({'https': '10.144.1.10:8080'})  # 使用https的代理
    opener = request.build_opener(proxy_handler)
    with opener.open('https://www.python.org/events/python-events/') as f:
        data = f.read()
        parser = MyHTMLParser()
        parser.feed(data.decode('utf-8'))
        parser.print_info()

# ### 示例
# 解析HTML(https://www.python.org/events/python-events/)，获得Python官网发布的会议时间、名称和地点；
