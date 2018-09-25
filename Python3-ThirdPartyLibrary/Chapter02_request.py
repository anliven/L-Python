# -*- coding: utf-8 -*-
import requests

# r = requests.get('https://www.bing.com/')
r = requests.session()
r.proxies = {'http': '10.144.1.10:8080'}
s = r.get('https://www.bing.com/', timeout=2.5)
print("request:", s.status_code,
      "\nrequest:", s.headers,
      "\nrequest:", s.headers['content-type'],
      "\nrequest:", s.encoding,  # 检测编码
      "\nrequest:", s.content,  # 获得bytes对象
      "\nrequest:", s.cookies,
      # "\nrequest:", s.text  # 读取服务器响应的内容
      )

# ### requests
# - Python HTTP for Humans.
# - Home Page: python-requests.org
# - Documentation: http://docs.python-requests.org/zh_CN/latest/
