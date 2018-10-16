# -*- coding: utf-8 -*-
from urllib import request

proxy_handler = request.ProxyHandler({'http': '10.144.1.10:8080'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler)
with opener.open('http://www.pythonchallenge.com/') as f:
    print('Status:', f.status, f.reason)

proxies = {'http': 'http://10.144.1.10:8080/'}
opener = request.FancyURLopener(proxies)  # 使用指定代理覆盖当前环境设置
with opener.open("http://www.pythonchallenge.com/") as f:
    print('Status:', f.status, f.reason)

with request.urlopen('https://www.bing.com') as f:
    data = f.read().decode('utf-8')  # urlopen返回的对象支持close、read、readline、readlines和迭代等
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

# ### 标准库urllib模块
# - URL handling modules
# - https://docs.python.org/3/library/urllib.html
