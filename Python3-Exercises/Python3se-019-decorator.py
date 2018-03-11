#! python3
# -*- coding: utf-8 -*-
import time
from functools import reduce


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        print(time.asctime(time.localtime(time.time())))
        return r

    return fn


@performance
def factorial(n):
    time.sleep(1)  # 强制推迟执行1秒
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# 实现一个装饰器（@performance），打印出函数调用的时间；
