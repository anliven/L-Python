#! python3
# -*- coding: utf-8 -*-
import threading

count = 0
lock = threading.Lock()  # threading.Lock()创建一个锁


def change_it(n):  # 先存后取，结果count应该为0
    global count
    count = count + n
    count = count - n


# def run_thread(n):
#     for i in range(100000):
#         change_it(n)


def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 获取锁，
        try:
            change_it(n)  # 执行修改
        finally:  # 用try...finally来确保锁一定会被释放
            lock.release()  # 释放锁


t1 = threading.Thread(target=run_thread, args=(5,))  # 启动线程
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()  # 多个线程同时修改同一个对象内容，如果不使用锁，将导致这个对象内容的修改混乱
t1.join()
t2.join()
print(count)

# ### 多线程中的变量
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响;
# 多线程中，所有变量都由所有线程共享，任何一个变量都可以被任何一个线程修改；
#
# ### 锁（Lock）
# 如果多个线程同时修改同一个对象内容，将导致这个对象内容的修改混乱，利用锁的方式可以避免此问题的发生；
# 通过threading.Lock()来实现创建锁；
# 如果一个线程获得了锁，那么其他线程不能同时执行修改，只能等待，直到锁被释放后，获得该锁的线程才能执行修改；
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以不会造成修改的冲突；
#
# ### 获取与释放锁
# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止；
# 获得锁的线程用完后一定要释放锁，否则其它等待锁的线程将永远等待下去，成为死线程；
#
# ### 锁的优缺点
# 优点: 确保某段关键代码只能由一个线程从头到尾完整地执行;
# 缺点：阻止多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率下降；
# 如果不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，只能强制终止；
# 总而言之，多线程编程的模型复杂，容易发生冲突，必须用锁加以隔离，同时又要小心死锁的发生;
