# coding=utf-8
import asyncio
import datetime


async def display_date(num, lp):  # 通过async关键字定义一个协程（coroutine）
    end_time = lp.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (lp.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)  # await等同于yield from


loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]  # 将协程存在列表
loop.run_until_complete(asyncio.gather(*tasks))  # 借助asyncio.gather()函数多个协程同时在一个loop里运行
loop.close()

# ### 关键字async与await
# 在Python3.5中引入了async和await关键字，更直接地支持协程，代码更为简洁可读；
# - 关键字async代替了“@asyncio.coroutine”；
# - 关键字await代替了“yield from”；
# 使用async定义协程对象，使用await可以针对耗时的操作进行挂起，函数让出控制权;
# 协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行;
#
# ### asyncio.gather()与asyncio.wait()
# 功能相似，书写略有区别；
# asyncio.wait(tasks)等同于asyncio.gather(*tasks)，前者接受一个task列表，后者接收一堆task；
#
# ### 概念总结
# 1. event_loop（事件循环）
#     程序开启一个无限的循环：函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数；
# 2. coroutine（协程对象，使用async关键字定义的函数）
#     函数被调用时不会立即执行，而是会返回一个协程对象；协程对象需要注册到事件循环，由事件循环调用；
# 3. task（任务）
#     一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态；
# 4. future
#     代表将来执行或没有执行的任务的结果，与task没有本质的区别；
# 5. async/await（用于定义协程的关键字）
#     在Python3.5引入，async定义一个协程，await用于挂起阻塞的异步调用接口；
