# -*- coding: utf-8 -*-
import io
import os

testText = '''\
Action is the antidote to despair!
There are two best times to plant a tree: one is ten years ago, and the other is now!
'''
testFile = 'test.txt'

with open(testFile, 'w', encoding="utf-8") as f:  # 引入with语句自动调用close()方法，妥善关闭一个可能打开的数据文件
    f.write(testText)
    print("This is a test!", file=f)  # 利用print函数的file参数，写入数据到文件

with open(testFile) as source, open("target.txt", "w") as target:  # 在一个with语句中调用两个open()
    for line in source.readlines():
        print("# ", line.strip())  # strip()删掉末尾的'\n'
    target.write(source.read())

text = io.open(testFile, encoding="utf-8", errors='ignore').read()
print(text)

os.remove(testFile)
os.remove("target.txt")

# ### 通用换行模式
# readlines等方法能够识别所有合法的换行符（"\n"、"\r"和"\r\n"）；
# open函数的关键字参数newline可设置指定的合法行尾字符，如果设置为空字符串则表示禁止自动转换；
#
# ### with语句
# - with语句会在执行完代码块后自动调用close()方法来关闭文件；
# - 无论文件操作是否成功，是否有异常抛出，with语句都会保证文件被关闭；
# - 可以将两个open()调用合并到一个with语句中，但要将两个open()用逗号隔开；
#
# ### with语句的执行流程
# 上下文管理器是支持“__enter__”方法和“__exit__”方法的对象；
# 使用with语句实际上是在使用上下文管理器：
# - 1.执行open()，返回一个文件对象；
# - 2.调用这个文件对象的“__enter__”方法，并将“__enter__”方法的返回值赋值给as子句中的变量；
# - 3.执行with语句体(with语句代码块)；
# - 4.无论执行过程中是否发生了异常，都会执行文件对象的“__exit__”方法(关闭文件)；
