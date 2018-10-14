# coding=utf-8
import sqlite3


def convert(value):
    """对各行进行分割并对各个字段进行转换"""
    if value.startswith('~'):
        return value.strip('~')  # 如果字段以波浪字符开头，就返回其内容
    if not value:
        value = '0'
    return float(value)


conn = sqlite3.connect('Chapter13SQLite.db')  # 如果db文件不存在将自动创建
curs = conn.cursor()  # 从连接获得游标

curs.execute('''
CREATE TABLE food (
    id         TEXT PRIMARY KEY,
    desc       TEXT,
    water      FLOAT,
    kcal       FLOAT,
    protein    FLOAT,
    fat        FLOAT,
    ash        FLOAT,
    carbs      FLOAT,
    fiber      FLOAT,
    sugar      FLOAT
)
''')  # 执行SQL语句：建表

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count = 10

for line in open('Chapter13_SourceData.txt'):
    fields = line.split('^')  # 数据行分解为字段
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)  # 执行SQL语句：插入数据

conn.commit()  # 如果修改数据，必须提交修改，才能保存到文件
conn.close()  # 关闭连接

# ### 脚本说明
# 将文本文件中的数据转换为SQL数据库；
#
# ### 数据源文件
# - 每行是一条数据记录，字段之间使用角标字符（^）分隔；
# - 数字字段直接包含数字，文本字段用两个波浪字符（~）将其字符串括起；
#
# ### SQLite
# SQLite（http://www.sqlite.org/）是开源轻型关系数据库，实现了自给自足的、无服务器的、零配置的、事务性的SQL数据库引擎；
#   - 整个SQLite数据库(定义、表、索引和数据本身)都存储在一个单一的跨平台的磁盘文件中；
#   - SQLite支持常见的标准SQL语句以及几种常见的数据类型；
#   - 占用资源非常的低，处理速度快，经常作为嵌入式数据库被集成到各种应用程序中；
#   - 使用“?”作为占位符，如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数；
# Python内置了SQLite3，可以直接使用；
#
# ### 一些基本概念
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表；
# 通过数据库连接（Connection）登录到数据库后，需要打开游标（Cursor），通过游标执行SQL语句，然后获得执行结果；
# 确保打开的Connection对象和Cursor对象都正确地被关闭，否则资源会泄露；
#
# ### 标准数据库API（Python Database API）
# 在PEP249（Python Database API Specification v2.0）中定义：https://www.python.org/dev/peps/pep-0249/
# 任何数据库想要和Python进行互操作，只需要提供符合Python Database API标准的数据库驱动即可；
# 由于SQLite的驱动内置在Python标准库中，所以可以直接操作SQLite数据库；
# 特别注意：Python Database API并不完全适用于所有数据库；
# 全局变量（Globals）
#   - 所有与DB API 2.0兼容的数据库都必须包含三个全局变量（描述模块的特征）
#   - 详细信息：https://www.python.org/dev/peps/pep-0249/#globals
#   - APIjibie（apilevel）：字符常量，表示使用的API版本；
#   - 线程安全程度（threadsafety）：整数，表示使用线程时线程的共享程度（共享模块、共享连接、共享游标、绝对安全）；
#   - 参数风格（paramstyle）：执行多个类似数据库查询时，如何在SQL查询中插入参数；
# 异常（Exceptions）
#   - DB API定义了多种异常，可以细致地处理错误，使用except语句就可捕获多种异常；
#   - 详细信息：https://www.python.org/dev/peps/pep-0249/#exceptions
# 连接对象（Connection Objects）
#   - 使用函数connect连接底层的数据库，根据具体数据库来接受参数；
#   - 函数connect返回一个连接对象，具有close、commit、rollback、cursor方法；
#   - 详细信息：https://www.python.org/dev/peps/pep-0249/#connection-objects
# 游标对象（Cursor Objects）
#   - 使用游标来执行SQL语句和查看结果，游标对象具备多个属性和方法；
#   - 详细信息：https://www.python.org/dev/peps/pep-0249/#cursor-objects
# 类型（Type Objects and Constructors）
#   - 定义了一些构造函数和常量（单例），用于提供特殊的类型和值，以便能够与底层SQL数据库正确地互操作；
#   - 详细信息：https://www.python.org/dev/peps/pep-0249/#type-objects-and-constructors
