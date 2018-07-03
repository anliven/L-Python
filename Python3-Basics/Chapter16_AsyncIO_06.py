# coding=utf-8
import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)  # 协程compute不会继续往下面执行，直到协程sleep返回结果
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)  # 协程print_sum不会继续往下执行，直到协程compute返回结果
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()

# Chain coroutines
