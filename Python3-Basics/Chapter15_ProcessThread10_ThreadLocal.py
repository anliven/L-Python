# -*- coding: utf-8 -*-
import threading

local_school = threading.local()  # 创建全局ThreadLocal对象，其每个属性都是线程的局部变量，可以任意读写而互不干扰


def process_student():
    std = local_school.student  # 获取当前线程关联的student
    age = local_school.age
    print(std, age, threading.current_thread().name)


def process_thread(name, age):
    local_school.student = name  # 绑定student属性到全局ThreadLocal对象
    local_school.age = age
    process_student()


t1 = threading.Thread(target=process_thread, args=('AAA', 29), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('BBB', 35), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ### 线程的局部变量
# 在多线程环境下，每个线程都有自己的数据（局部变量），这些局部变量只有线程自己可见，不会影响其他线程；
# 但在函数调用的时候，局部变量难以简洁有效地传递；
#
# ### ThreadLocal
# 一个全局ThreadLocal对象，每个线程都只能读写自己线程的独立副本，互不干扰；
#  - 解决了参数在一个线程中各个函数之间互相传递的问题；
#  - 常用来为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以方便地访问这些资源；
