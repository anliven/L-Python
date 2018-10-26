# -*- coding: utf-8 -*-


def func():
    while True:
        print("before yield")
        x = yield
        print("after yield:", x)


g = func()
next(g)  # 运行到yield并停在该处，等待下一个next
g.send(1)  # 给yield发送值1，赋值给x并打印，然后继续下一次循环停在yield处
g.send(2)  # 给yield发送值2，赋值给x并打印，然后继续下一次循环停在yield处
next(g)  # 没有给x赋值，执行print语句，打印“None”，继续循环停在yield处

# ### generate.send(value)方法
# yield表达式有一个返回值，generate.send(value)方法的作用就是控制这个返回值，参数value就是yield表达式的返回值；
