# coding=utf-8
import sqlite3
import sys

conn = sqlite3.connect('Chapter13SQLite.db')  # 创建连接
curs = conn.cursor()  # 获取游标

query = 'SELECT * FROM food WHERE ' + sys.argv[1]
print(query)
curs.execute(query)  # 执行SQL查询
names = [f[0] for f in curs.description]
for row in curs.fetchall():  # 提取结果
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()

# ### 脚本说明
# 在SQL数据库执行数据查询；
# 执行方式：python listing13-2.py fat
