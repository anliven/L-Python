#! python3
# -*- coding: utf-8 -*-

a = 2  # 整型变量
b = 1.5  # 浮点型变量
c = True  # 布尔型变量
d = 3.14j  # 复数型变量
e = True + False  # True代表1，False代表0
print(a, b, c, d, e)

string_sample = "Hello Python!"
print(string_sample.replace('!', '!!!'))  # replace方法并返回一个新字符串
print(string_sample.find('P'))  # find方法判断指定子字符串是否存在，若存在，返回索引位置，若不存在，返回-1
print(string_sample.split('P', 1))  # split方法分解字符串，并返回一个字符串列表
print(string_sample)

print(string_sample[0:2])  # 从下标0到下标2，包括0不包括2
print(string_sample[0:-1])  # 从下标0到倒数第1个,不包括倒数第1个
print(string_sample[5:])  # 从下标5到最后
print(string_sample[:-7])  # 从开始到倒数第7个,,不包括倒数第7个
print(string_sample[0])  # 打印下标0的值
print(string_sample * 2)  # 连续输出两次
print(string_sample + "HelloWorld!")  # 连接字符串
print('Hello' in string_sample)  # in运算符用以检查给定的字符串是否是查询的字符串中的一部分
print('Java' in string_sample)
print('Java' not in string_sample)  # 判断'Java'是否不是str的子串

print('\nHello')  # 转义字符\n可以换行
print(r'\nHello')  # 字符串前加上r或R可以使字符串原样输出，防止被转义

print('中文', u'显示')  # Python3中字符串以Unicode编码，支持多语言
print(ord('A'), ord('中'))  # ord()函数获取字符的整数表示
print(chr(65), chr(20013))  # chr()函数把编码转换为对应的字符

print('ABC', len('ABC'), b'ABC', len(b'ABC'))  # bytes类型的数据用带b前缀的单引号或双引号表示
print(len('ABC'), len(b'ABC'))  # len()计算str的字符数; bytes的字节数；
print('ABC'.encode('ascii'))  # encode()方法转换str为指定的bytes
print('中文'.encode('utf-8'))  # 中文使用UTF-8编码
print(b'ABC'.decode('ascii'))  # decode()方法将bytes变为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore'))  # 传入errors='ignore'忽略错误的字节

name = 'Anliven'
print("The length of this string: %d" % len(name))  # len(string)方法返回字符串长度
print("name.count('n'): %d" % name.count("n", 0, len(name)))  # 返回str在 string 里面出现的次数
if name.startswith('An'):  # startswith()方法用于查找字符串是否以给定的字符串内容开头
    print('The string starts with "An"')
if 'liven' in name:  # in运算符用以检查给定的字符串是否是查询的字符串中的一部分
    print('It contains the string "liven"')
if name.find('li') != -1:  # find(str, beg=0 end=len(string))方法用于返回子字符串开始的索引值，如果找不到则返回-1
    print('It contains the string "li"')

delimiter = '_*_'
testList = ['Anliven', 'Love', 'Angelina']
print(delimiter.join(testList))  # 联结序列中的项目并生成字符串

aa, bb, cc = 'hello', 'world', '!'
print('%s-%s%s' % (aa, bb, cc))  # 使用%操作符连接字符串
print(aa + "-" + bb + cc)  # 通过+号连接字符串
print('{}-{}{}'.format(aa, bb, cc))  # 使用format方法连接字符串
print(f'{aa}-{bb}{cc}')  # 使用f-string方式连接字符串
print(f'第一个：{aa} 第二个：{bb} 第三个：{cc}')
print('-'.join([aa, bb, cc]))  # 使用join内置方法连接字符串

# ### Number：数字
# Number包括整型、浮点型、布尔型和复数型。Number可以进行常见的数值运算，运算时布尔型True为1，False为0；
#
# ### String：字符串
# - 字符串是一种对象，具有自己的方法；在程序中使用的所有字符串都是str类下的对象；
# - 字符串使用单引号(”)或双引号(“”)括起来，同时使用反斜杠(\)转义特殊字符；
# - 字符串截取的语法格式：变量[头下标:尾下标]；
#
# ### 字符串输出格式化
# 字符串有多种输出方式，最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中；
# 字符串前加上r或R可以使字符串原样输出，防止被转义;
#
# ### str和bytes互换
# 为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换；
# encode()方法转换str为指定的bytes；
# decode()方法将bytes变为str；
# 中文编码范围超过了ASCII编码范围，含有中文的str无法用ASCII编码，会报错；
# 如无特殊业务要求，仅使用UTF-8编码；
#
# ### 连接字符串的方法
# - %操作符
# - +号，适用于连接少量字符串；
# - format方法
# - f-string（Formatted String Literals，字面量格式化字符串）方式，适用性广，可读性较好，python3.6及以上版本支持；
# - join方法，适用于连接大量字符串，但其参数是一个序列类型，例如数组或者元组等；
#
# ### 保存中文
# 源代码包含中文的时，在保存源代码时，务必指定保存为UTF-8编码；
# 指定Python解释器按UTF-8编码读取源代码：“# -*- coding: utf-8 -*-”
#
# ### 字符串常用方法
# - help(str)获取String类的更多信息；
#
# ### 数据结构（ Data Structures）
# - 四种内置的数据结构：列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set），都是使用对象与类的实例；
