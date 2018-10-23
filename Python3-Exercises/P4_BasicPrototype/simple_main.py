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
    <h1>The FooBar Bulletin Board</h1>
""")

curs.execute('SELECT * FROM messages')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]
top_level = []  # 顶级消息
children = {}  # 子消息

for row in rows:
    # print("ID:", row['id'],  # 标识消息，数据库管理器自动为每条消息提供独一无二的ID
    #       "Subject:", row['subject'],  # 包含消息主题的字符串
    #       "Sender:", row['sender'], # 包含发送者姓名、邮件或其他信息的字符串
    #       "Reply_To:", row['reply_to'],  # 标识消息用来回复哪条消息（ID），如果不是回复消息则为空
    #       "Text:", row['text'],   # 包含消息正文的字符串
    #       "<br>")  # 页面显示换行
    parent_id = row['reply_to']  # 获取消息的reply_to字段
    if parent_id is None:  # 如果这个字段为None（表明不是回复消息），则加入顶级消息列表中
        top_level.append(row)
    else:  # 否则就将其加入到子消息列表children[parent_id]末尾
        children.setdefault(parent_id, []).append(row)


def format_data(row):  # 对于每条顶级消息，调用此函数打印消息的主题
    print(" " * 8, "Subject:", row['subject'])
    try:
        kids = children[row['id']]
    except KeyError:
        pass
    else:  # 如果有子消息就打印
        print(" " * 6, '<blockquote>')  # 打印开始标签
        for kid in kids:  # 对每条子消息递归地调用
            format_data(kid)
        print(" " * 6, '</blockquote>')  # 打印结束标签


print('    <p>')
for r in top_level:
    format_data(r)
print("""    </p>
  </body>
</html>
""")

# ### 脚本说明
#
#
# ### 执行脚本
#
#
