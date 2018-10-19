# -*- coding: utf-8 -*-
import cgi

form = cgi.FieldStorage()  # 创建FieldStorage实例（应只创建一个）
name = form.getvalue('name', 'world')  # CGI脚本通过getvalue方法获取值，这里默认值为world

print('Content-type: text/plain\n')
print('Hello, {}!'.format(name))

# ### 脚本说明
# 从FieldStorage中获取单个值；
# 执行脚本：
#   1-启动支持cgi的Web服务器：在命令行下执行“py -3 -m http.server --cgi”；
#   2-将本CGI脚本放在服务器所在目录的子目录cgi-bin，并设置权限；
#   3-在浏览器打开“http://127.0.0.1:8000/cgi-bin/Chapter16_Web02_cgi.py”；
#   4-打开的页面只显示“Hello, world!”；
#
# ### CGI脚本的输入
# 方式一：
#   1-通过HTML表单以键值对（字段）方式提供给CGI脚本；
#   2-在CGI脚本中使用模块cgi的FieldStorage类来获取这些字段；
# 方式二：
#   1-在调用CGI脚本时直接指定参数：例如“http://127.0.0.1:8000/cgi-bin/Chapter18_Web02_cgi.py?name=Anliven”；
#   2-页面将显示“Hello, Anliven!”，而不是“Hello, world!”；
#   3-可以指定多个参数：例如“http://127.0.0.1:8000/cgi-bin/Chapter18_Web02_cgi.py?name=Anliven&age=29”;
#   4-模块urllib.parse中的urlencode方法支持多个参数格式的创建；
