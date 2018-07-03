#! python3
# -*- coding: utf-8 -*-
import time


# 理解装饰器 - 步骤1
def myfunc():
    start_time = time.time()
    print("myfunc start...")
    time.sleep(0.6)
    print("myfunc end...")
    end_time = time.time()
    milliseconds = (end_time - start_time) * 1000
    print("------ It's %f ms." % milliseconds)


myfunc()


# 理解装饰器 - 步骤2

def deco2(func):
    start_time = time.time()
    func()
    end_time = time.time()
    milliseconds = (end_time - start_time) * 1000
    print("---- It's %f ms." % milliseconds)


def myfunc2():
    print("myfunc2 start...")
    time.sleep(0.6)
    print("myfunc2 end...")


deco2(myfunc2)  # 此时deco2()实际变成了myfunc2()的装饰器


# 理解装饰器 - 步骤3
def deco3(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        milliseconds = (end_time - start_time) * 1000
        print("------ It's %f ms." % milliseconds)

    return wrapper


def myfunc3():
    print("myfunc3 start...")
    time.sleep(0.6)
    print("myfunc3 end...")


print("Func name is : %s" % myfunc3.__name__)
myfunc3 = deco3(myfunc3)
print("## Decorator!")
print("Func name is : %s" % myfunc3.__name__)
myfunc3()


# 理解装饰器 - 步骤4
def deco4(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        milliseconds = (end_time - start_time) * 1000
        print("------ It's %f ms." % milliseconds)

    return wrapper


@deco4  # 利用@语法，这里实际是将语句“myfunc4 = deco4(myfunc4)”简写为“@deco4”
def myfunc4():
    print("myfunc4 start...")
    time.sleep(0.6)
    print("myfunc4 end...")


print("Func name is : %s" % myfunc4.__name__)
myfunc4()

# ### 装饰器（Decorator）
# 装饰器：在代码运行期间动态增加功能的方式；
# 本质上，decorator就是一个返回函数的高阶函数；
# 使用“@”语法糖精简装饰器的代码；
# 装饰器的作用主要是实现代码重用，多用在函数式编程；
