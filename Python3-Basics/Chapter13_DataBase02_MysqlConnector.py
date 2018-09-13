# -*- coding: utf-8 -*-
import mysql.connector  # 导入MySQL驱动

conn = mysql.connector.connect(host="192.168.16.200", user='root', password='anliven',
                               database='pythondb')  # 建立数据库连接
cursor = conn.cursor()  # 获取游标
select_sql = """select * from student"""  # 预制sql语句

try:
    cursor.execute(select_sql)  # 执行sql语句
except mysql.connector.OperationalError:
    print("Operational Error!!!")

data_1 = cursor.fetchone()  # 获取从当前游标位置开始的第一行数据
print(data_1)
data_2 = cursor.fetchall()  # 获取从当前游标位置开始的所有数据
print(data_2)

cursor.close()  # 关闭游标
conn.close()  # 关闭数据库连接

# ### 利用支持Python的MySQL驱动包访问MySQL
# MySQL官方提供了mysql-connector-python驱动(https://dev.mysql.com/doc/connector-python/en/)；
# 安装：“pip3 install mysql-connector-python --allow-external mysql-connector-python”
#
# ### 操作MySQL数据库
# 由于Python的DB-API定义都是通用的，所以操作MySQL的数据库代码和SQLite类似；
# MySQL的SQL占位符是%s；
