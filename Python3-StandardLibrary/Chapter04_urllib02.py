# -*- coding: utf-8 -*-
import urllib.request

local_file = 'd:/test.txt'

open_local_file = urllib.request.urlopen('file:/' + local_file)  # 直接读取本地文件
print(open_local_file.read())

req_local_file = urllib.request.Request(local_file)
text = urllib.request.FileHandler().file_open(req_local_file).read()  # 通过urllib.request.FileHandler类读取本地文件
print(text)

local_filename, headers = urllib.request.urlretrieve('https://www.bing.com', filename='d:/test_page.html')
print(local_filename, "\n", headers)  # 保存的文件可以通过函数open打开

# ### 访问本地文件
# 可使用已“file:”开头的URL直接访问本地文件；
# 也可以使用urllib.request.FileHandler类读取本地文件；
#
# ### 获取远程文件
# 通过urllib.request.urlretrieve()可以下载远程文件并保存在本地；
# 返回格式为的元组，filename是本地文件名称，headers包含远程文件的信息；
