#! python3
# -*- coding: utf-8 -*-
import io
import os

testText = '''\
Action is the antidote to despair!
There are two best times to plant a tree: one is ten years ago, and the other is now!
'''
testList = ['AAA', 'BBB', 'CCC']
testFile = 'test.txt'

f = open(testFile, 'w', encoding="utf-8")  # 以写入方式打开文件，不存在就创建
f.write(testText)  # 写入文本
f.close()  # 关闭打开的文件

with open(testFile) as f:  # 引入with语句自动调用close()方法
    for line in f.readlines():
        print("# ", line.strip())  # 删掉末尾的'\n'

f = open(testFile)
while True:
    line = f.readline()  # 读取每一行
    if len(line) == 0:  # 当一个空字符串返回时，表示已经到达了文件末尾
        break
    print("## ", line, end='')
f.close()

text = io.open(testFile, encoding="utf-8", errors='ignore').read()
print(text)

os.remove(testFile)

# ### 处理文件
# - 通过内置open函数打开文件，返回一个文件对象；
# - 通过文件对象的read、readline、write、close等方法完成文件读取、写入、关闭等操作；
# - 例如，readline方法读取文件的每一行；
#
# ### 内置open函数
# 内置函数open()可实现读文件功能，并返回一个file对象，随后便可对其进行相关操作。
# 语法格式为：open(filename, mode)。filename是文件名称，mode是打开文件的模式。
# - 指定文件的打开方式，默认以文本（text）文件类型和阅读（read）模式打开；
# - 常用的打开模式
#   - r：只读方式，默认模式；如果文件不存在，抛出异常并给出错误码和详细的信息；
#   - r+：读写方式，若已存在该文件则从文件头开始覆盖
#   - w：写入方式 / w+：读写方式，若已存在该文件则覆盖，若不存在则创建
#   - a：追加方式 / a+：读写方式，若已存在该文件则追加，若不存在则创建
# - 指定文本类型：文本模式（'t'）、二进制模式（'b'）；
# - 指定字符串读取与写入的格式，例如“encoding="utf-8"”和“encoding='gbk'”；
# - errors参数表示如果遇到编码错误后如何处理，最简单的方式是直接忽略“errors='ignore'”；
# - help(open)获得更多信息；
#
# ### 文件操作
# 文件读写是通过open()函数打开的文件对象完成的：open函数打开文件，返回一个file对象，然后对其进行相关操作；
# - file.read()：读文件，一次读取文件的全部内容；
# - file.write()：写文件，可以反复调用write()来写入文件；
# - file.close()：关闭文件，文件使用完毕后必须关闭，释放系统资源；
# - 引入with语句可以自动调用close()方法，来保证把没有写入的数据全部写入磁盘；
#
# ### 避免读取过多内容的方法
# - read()一次性读取文件的全部内容，适合文件较小的情况；
# - 反复调用read(size)方法，每次最多读取size个字节的内容，适合无法确定文件大小的情况；
# - 调用readline()每次读取一行内容；
# - 调用readlines()按行读取所有内容并返回list，适合读取配置文件；
#
# ### Unicode与UTF-8
# - Unicode是编码字符集（万国码），规定了字符的唯一二进制代码，但没有规定二进制代码如何存储；
# - UTF-8是编码格式，是Unicode的一种存储实现方式，同样的还有UTF-16, UTF-32；
# - 不同系统平台的Unicode字符存储实现方式很可能是不同的，统一转换为UTF-8编码格式，易于发送和接收；
# - 简而言之，UTF-8是Unicode的一种存储实现方式，UTF-8其实仍是Unicode；
# - 在io.open函数中提供编码（Encoding）与解码（Decoding）参数来指定编码格式；
# - 可将“# encoding=utf-8” 放置python程序顶端来声明使用UTF-8编码方式；
