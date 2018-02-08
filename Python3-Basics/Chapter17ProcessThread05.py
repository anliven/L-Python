#! python3
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import os
import time
import random


def write(q):  # 写数据进程执行的代码
    print('Process to write: %s' % os.getpid())  # getppid()获取进程的ID
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):  # 读数据进程执行的代码
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()  # 父进程创建Queue，并传给各个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动子进程pw，写入
    pr.start()  # 启动子进程pr，读取
    pw.join()  # 等待pw结束
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止

# ### 进程间通信
# multiprocessing模块包装了底层的机制，通过Queue、Pipes等多种方式来交换数据，实现进程间通信；
# Queue方法：在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据；
#
# ### multiprocessing模拟fork
# 在Unix/Linux下，multiprocessing模块封装了fork()调用，不需要关注fork()的细节；
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程，如果multiprocessing在Windows下调用失败，要先检查pickle是否失败了；
