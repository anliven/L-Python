#! python3
# -*- coding: utf-8 -*-
import os
import shutil

print("OS-type: ", os.name)
# print("OS-details: ", os.uname())
print("OS-ENV: ", os.environ)
print("OS-ENV-PATH: ", os.environ.get('PATH'))

print(os.getcwd())
print(os.path.abspath('.'))
testPath = os.path.join('.', 'testDir')
os.mkdir(testPath)
os.rmdir(testPath)

print(os.path.split('/testdir/file.txt'))
print(os.path.splitext('/testdir/file.txt'))

print([x for x in os.listdir('.') if os.path.isdir(x)])  # 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])  # 列出当前目录下的所有.py文件

testText = '''Action is the antidote to despair!'''
testFile = 'test.txt'

f = open(testFile, 'w', encoding="utf-8")
f.write(testText)
f.close()

print(os.path.exists(testFile))  # 判断是否存在
os.rename('test.txt', 'test.py')
shutil.copyfile('test.py', 'test2.py')
os.remove('test.py')
os.remove('test2.py')

# ### os模块
# - os.name : 操作系统类型；打印出posix说明系统是Linux、Unix或Mac OS X，如果是nt说明系统是Windows系统；
# - os.uname() ：获取详细的系统信息，Windows系统上不提供；os模块的某些函数是跟操作系统类型相关的；
# - os.environ : 获取操作系统中定义的环境变量；
# - os.environ.get('key') ： 获取某个环境变量的值；
#
# - os.mkdir() ： 创建目录
# - os.rmdir() ： 删除目录
# - os.chdir() ： 切换目录
#
# - os.getcwd() : 查看当前目录；
# - os.path.abspath() ： 查看目录的绝对路径；
# - os.path.isdir() ： 判断是否为目录；
# - os.path.exists() : 判断路径是否存在；
# - os.listdir() ： 列出目录；
# - os.path.join() ： 合成路径，能够正确处理不同操作系统的路径分隔符；
# - os.path.split() ： 拆分路径，可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名；
# - os.path.splitext() ： 得到文件扩展名；
# 注意：join()、split()、splitext()等函数只对字符串进行操作。并不要求目录和文件真实存在；
#
# ### shutil模块
# shutil模块可以看做是os模块的补充；
# - shutil.copyfile()：复制文件
