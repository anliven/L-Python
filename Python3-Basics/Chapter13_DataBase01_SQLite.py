#! python3
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

# ### SQLite
# http://www.sqlite.org/
# SQLite是开源的轻型关系数据库，实现了自给自足的、无服务器的、零配置的、事务性的SQL数据库引擎；
# 整个SQLite数据库(定义、表、索引和数据本身)都存储在一个单一的跨平台的磁盘文件中;
# SQLite支持常见的标准SQL语句以及几种常见的数据类型;
# 占用资源非常的低，处理速度快，经常作为嵌入式数据库被集成到各种应用程序中；
# 使用“?”作为占位符，如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数；
#
# ### Python内置了SQLite3，可以直接使用；
#
# ### 一些基本概念
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表；
# 通过数据库连接（Connection）登录到数据库后，需要打开游标（Cursor），通过游标执行SQL语句，然后获得执行结果；
# 确保打开的Connection对象和Cursor对象都正确地被关闭，否则资源会泄露；
#
# ### API接口
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在Python标准库中，所以可以直接来操作SQLite数据库；
