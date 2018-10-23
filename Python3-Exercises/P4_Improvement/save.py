# coding=utf-8
import sqlite3
import cgi
import sys
import cgitb

cgitb.enable()

conn = sqlite3.connect('TempTest.db')  # 创建连接
curs = conn.cursor()  # 获取游标

form = cgi.FieldStorage()
sender = form.getvalue('sender')
subject = form.getvalue('subject')
text = form.getvalue('text')
reply_to = form.getvalue('reply_to')

if not (sender and subject and text):
    print('Please supply sender, subject, and text')
    sys.exit()

if reply_to is not None:
    query = 'insert into messages (subject, sender, reply_to, text) ' \
            'values (\'{}\', \'{}\', {}, \'{}\')'.format(subject, sender, int(reply_to), text)
else:
    query = 'insert into messages (subject, sender, text) ' \
            'values (\'{}\', \'{}\', \'{}\')'.format(subject, sender, text)

curs.execute(query)
conn.commit()  # 提交修改
print('Content-type: text/html')
print("""
<html>
  <head>
    <title>Message Saved</title>
  </head>
  <body>
    <h1>Message Saved</h1>
    <hr>
    <a href='main.py'>Back to the main page</a>
  </body>
</html>""")
