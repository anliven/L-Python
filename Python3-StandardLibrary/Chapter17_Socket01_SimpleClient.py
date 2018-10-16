# coding=utf-8
import socket

s = socket.socket()  # 创建普通套接字时，不用提供任何参数

# host = socket.gethostname()  # 获取当前主机名
# port = 1234  # 端口号
# address = (host, port)  # 地址是格式为(host, port)的元组
# print("Client address: ", address)
# s.connect(address)  # 客户端套接字连接服务器
s.connect(('127.0.0.1', 1234))  # 客户端套接字连接服务器
print(s.recv(1024))  # 传输数据，调用方法recv接收数据（可指定可接收数据的最大字节数，一般为1024）

# ###　脚本说明
# 实现一个最简单的客户端；
# 客户端套接字处理通常比服务端简单些，只需连接，完成任务后再断开即可；
