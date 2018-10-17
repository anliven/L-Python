# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/jobs').read()
soup = BeautifulSoup(text, 'html.parser')  #

jobs = set()  # set函数消除重复项
for job in soup.body.section('h2'):  # 使用soup.body获取文档体，再访问其中所有h2元素
    jobs.add('{} (http://python.org{})'.format(job.a.string, job.a['href']))  # 属性string是文本内容，a['href']为属性href

print('\n'.join(sorted(jobs, key=str.lower)))  # sorted函数按字母排序

# ### 脚本说明
# 使用Beautiful Soup来进行屏幕抓取；
#
# ### Beautiful Soup
# Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping.
# Home-page: http://www.crummy.com/software/BeautifulSoup
# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# 可用于解析格式不严谨的HTML；
