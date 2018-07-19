# coding=utf-8
import asyncio


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s.'.format(x)


co1 = do_some_work(1)
co2 = do_some_work(2)
co3 = do_some_work(3)

tasks = [  # 创建多个协程的列表
    asyncio.ensure_future(co1),
    asyncio.ensure_future(co2),
    asyncio.ensure_future(co3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for t in tasks:
    print('Task result:', t.result())

# ### asyncio并发简述
# 创建多个协程的列表，然后将这些协程注册到事件循环中；
# 通过多个协程来完成并发任务，每当有任务阻塞的时候就await，然后其他协程继续工作；
