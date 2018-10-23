# coding=utf-8
import cgitb
import sqlite3

cgitb.enable()

conn = sqlite3.connect('TempTest.db')  # 创建连接
curs = conn.cursor()  # 获取游标

print('Content-type: text/html')
print("""
<html>
  <head>
    <title>The FooBar Bulletin Board</title>
  </head>
  <body>
    <h1>The FooBar Bulletin Board</h1>""")

curs.execute('SELECT * FROM messages')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

top_level = []
children = {}

for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:
        top_level.append(row)
    else:
        children.setdefault(parent_id, []).append(row)


def format_data(row):
    print(' '*4, '<p><a href="view.py?id={}">{}</a></p>'.format(row['id'], row['subject']))  # 通过问号和“key=val”传递参数
    try:
        kids = children[row['id']]
    except KeyError:
        pass
    else:
        print('<blockquote>')
        for kid in kids:
            format_data(kid)
        print('</blockquote>')


print(' '*4, '<p>')
for row in top_level:
    format_data(row)
print("""     </p>
     <hr>
     <p><a href="edit.py">Post message</a></p>
  </body>
</html>
""")

# ### 脚本说明
# - main.py：公告板主页，展示当前所有主题信息，包含发布新消息的链接；
# - view.py：消息查看，根据传递过来的参数从数据库获取信息并显示，包含返回主页面的链接；
# - edit.py：消息编辑，用于编辑新消息和回复；
# - save.py：消息保存，从编辑页面获取信息并存储到数据库中；
#
# ### 执行脚本
#   1-通过create_db_table.py生成sqlite3数据库文件TempTest.db；
#   2-启动支持cgi的Web服务器：在命令行下执行“py -3 -m http.server --cgi”；
#   3-将数据文件和CGI脚本放在CGI服务器所在目录的子目录cgi-bin，并设置权限；
#   4-在浏览器打开“http://127.0.0.1:8000/cgi-bin/main.py”；
