#! python3
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM指定Socket的类型是UDP
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:  # 手工关闭服务端程序
    data, addr = s.recvfrom(1024)  # recvfrom()方法返回数据和客户端的地址与端口
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)  # 服务器收到数据后，直接调用sendto()把数据用UDP发给客户端

# ### 基于UDP的Socket
# UDP的使用与TCP类似，但是不需要建立连接；
# 不需要调用listen()方法，而是直接接收来自任何客户端的数据；
