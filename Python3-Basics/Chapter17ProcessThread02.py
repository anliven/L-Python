#! python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os


def run_proc(name):
    print('# Run child process %s (%s)...' % (name, os.getpid()))
    pass  # 子进程要执行的代码


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 传入一个执行函数和函数的参数来创建子进程
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# ### multiprocessing模块
# multiprocessing模块是跨平台版本的多进程模块，提供一个Process类来代表一个进程对象；
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动；
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步；
