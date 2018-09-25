# -*- coding: utf-8 -*-
import psutil

# CPU
print("CPU: ", psutil.cpu_count())  # CPU逻辑数量
print("CPU: ", psutil.cpu_count(logical=False))  # CPU物理核心
print("CPU: ", psutil.cpu_times())  # 统计CPU的用户／系统／空闲时间
# for x in range(3):
#     print(psutil.cpu_percent(interval=1, percpu=True))  # 每秒刷新一次CPU使用率

# 内存
print("memory", psutil.virtual_memory())  # 物理内存信息, 以整数字节为单位显示
print("memory", psutil.swap_memory())  # 交换内存信息

# 磁盘
print("disk: ", psutil.disk_partitions())  # 磁盘分区信息
print("disk: ", psutil.disk_usage('/'))  # 磁盘使用情况
print("disk: ", psutil.disk_io_counters())  # 磁盘IO

# 网络
print("network: ", psutil.net_io_counters())  # 网络读写字节／包的个数
print("network: ", psutil.net_if_addrs())  # 网络接口信息
print("network: ", psutil.net_if_stats())  # 网络接口状态
print("network: ", psutil.net_connections())  # 当前网络连接信息

# 进程
print("process: ", psutil.pids())  # 所有进程ID
p = psutil.Process(12052)  # 获取指定进程
print("process: ", p.name(),  # 进程名称
      "\nprocess: ", p.status(),  # 进程状态
      "\nprocess: ", p.exe(),  # 进程exe路径
      "\nprocess: ", p.cwd(),  # 进程工作目录
      "\nprocess: ", p.create_time(),  # 进程创建时间
      "\nprocess: ", p.cmdline(),  # 进程启动的命令行
      "\nprocess: ", p.ppid(),  # 父进程ID
      "\nprocess: ", p.parent(),  # 父进程
      "\nprocess: ", p.children(),  # 子进程列表
      "\nprocess: ", p.username(),  # 进程用户名
      "\nprocess: ", p.cpu_times(),  # 进程使用的CPU时间
      "\nprocess: ", p.memory_info(),  # 进程使用的内存
      "\nprocess: ", p.num_threads(),  # 进程的线程数量
      "\nprocess: ", p.threads(),  # 所有线程信息
      "\nprocess: ", p.environ(),  # 进程环境变量
      "\nprocess: ", p.open_files(),  # 进程打开的文件
      "\nprocess: ", p.connections()  # 进程相关网络连接
      )
# p.terminate()  # 结束进程
psutil.test()  # test()函数可模拟出ps命令的效果

# ### psutil
# - Cross-platform lib for process and system monitoring in Python.
# - Home Page: https://github.com/giampaolo/psutil
# - Documentation: http://psutil.readthedocs.io/en/latest/
