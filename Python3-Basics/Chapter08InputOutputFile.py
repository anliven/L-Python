# encoding=utf-8
import io
import os
import pickle

testText = '''\
Action is the antidote to despair!
There are two best times to plant a tree: one is ten years ago, and the other is now!
'''
testList = ['AAA', 'BBB', 'CCC']
testFile = 'test.txt'
testDataFile = 'test.data'

f = open(testFile, 'w', encoding="utf-8")
f.write(testText)
f.close()

f = open(testFile)
while True:
    line = f.readline()
    if len(line) == 0:  # 当一个空字符串返回时，表示已经到达了文件末尾
        break
    print(line, end='')
f.close()

text = io.open(testFile, encoding="utf-8").read()
print(text)

f = open(testDataFile, 'wb')
pickle.dump(testList, f)
f.close()

f = open(testDataFile, 'rb')
print(pickle.load(f))
f.close()

os.remove(testFile)
os.remove(testDataFile)

# ### 处理文件
# - 通过内置open函数打开文件，返回一个文件对象；
# - 通过文件对象的read、readline、write、close等方法完成文件读取、写入、关闭等操作；
# - 例如，readline方法读取文件的每一行；
#
# ### 内置open函数
# - 指定文件的打开方式，默认以文本（text）文件类型和阅读（read）模式打开；
# - 阅读模式（'r'）、写入模式（'w'）、追加模式（'a'）；
# - 指定文本类型：文本模式（'t'）、二进制模式（'b'）；
# - 指定字符串读取与写入的格式，例如“encoding="utf-8"”；
# - help(open)获得更多信息；
#
# ### Pickle模块
# - 通过Pickle模块可以持久地（Persistently）存储任何纯Python对象到文件并读取；
# - 封装（Pickling）：通过open以写入二进制（'wb'）模式打开文件，然后调用pickle.dump函数将对象存储到文件
# - 拆封（Unpickling）：通过pickle.load函数接收返回的对象；
# - 导入pickle模块后，可通过help(pickle)了解更多信息；
#
# ### Unicode与UTF-8
# - Unicode是编码字符集（万国码），规定了字符的唯一二进制代码，但没有规定二进制代码如何存储；
# - UTF-8是编码格式，是Unicode的一种存储实现方式，同样的还有UTF-16, UTF-32；
# - 不同系统平台的Unicode字符存储实现方式很可能是不同的，统一转换为UTF-8编码格式，易于发送和接收；
# - 简而言之，UTF-8是Unicode的一种存储实现方式，UTF-8其实仍是Unicode；
# - 在io.open函数中提供编码（Encoding）与解码（Decoding）参数来指定编码格式；
# - 可将“# encoding=utf-8” 放置python程序顶端来声明使用UTF-8编码方式；
