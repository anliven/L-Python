#! python3
# -*- coding: utf-8 -*-
import webbrowser

url = "www.bing.com"
# webbrowser.open_new_tab(url)  # Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new(url)  # Open URL in new window, raising the window if possible.
webbrowser.open(url, new=2, autoraise=True)  # new=2 浏览器窗口新的tab会被打开

chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'  # 浏览器目录
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))  # webbrowser.register()方法注册浏览器类型
webbrowser.get('chrome').open('www.baidu.com', new=1, autoraise=True)  # # webbrowser.get()方法获取到系统浏览器的操作对象

# ### 标准库webbrowser模块
# Convenient Web-browser controller
# https://docs.python.org/3/library/webbrowser.html
#
# ### webbrowser.open(url, new=0, autoraise=True)
# Display url using the default browser
# - new=0: 同一浏览器窗口打开
# - new=1: 打开浏览器新的窗口
# - new=2: 打开浏览器窗口新的tab
# - autoraise=True:the window is raised if possible
#
# ### webbrowser.register(name, constructor, instance=None)
# 注册浏览器类型
#
# ### webbrowser.get(using=None)
# 获取打开的浏览器对象，如果参数为空，则打开默认的浏览器；
# 使用get()方法之前，必须注册浏览器对象；
