# coding=utf-8
import cgi

form = cgi.FieldStorage()
text = form.getvalue('text', open('d:/simple.txt').read())  # 获取数据文件的内容，此文件必须存在
f = open('d:/simple.txt', 'w')
f.write(text)
f.close()

print("""Content-type: text/html

<html>
  <head>
    <title>A Simple Editor</title>
  </head>
  <body>
    <form action='simple_edit.py' method='POST'>
      <textarea rows='10' cols='20' name='text'>{}</textarea><br>
      <input type='submit' value='Submit'>
    </form>
  </body>
</html>
""".format(text))

# ### 脚本说明
# 实现远程文档编辑功能的简单CGI脚本；
#   - 显示一个包含编辑和提交文本的网页；
#   - 如果提交新内容则保存到文件，如果没有提交则显示文件的当前内容；
# 执行脚本：
#   1-启动支持cgi的Web服务器：在命令行下执行“py -3 -m http.server --cgi”；
#   2-将本CGI脚本放在服务器所在目录的子目录cgi-bin，并设置权限；
#   3-在浏览器打开“http://127.0.0.1:8000/cgi-bin/Chapter16_Web04_cgi.py”；
#
# ### CGI中的POST与GET方法
# - GET方法：默认方法；
# - POST方法：通常提交大量数据时，应使用POST方法；
