# coding=utf-8
import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())  # threading.currentThread()打印当前线程名称
    yield from asyncio.sleep(1)  # “yield from”语法异步调用asyncio.sleep(1)（可以将其视为是耗时1秒的IO操作）
    print('Hello again! (%s)' % threading.currentThread())


# ### 一些说明
# @asyncio.coroutine将一个generator标记为coroutine类型；
# 在coroutine中通过“yield from”调用另一个generator，也就是asyncio.sleep(1)；
# asyncio.sleep()也是一个coroutine，主线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环；
# 当asyncio.sleep()返回时，线程就可以从“yield from”拿到返回值（这里是None），然后接着执行下一行语句；
# 在asyncio.sleep(1)执行期间，主线程并未等待，而是继续执行EventLoop中其他可以执行的coroutine，从而实现并发执行；


loop = asyncio.get_event_loop()  # get_event_loop方法创建一个事件循环
loop.run_until_complete(hello())  # run_until_complete方法将协程注册到事件循环，并启动事件循环
loop.close()

print(asyncio.iscoroutinefunction(hello))  # 验证是否是协程函数
print(asyncio.iscoroutine(hello()))  # 验证是否是协程对象

# ### 同步IO与异步IO
# 同步IO（Synchronous IO）
#     1. 执行IO操作时，发出IO请求，必须等待IO操作完成（IO结果），才能执行下一步的操作；
#     2. 在“发出IO请求”到等待IO操作完成（IO结果）的这段时间里，主线程只能挂起；
# 异步IO（Asynchronous IO）
#     1. 执行IO操作时，只发出IO请求，不等待IO操作完成（IO结果），而是允许执行后续操作（结束本轮消息处理，进入下一轮消息处理过程）；
#     2. 当IO操作完成（返回IO结果）时，将收到一条“IO完成”的消息，处理该消息时就可以直接获取IO操作结果；
#     3. 在“发出IO请求”到收到“IO完成”的这段时间里，主线程并没有休息，而是在消息循环中继续处理其他消息；
# 简而言之，异步IO就是发起一个IO操作，却不用等它结束，可以继续做其他事情，当它结束时，会得到通知；
# 相比同步IO，在异步IO中一个线程就可以同时处理多个IO请求，将大大提升系统的多任务处理能力；
# 对于大多数IO密集型的应用程序，使用异步IO可以很好地解决高速计算能力和低速IO处理严重不匹配的问题；
#
# ### 协程（Coroutine）
# 简单理解，可将交给标准库asyncio执行的任务称为协程（微线程、纤程），是运行在单线程当中的“并发”，更适用于IO密集型的应用；
# 相比多线程，协程不需要多线程的锁机制，省去了多线程之间的切换开销，让耗时的IO操作异步化，获得了更大的运行效率；
# 协程的使用：
# - 等待另一个协程（产生一个结果，或引发一个异常）；
# - 产生一个结果给正在等它的协程；
# - 引发一个异常给正在等它的协程；
# 运行协程对象：协程对象不能直接运行，需要放置在事件循环（loop）里，只有loop运行了，协程才可能运行；
#
# ### 标准库asyncio
# Python中的标准库asyncio提供了完善的异步IO支持：
# - 用@asyncio.coroutine将一个generator标记为coroutine类型，然后在coroutine内部用“yield from”调用另一个coroutine实现异步操作；
# - 从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程放到EventLoop中执行，从而实现异步IO;
# 标准库asyncio在Python3.4中引入，在Python3.6中由临时版改为了稳定版；
#
# ### 第三方库
# gevent和tornado实现了类似asyncio的功能；
