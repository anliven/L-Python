# -*- coding: utf-8 -*-
import cgitb

cgitb.enable()  # 调用函数enable可显示包含错误或异常信息的网页，程序开发完成后，应关闭cgitb功能

print('Content-type: text/html\n')
print(1 / 0)  # 此行将报错
print('Hello, world!')

# ### 脚本说明
# 使用cgitb进行调试；
# 执行脚本：
#   1-启动支持cgi的Web服务器：在命令行下执行“py -3 -m http.server --cgi”；
#   2-将本CGI脚本放在服务器所在目录的子目录cgi-bin，并设置权限；
#   3-在浏览器打开“http://127.0.0.1:8000/cgi-bin/Chapter18_Web02_cgitb.py”；
#   4-打开的页面将显示有关“ZeroDivisionError”的信息；
#
# ### 标准库cgitb模块
# Traceback manager for CGI scripts
# https://docs.python.org/3/library/cgitb.html
# 用于CGI栈跟踪，可以帮助调试CGI脚本；
# 特别注意：程序开发完成后，应关闭cgitb功能；
