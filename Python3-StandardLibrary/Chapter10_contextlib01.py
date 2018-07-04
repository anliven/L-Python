#! python3
# -*- coding: utf-8 -*-
import os

testText = '''\
Action is the antidote to despair!
There are two best times to plant a tree: one is ten years ago, and the other is now!
'''
testFile = 'test.txt'

with open(testFile, 'w', encoding="utf-8") as f:  # 引入with语句自动调用close()方法，妥善关闭一个可能打开的数据文件
    f.write(testText)

with open(testFile) as source:
    for line in source.readlines():
        print("# ", line.strip())  # 删掉末尾的'\n'

os.remove(testFile)


class ContextManager(object):
    def __enter__(self):
        print("[in __enter__] acquiring resources")

    def __exit__(self, exception_type, exception_value, traceback):
        print("[in __exit__] releasing resources")
        if exception_type is None:
            print("[in __exit__] Exited without exception")
        else:
            print("[in __exit__] Exited with exception: %s" % exception_value)
            return False  # exception_type不为None，“__exit__”方法返回False，异常被重新抛出


with ContextManager():
    print("[in with-body] Testing")
    # raise (Exception("something wrong"))

# ### with语句
# with语句会在执行完代码块后（无论文件操作是否成功，是否有异常抛出）自动调用close()方法来保证文件被关闭；
# 执行流程：
# - 1.执行open()，返回一个文件对象；
# - 2.调用这个文件对象的“__enter__”方法，并将“__enter__”方法的返回值赋值给as子句中的变量；
# - 3.执行with语句体(with语句代码块)；
# - 4.无论执行过程中是否发生了异常，都会执行文件对象的“__exit__”方法(关闭文件)；
#
# ### 上下文管理器
# 上下文管理器是实现了__enter__和__exit__方法的对象；
# 可以将上下文管理器简单理解为：定义了with语句块执行前和执行后的预备条件和操作；
#
# ### 方法__enter__()：
# 在语句体执行前调用；
# 一般用于资源分配，如打开文件、连接数据库、获取线程锁；
# 如果有as子句，with语句将该方法的返回值赋值给as子句中的变量；
#
# ### 方法__exit__(exception_type, exception_value, traceback)：
# 在语句体执行后调用；
# 一般用于资源释放，如关闭文件、关闭数据库连接、释放线程锁；
# 如果with语句体中没有异常发生，调用__exit__(None, None, None)，并且忽略__exit__的返回值；
# 如果with语句体中发生异常，返回一个布尔值表示是否处理异常（True：忽略异常，False：重新抛出异常）；
# 使用sys.exc_info得到的异常信息作为参数调用；
#
# ### 自定义上下文管理器
# 可以通过实现__enter__和__exit__方法来实现一个自定义的上下文管理器；
