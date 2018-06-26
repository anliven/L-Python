#! python3
# -*- coding: utf-8 -*-
import multiprocessing


def loop():
    while True:
        pass


if __name__ == '__main__':

    for i in range(multiprocessing.cpu_count()):
        t = multiprocessing.Process(target=loop)
        t.start()

# 注意观察CPU使用率，
# 需要强制终止本程序

# ### 实现多核任务
# 重写一个不带GIL的解释器来真正利用多核 --- 难以实现
# 通过C扩展来实现多线程利用多核 --- 复杂难用
# 通过多进程实现多核任务（多个Python进程有各自独立的GIL锁，互不影响） --- 实用可行
