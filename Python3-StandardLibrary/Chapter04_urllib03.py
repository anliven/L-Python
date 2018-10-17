# coding=utf-8
from urllib.request import urlopen
import re

p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()
print(p.findall(text)[0])
for url, name in p.findall(text):
    print('{} (http://python.org{})'.format(name, url))

# ### 脚本说明
# 实现屏幕抓取（通过程序下载网页并从中提取信息的过程）；
#   - 使用urllib来获取网页的HTML代码；
#   - 使用正则表达式或其他技术从中提取信息；
#
# ### 可能存在的缺点
# - 正则表达式难以理解，尤其在HTML代码复杂的场景；
# - 正则表达式可能无法处理某些HTML内容；
# - 难以应对变化（正则表达式依赖于HTML代码细节，如果相关网页结构发生变化，正则表达式很可能失效）；
# 解决方法：使用第三方库Beautiful Soup来进行屏幕抓取；
