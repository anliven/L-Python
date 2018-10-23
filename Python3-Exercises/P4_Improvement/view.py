# coding=utf-8
import sqlite3
import cgi
import sys
import cgitb

cgitb.enable()

conn = sqlite3.connect('TempTest.db')  # 创建连接
curs = conn.cursor()  # 获取游标

form = cgi.FieldStorage()
message_id = int(form.getvalue('id'))

print('Content-type: text/html')
print("""
<html>
  <head>
    <title>View Message</title>
  </head>
  <body>
    <h1>View Message</h1>""")

curs.execute('SELECT * FROM messages WHERE id = {}'.format(message_id))
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

if not rows:
    print('Unknown message ID')
    sys.exit()

row = rows[0]

print("""
    <p>
    <b>Subject:</b>{subject}<br>
    <b>Sender:</b>{sender}<br>
    <b>Content:</b><pre>{text}</pre>
    </p>
    <hr>
    <a href='main.py'>Back to the main page.</a><br>
    <a href="edit.py?reply_to={id}">Reply</a>
  </body>
</html>""".format(subject=row['subject'],
                  sender=row['sender'],
                  text=row['text'],
                  id=row['id']))
