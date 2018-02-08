#! python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 调用close()之后不能继续添加新的Process
    p.join()  # Pool对象调用join()方法等待所有子进程执行完毕，调用join()之前必须先调用close()
    print('All subprocesses done.')

# ### Pool
# 可以用进程池的方式批量创建子进程；
# Pool的默认大小是CPU的核数，超过CPU核心数的task要等待前面某个task完成后才执行；
