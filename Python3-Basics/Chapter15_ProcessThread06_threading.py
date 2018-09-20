# -*- coding: utf-8 -*-
import time
import threading


def loop():  # 新线程执行的代码
    print('Sub-thread %s is running...' % threading.current_thread().name)  # current_thread()函数返回当前线程的实例
    n = 0
    while n < 3:
        n += 1
        print('Sub-thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Sub-thread %s ended.' % threading.current_thread().name)


print('Main-thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 命名子线程为LoopThread，并启动线程
t.start()
t.join()
print('Main-thread %s ended.' % threading.current_thread().name)

# ### threading
# 线程是操作系统直接支持的执行单元，高级语言通常都内置多线程的支持；
# Python的内置模块_thread和threading提供了对多线程的支持；
# 高级模块threading是对低级模块_thread的封装，绝大多数情况下，只需要使用threading模块；
#
# ### 主线程
# 任何进程默认就会启动一个线程，该线程称为主线程，主线程的实例名为MainThread；
# 主线程又可以启动新的线程；
