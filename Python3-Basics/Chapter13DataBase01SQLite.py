#! python3
# -*- coding: utf-8 -*-
import sqlite3  # 导入SQLite驱动


# ### SQLite
# http://www.sqlite.org/
# SQLite是开源的轻型关系数据库，实现了自给自足的、无服务器的、零配置的、事务性的SQL数据库引擎；
# 占用资源非常的低，处理速度快，经常作为嵌入式数据库被集成到各种应用程序中；
# Python内置了SQLite3，可以直接使用；
#
# ### 一些基本概念
# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表；
# 通过数据库连接（Connection）登录到数据库后，需要打开游标（Cursor），通过游标执行SQL语句，然后获得执行结果；
#
# ### API接口
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在Python标准库中，所以可以直接来操作SQLite数据库；
