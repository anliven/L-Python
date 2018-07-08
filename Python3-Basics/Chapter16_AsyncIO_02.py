# coding=utf-8


def test_yield():
    reply = yield 'hello'  # 第一次启动生成器，运行到“yield 'hello'”中断，并将yield之后表达式的值返回给generator.send()
    # print("reply: ", reply)
    yield reply


ty = test_yield()
print(next(ty))  # 等同于“print(ty.send(None))”，第一次启动生成器时必须send(None)，因为当前还没有yield表达式可以接收参数
print(ty.send('world'))  # 再次通过send()启动生成器时，会从上次中断的地方开始重新启动，赋值给reply


# 协程的实现示例（生产者消费者模式）
# 创建了一个叫做consumer的协程，并且在主线程中生产数据，协程中消费数据
def consume():
    while True:  # 协程等待接收数据
        number = yield  # 当协程执行到yield关键字时暂停（由程序控制），等到主线程调用send方法发送了数据，协程才会接到数据继续执行
        print("开始消费", number)


consumer = consume()  # 创建名为consumer的协程
next(consumer)  # 先执行初始化状态的consumer协程，在yield处停止
for num in range(0, 100):
    print("开始生产", num)
    consumer.send(num)  # 发送数据给consumer协程

# ### yield关键字
# 在一个函数代码中添加yield关键字，python会自动将其识别为一个生成器generator；
# 在generator中，可以通过for循环来迭代，不断调用next()函数来获取由yield语句返回的下一个值；
# yield不但可以返回一个值，还可以接收调用者发出的参数；
# Python对协程的支持是通过generator实现的；
#
# ### generate.send(value)方法
# yield表达式有一个返回值，generate.send(value)方法的作用就是控制这个返回值，参数value就是yield表达式的返回值；
#
# ### “yield from”
# 1. “yield from”会将send的值传递到最里层，再次启动生成器也是从最里层的yield开始启动；
# 2. 当内层的yield结束后，执行外层的yield直到程序结束；
