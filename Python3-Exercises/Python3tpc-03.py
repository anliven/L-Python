#! python3
# -*- coding: utf-8 -*-

import re
from urllib import request

testFile = 'Python3tpc-03.txt'

# Solution - 1
with open(testFile) as f:
    data = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", f.read()))
    print(data)

# Solution - 2
html = request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
# proxy_handler = request.ProxyHandler({'http': 'http://10.144.1.10:8080/'})  # 设置代理
# opener = request.build_opener(proxy_handler)
# page = opener.open("http://www.pythonchallenge.com/pc/def/equality.html")
# html = page.read().decode('utf-8')
data2 = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data2)))

# 从如下网页源代码中找出符合要求的字符（前后有三个大写字符）来获得线索信息
# view-source:http://www.pythonchallenge.com/pc/def/equality.html
#
# Problem Link : http://www.pythonchallenge.com/pc/def/equality.html
# Solution Link : http://www.pythonchallenge.com/pcc/def/linkedlist.php
