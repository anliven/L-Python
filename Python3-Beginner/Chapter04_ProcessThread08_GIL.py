#! python3
# -*- coding: utf-8 -*-
import threading
import multiprocessing


def loop():
    while True:  # 死循环
        pass


for i in range(multiprocessing.cpu_count()):  # multiprocessing.cpu_count()获取CPU核心数
    t = threading.Thread(target=loop)
    t.start()

# 注意观察CPU使用率
# 需要强制终止本程序

# ### GIL锁(Global Interpreter Lock)
# Python的解释器执行代码时，有一个GIL锁（Global Interpreter Lock）
# 任何Python线程执行前，必须先获得GIL锁，然后，不间断地在Python3运行15毫秒，解释器就自动释放GIL锁，让其它线程执行；
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核；
# 简而言之，Python的多线程相当于单核多线程；
# Python解释器由于设计时有GIL全局锁，虽然在Python中可以使用多线程，但并不能有效利用多核，多线程的并发也就难以发挥作用；
