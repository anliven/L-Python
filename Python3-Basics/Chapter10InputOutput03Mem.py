#! python3
# -*- coding: utf-8 -*-
import io

f = io.StringIO()
f.write('Hello')
f.write(' ')
f.write('Python3!')
print(f.getvalue())  # getvalue()方法用于获得写入后的str

f2 = io.StringIO('Hi!\nPython3!')
print(f2.getvalue())
while True:
    s = f2.readline()  # 用一个str初始化StringIO，然后像读文件一样读取
    if s == '':
        break
    print(s.strip())

f3 = io.BytesIO()
f3.write('中文'.encode('utf-8'))  # 写入的是经过UTF-8编码的bytes
print(f3.getvalue())

f4 = io.BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')  # 用一个bytes初始化BytesIO，然后像读文件一样读取
print(f4.read().decode('utf-8'))

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口;
# - io.StringIO(在内存中读写str)
# - io.BytesIO(在内存中读写二进制数据)
