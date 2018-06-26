# coding=utf-8
import asyncio
import datetime


async def display_date(num, loop):  # 声明一个协程
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
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
#
# ### asyncio.gather()与asyncio.wait()
# 功能相似，书写略有区别；
