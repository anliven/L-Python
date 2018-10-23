# coding=utf-8
import cgitb;
import sqlite3
import cgi

cgitb.enable()
conn = sqlite3.connect('TempTest.db')  # 创建连接
curs = conn.cursor()  # 获取游标

form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')

print('Content-type: text/html')
print("""
<html>
  <head>
    <title>Compose Message</title>
  </head>
  <body>
    <h1>Compose Message</h1>
    <form action='save.py' method='POST'>""")

subject = ''
if reply_to is not None:
    print('<input type="hidden" name="reply_to" value="{}"/>'.format(reply_to))  # 隐藏的input元素
    curs.execute('SELECT subject FROM messages WHERE id = {}'.format(reply_to))
    subject = curs.fetchone()[0]
    if not subject.startswith('Re:'):  # 设置回复的默认开头
        subject = 'Re:' + subject

print("""       <b>Subject:</b><br>
         <input type='text' size='40' name='subject' value='{}'><br>
       <b>Sender:</b><br>
         <input type='text' size='40' name='sender'><br>
       <b>Message:</b><br>
       <textarea name='text' cols='40' rows='20'></textarea><br>
         <input type='submit' value='Save'>
     </form>
     <hr>
     <a href='main.py'>Back to the main page</a>
  </body>
</html>
""".format(subject))
