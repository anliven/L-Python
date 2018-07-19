# coding=utf-8
import asyncio


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)  # 使用asyncio.sleep()模拟IO操作；在sleep的时候，使用await让出控制权
    return 'Done after {}s.'.format(x)


def callback(future):  # 回调里的future和创建的task，实际上是同一个对象
    print('Callback: ', future.result())


# def callback(t, future):
#     print('Callback:', t, future.result())


co = do_some_work(3)
loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(co) # ensure_future()和loop.create_task()都可以创建task对象
task = loop.create_task(co)
print(isinstance(task, asyncio.Future))  # task对象是Future类的子类

task.add_done_callback(callback)  # 协程执行结束时会调用回调函数，并通过参数future获取协程执行的结果
# import functools
# task.add_done_callback(functools.partial(callback, 2))

print(task)  # 创建task后，task在加入事件循环之前是pending状态
loop.run_until_complete(task)  # 传入一个协程对象到run_until_complete()，其内部会自动将协程包装成为一个任务（task）对象
print(task)  # task执行完后是finished状态
print('Task result: {}'.format(task.result()))  # task是finished状态时，可以直接读取task的result方法

# ### task对象
# task对象是Future类的子类，保存协程运行后的状态，用于未来获取协程的结果；
# ensure_future()和loop.create_task()都可以创建task对象；
#
# ### 绑定回调
# 协程执行结束时可以调用回调函数，并通过参数future获取协程执行结果（协程返回值）；
# 如果回调需要多个参数，可以通过偏函数导入；
# 创建的task和回调里的future对象，实际上是同一个对象;
#
# ### 阻塞和await
# 当遇到阻塞调用的函数的时候，使用await方法将协程的控制权让出，以便loop调用其他的协程；
