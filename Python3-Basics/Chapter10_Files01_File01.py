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
print("file name:%s, encode:%s, access mode:%s" % (f.name, f.encoding, f.mode))  # 文件对象的属性
f.write(testText)  # 写入文本，返回值是写入的字符数
print("This is a test!", file=f)  # 利用print函数的file参数，写入数据到文件
if testFile in locals():  # 判断testFile是否存在；locals()返回当前作用域中定义的所有名的集合
    f.close()  # 必须在使用完后关闭打开的文件

try:
    f = open(testFile)
    while True:
        line = f.readline()  # 利用循环和readline方法读取每一行
        if len(line) == 0:  # 当一个空字符串返回时，表示已经到达了文件末尾
            break
        print("## ", line, end='')
except FileNotFoundError:  # 如果文件不存在，进引发FileNotFoundError异常
    print("No such file:", testFile)
finally:
    f.close()

f2 = open(testFile, 'a', encoding="utf-8")  # 追加方式
f2.write("新写入的内容!")
f2.close()

f3 = open(testFile, 'r+', encoding="utf-8")
f3.seek(0, 2)  # 指针指到尾部
f3.write("新插入的内容!")
print("# Current index: ", f3.tell())
f3.close()

text = io.open(testFile, encoding="utf-8", errors='ignore').read()  # io模块的open方法
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
# - 指定文件的打开方式，默认模式是“rt”，也就是以文本（text）文件类型和阅读（read）模式打开；
# - 常用的打开模式
#   - r：只读模式（默认模式），如果文件不存在则抛出异常并给出错误码和详细信息；
#   - r+：读写模式；
#   - w：写入模式 / w+：若文件已存在则覆盖（从文件开头开始写入），若不存在则创建；
#   - a：追加模式 / a+：若文件已存在则追加（从文件末尾继续写入），若不存在则创建；
#   - x: 独占写入模式，如果文件已存在则引发FileExistsError异常；
#   - +: 读写模式（可读取也可写入，可与其他任何模式结合使用）；
#   - U：支持所有的换行符号，“\r”、“\n”、“\r\n”;
# - 指定文本类型：'t'文本模式（默认值，与其他模式结合使用）、'b'二进制模式（与其他模式结合使用）；
# - 对于非文本的二进制数据（声音、图像等）可使用二进制模式“rb”来禁用与文本相关的功能；
# - 指定字符串读取与写入的格式，例如“encoding="utf-8"”和“encoding='gbk'”；
# - errors参数表示如果遇到编码错误后如何处理，最简单的方式是直接忽略“errors='ignore'”；
# - 运行help(open)获得更多信息；
#
# ### 文件对象的属性
# - file.encoding: 文件所使用的编码
# - file.mode: Access文件打开时使用的访问模式
# - file.name: 文件名
#
# ### 常用文件操作
# 文件读写是通过open()函数打开的文件对象完成的：open函数打开文件，返回一个file对象，然后对其进行相关操作；
# - file.read()：读文件，所有内容为字符串，一次读取文件的全部内容；
# - file.read(x)：每次读取x个字符并改变指针，返回值是读取的x个字符内容；
# - f.readline()：读取一行（从当前位置到下一个分行符的文本）；
# - f.readline(x)：读取一行（从当前位置到下一个分行符的文本），指定最多读取x个字符；
# - f.readlines()：读取文件中所有行并以列表方式返回；
# - file.tell()：返回当前读写位置；
# - file.write()：写文件，返回值是写入的字符数，可以反复调用write()来写入文件，适合少量写入；
# - file.writelines()：接收一个字符串列表并将内容写入文件，效率比write()高，速度快，但需要自行添加换行符；
# - file.close()：关闭文件，文件使用完毕后必须关闭，确保修改成功保存和释放系统资源；
# - file.next()：返回当前行，并将文件指针到下一行；
# - file.flush()：在不关闭文件的情况下，可以提交更新（刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件）；
# file.seek(offset[, whence])：设置文件当前位置；
# - f.seek(5)：改变用户态读写指针偏移位置,可做随机写
# - f.seek(p,0)：移动当文件第p个字节处，绝对位置
# - f.seek(p,1)：移动到相对于当前位置之后的p个字节
# - f.seek(p,2)：移动到相对文件尾之后的p个字节
# - f.seek(0,2)：指针指到尾部
# 一些迭代文件内容的示例：
# - read(1)：每次一个字符（或字节）
# - read()：迭代所有字符
# - readline()： 每次一行
# - readlines()： 迭代所有行
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
