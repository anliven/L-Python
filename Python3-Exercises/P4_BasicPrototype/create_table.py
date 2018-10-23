# coding=utf-8
import sqlite3

conn = sqlite3.connect('TempTest.db')  # 如果db文件不存在将自动创建
curs = conn.cursor()  # 从连接获得游标

curs.execute('''
CREATE TABLE messages (
    id          integer primary key autoincrement,
    subject     text not null,
    sender      text not null,
    reply_to    int,
    text        text not null
)
''')  # 执行SQL语句：建表

curs.execute("""insert into messages (subject, sender, text) values ('111', '111', 'Test111' )""")
curs.execute("""insert into messages (subject, sender, text) values ('222', '222', 'Test222' )""")
curs.execute("""
insert into messages (subject, sender, reply_to, text) values ('333', '333', 1, 'Test333' )
""")
curs.execute("""
insert into messages (subject, sender, reply_to, text) values ('444', '444', 3, 'Test444' )
""")

conn.commit()  # 如果修改数据，必须提交修改，才能保存到文件
conn.close()  # 关闭连接
