#! python3
# -*- coding: utf-8 -*-
from pyquery import PyQuery
from urllib import request

# link = 'https://www.python.org/events/python-events/'
# doc = PyQuery(url=link)
# events = doc('.shrubbery').text()
# print(events)

proxy_handler = request.ProxyHandler({'https': '10.144.1.10:8080'})  # 使用https的代理
opener = request.build_opener(proxy_handler)
with opener.open('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')
    doc = PyQuery(data)
    events2 = doc('.shrubbery').text()
print(events2)

# ### pyquery
# A jquery-like library for python
# PYPI: https://pypi.python.org/pypi/pyquery/
# Home Page: https://github.com/gawel/pyquery
# Documentation： http://pythonhosted.org/pyquery/
#
# ### 示例
# 解析HTML(https://www.python.org/events/python-events/)，获得Python官网发布的会议时间、名称和地点；
