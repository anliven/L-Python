# -*- coding: utf-8 -*-
import cgi

form = cgi.FieldStorage()  # 创建FieldStorage实例（应只创建一个）
name = form.getvalue('name', 'world')  # CGI脚本通过getvalue方法获取值，这里默认值为world
print("""Content-type: text/html

<html>
  <head>
    <title>Greeting Page</title>
  </head>
  <body>
    <h1>Hello, {}!</h1>
    <form action='Chapter16_Web03_cgi.py'>
      Change Name：<input type='text' name='name'>
      <input type='submit' value='Submit'>
    </form>
  </body>
</html>
""".format(name))

# ### 脚本说明
# 实现包含HTML表单的简单CGI脚本；
# 执行脚本：
#   1-启动支持cgi的Web服务器：在命令行下执行“py -3 -m http.server --cgi”；
#   2-将本CGI脚本放在服务器所在目录的子目录cgi-bin，并设置权限；
#   3-在浏览器打开“http://127.0.0.1:8000/cgi-bin/Chapter16_Web03_cgi.py”；
#   4-填写文本并提交，将显示形如“Hello world”的内容；
#
# ### HTML表单的相关说明
# - HTML表单是一个包含表单元素的区域，允许用户在表单中输入内容，比如文本域、下拉列表、单选框、复选框、提交按钮等；
# - 使用表单标签<form>来设置，属性action设置为脚本的名称，意味着提交表单后将再次运行这个脚本；
# - 输入元素标签<input>：输入类型由类型属性（type）定义；
#
# ### Web框架
# 对于重要或复杂的Web应用，一般不会直接为其编写繁琐的CGI脚本，而是使用Web框架，自动完成很多繁重的环节；
# 更多信息：Python的Web编程指南（https://wiki.python.org/moin/WebProgramming）；
#
# ### Web框架Flask
# 简单又实用的Flask，适用于较复杂的服务端Web应用开发；
# A simple framework for building complex web applications.
# Home-page: https://www.palletsprojects.com/p/flask/
# Documentation：http://flask.pocoo.org/docs/
