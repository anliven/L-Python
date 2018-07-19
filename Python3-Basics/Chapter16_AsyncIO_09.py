# coding=utf-8
import asyncio


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    co1 = do_some_work(1)
    co2 = do_some_work(2)
    co3 = do_some_work(3)

    tasks = [
        asyncio.ensure_future(co1),
        asyncio.ensure_future(co2),
        asyncio.ensure_future(co3)
    ]

    results = await asyncio.gather(*tasks)  # 使用asyncio.gather创建协程对象，await的返回值是协程运行的结果
    for result in results:
        print('Task result-1: ', result)

    return await asyncio.wait(tasks)  # 不在main协程函数里处理结果，直接返回await的内容


loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())  # un_until_complete()返回main协程的结果
for task in done:
    print('Task result-2: ', task.result())

# ### Chain coroutines（协程嵌套）
# 嵌套的协程，即一个协程中await了另外一个协程；
