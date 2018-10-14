# -*- coding: utf-8 -*-
import pymysql  # 引入pymysql模块

conn = pymysql.connect("192.168.16.200", "root", "anliven", "pythondb")  # connect()打开数据库连接
cursor = conn.cursor()  # cursor()获取操作游标

try:
    create_sql = "create table student(id varchar(8),name varchar(10),age tinyint,sex varchar(2))"  # 预定义sql语句
    cursor.execute(create_sql)  # 执行sql语句

    cursor.execute('insert into student values (%s, %s, %s, %s)', ['001', 'Liven', 35, 'M'])  # 直接执行sql语句
    cursor.execute('insert into student values (%s, %s, %s, %s)', ['002', 'An', 32, 'W'])  # %s为占位符

    insert_sql = """insert into student values ('003','Duo',2,'W')"""  # 三引号之间的内容可避免繁杂的转义;
    cursor.execute(insert_sql)

    conn.commit()  # 提交到数据库执行(只有对数据库进行了增删改时需要提交数据库，查询不需要)
except pymysql.err.OperationalError:
    print("Operational Error!!!")
    conn.rollback()  # 回滚
except pymysql.err.InternalError:
    print("Table already exists!!!")

cursor.execute("select * from student")
print(cursor.fetchall())  # 获取从当前游标位置开始的所有数据
cursor.scroll(0, mode='absolute')  # 绝对位置移动，游标位置移动到首行
print(cursor.fetchone())  # 获取从当前游标位置开始的第一行数据
cursor.scroll(-1, mode='relative')  # 相对位置移动，当前游标位置向前移动1行
print(cursor.fetchmany(2))  # 获取从当前游标位置开始的前2行数据

cursor.close()  # 关闭游标
conn.close()  # 关闭数据库连接

# ### 利用模块PyMySQL访问MySQL
# PyMySQL模块是对mysql连接做了一层封装，本质上也是使用的MySQL驱动包；
# - 创建连接：connect(host='', port=3306, uer='', passwd='', db='', charset='utf8')；“”charset='utf8'防止中文显示乱码；
# - 创建游标：cursor()；
# - 执行sql语句：execute(sql)；
# - 提交（保存新建或者修改的数据）：commit()；
# - 移动游标：scroll()；
#
# ### 连接数据库前的准备
# 1 - 目的主机上的数据库服务已开启并正常运行；
# 2 - 数据库已创建好并开放了对应的访问权限；
# 3 - pymysql模块已正确安装完成（“pip3 install PyMySQL”）；
