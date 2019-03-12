# -*- coding: utf-8 -*-

print('Content-type: text/plain')  # 设置首部，这里表示本网页为纯文本，如果表示为HTML则为“text/html”
print()  # Prints an empty line, to end the headers
print('Hello, world!')

# ### 脚本说明
# 实现简单的CGI脚本；
# 执行脚本：
#   1-启动支持cgi的Web服务器：在命令行下执行“py -3 -m http.server --cgi”；
#   2-将本CGI脚本放在服务器所在目录的子目录cgi-bin，并设置权限；
#   3-在浏览器打开“http://127.0.0.1:8000/cgi-bin/Chapter18_Web01_cgi.py”；
#   4-打开的页面只显示“Hello, world!”；
#
# ### CGI（Common Gateway Interface，通用网关接口）
# CGI是一种标准机制，Web服务器通过CGI将查询交给专用测序，并以网页方式显示查询结果；
# 可以简单理解CGI是创建Web应用的简单方式：是一段运行在服务器上的程序（例如HTTP服务器），提供网页接口给客户端；
#
# ### Python的Web编程指南
# https://wiki.python.org/moin/WebProgramming
#
# ### 尝试使用CGI
# 可以通过模块http.server直接运行一个临时Web服务器；
# 特别注意：启动的服务器将提供运行时所在目录中的文件；
# 示例：
#   - 在命令行下执行“py -3 -m http.server --cgi”（指定了“--cgi”参数，启动的服务器将支持CGI）；
#   - 在浏览器中打开“http://127.0.0.1:8000/”或“http://localhost:8000/”，将看到服务器所在目录的文件；
#
# ### CGI脚本
# 存放：
#   - CGI程序必须放在可通过web访问的目录中，而且必须标识为CGI脚本，避免Web服务器以网页方式提供其源代码；
#   - CGI脚本放在子目录cgi-bin中，在Python中可以使用“.py”作为扩展名；
# 格式及权限：
#   - 在unix中需要在首行添加#!部分，告知Web服务器如何执行脚本，例如“#!/usr/bin/python3”；
#   - 脚本必须保存为unix风格的纯文本文件；
#   - 设置合适的权限，保证只有自己可以修改，其他人可以读取和执行，一般为755权限；
#   - 为防止安全风险，一般不允许CGI脚本对服务器的文件执行写入操作，禁止666权限，
#
# ### 模块http.server
# HTTP servers
# https://docs.python.org/3/library/http.server.html
#
# ### 模块cgi
# Common Gateway Interface support
# https://docs.python.org/3/library/cgi.html
