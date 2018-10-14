# -*- coding: utf-8 -*-
import sqlite3  # 导入SQLite驱动
import os

db_file = os.path.join(os.path.dirname(__file__), 'Chapter13SQLite.db')
print(db_file)
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)  # 创建数据库连接，如果数据库文件不存在则在当前目录创建
cursor = conn.cursor()  # 创建游标

try:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')  # 执行sql语句
    print(cursor.rowcount)  # rowcount返回影响的行数
    cursor.execute('insert into user (id, name) values (\'1\', \'An\')')
    print(cursor.rowcount)
    cursor.execute("""insert into user (id, name) values ('2', 'Liven')""")
    print(cursor.rowcount)
    conn.commit()  # 提交事务（查询操作没有改动，不需要提交）

    cursor.execute('select * from user where id=?', ('1',))  # 1个占位符?对应1个参数
    values = cursor.fetchall()  # 获取结果集（返回一个list，每个元素都是一个tuple，对应一行记录）
    print(values)
except sqlite3.OperationalError:
    print("Something wrong!")
finally:
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接

# ### 参考信息
# Python支持的数据库清单：https://wiki.python.org/moin/DatabaseInterfaces
# Python数据库编程指南：https://wiki.python.org/moin/DatabaseProgramming
