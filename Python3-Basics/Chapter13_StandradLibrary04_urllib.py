#! python3
# -*- coding: utf-8 -*-

from urllib import request

with request.urlopen('https://www.bing.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

proxy_handler = request.ProxyHandler({'http': '10.144.1.10:8080'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler)
with opener.open('http://www.pythonchallenge.com/') as f:
    print("Proxy is ok!")
    pass

# ### 标准库urllib模块
# - URL handling modules
# - 官方文档：https://docs.python.org/3/library/urllib.html
