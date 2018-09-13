# -*- coding: utf-8 -*-

import os
import pickle

testDic = dict(name='Anliven', age=29, score=85)
testFile = 'test.txt'
f = open(testFile, 'wb')
f.write(pickle.dumps(testDic))  # pickle.dumps()可以把任意对象序列化成一个bytes，然后可以把这个bytes写入文件
f.close()
with open(testFile, 'rb') as f:
    print(pickle.loads(f.read()))  # 先把内容读到一个bytes，然后用pickle.loads()反序列化出对象

testList = ['AAA', 'BBB', 'CCC']
testDataFile = 'test.data'
f2 = open(testDataFile, 'wb')
pickle.dump(testList, f2)  # pickle.dump()直接把对象序列化然后写入文件对象
f2.close()
with open(testDataFile, 'rb') as f:
    print(pickle.load(f))  # pickle.load()直接从文件对象中反序列化出对象

os.remove(testFile)
os.remove(testDataFile)

try:
    with open('a_data.txt', 'wb') as a_file, open('b_data.txt', 'wb') as b_file:
        pickle.dump(testDic, file=a_file)
        pickle.dump(testList, file=b_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as p:
    print('Pickling error: ' + str(p))

try:
    with open('a_data.txt', 'rb') as f1, open('b_data.txt', 'rb') as f2:
        print(pickle.load(f1))
        print(pickle.load(f2))
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as p:
    print('Pickling error: ' + str(p))

os.remove('a_data.txt')
os.remove('b_data.txt')

# ### 序列化（pickling）与反序列化（unpickling）
# 在程序运行的过程中，所有的变量都是在内存中，可以随时修改变量，一旦程序结束，变量所占用的内存就被操作系统全部回收；
# 如果没有把在内存中的修改存储到磁盘上，那么下次重新运行程序，变量又会被初始化；
# 这种将变量从内存中变成可存储或传输的过程称之为序列化，也就是说序列化后的内容才可以被存储或用于传输；
# 在Java语言中被称之为serialization，其他语言中的marshalling，flattening等；
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化（unpickling）；
#
# ### Pickle模块
# - Python的pickle模块可用来实现序列化，可以持久地（Persistently）存储任何纯Python对象到文件并读取；
# - 封装（Pickling）：保存数据，通过open以写入二进制（'wb'）模式打开文件，然后调用pickle.dump函数将对象存储到文件
# - 拆封（Unpickling）：恢复数据，以（'rb'）模式打开文件，然后通过pickle.load函数接收返回的对象；
# - 如果在封装或拆封数据时出现问题，pickle模块会产生一个PickleError类型的异常；
# - 导入pickle模块后，可通过help(pickle)了解更多信息；
#
# ### Pickle的问题
# Pickle只能用于Python，并且可能不同版本的Python彼此都不兼容；
# 建议Pickle保存不重要的数据，不能成功地反序列化也没关系；
