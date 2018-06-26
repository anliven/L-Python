# coding=utf-8
import asyncio
import threading


@asyncio.coroutine
def test(i):
    print("Start: ", i, "Thread", threading.currentThread())
    yield from asyncio.sleep(2)  # 使用关键字yield from来阻塞，在这2s中让出CPU的执行权，直到协程asyncio.sleep(2)返回结果
    print("End: ", i, "Thread", threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [test(i) for i in range(3)]  # 多个coroutine可以封装成一组Task然后由一个线程并发执行
loop.run_until_complete(asyncio.wait(tasks))
loop.close()  # 调用loop.close()彻底清理loop对象，防止误用

print(asyncio.iscoroutine(test(1)))  # 验证是否是协程对象

# ### run_until_complete()
# run_until_complete()：开启事件循环（内置add_done_callback），是一个阻塞（blocking）调用，直到协程运行结束才返回；
# 调用协程函数，协程并不会开始运行，只是返回一个协程对象；
# 如果事件循环没有开启，即使调用了协程方法，协程也不会执行；
