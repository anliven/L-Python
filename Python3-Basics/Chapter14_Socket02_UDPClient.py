#! python3
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'aaa', b'bbb', b'ccc']:
    s.sendto(data, ('127.0.0.1', 9999))  # 不需要调用connect()，直接通过sendto()给服务器发送数据
    print(s.recv(1024).decode('utf-8'))  # 调用recv()方法接收服务器的数据
s.close()

# ### UDP用户数据报协议（User Datagram Protocol）
# UDP是面向无连接的协议，使用UDP协议时，不需要建立连接，只需要知道目的IP地址和端口号，就可以直接发数据包，不保证数据是否被成功接收；
# 虽然UDP传输数据不可靠，但比TCP速度快，对于不要求可靠到达的数据，可以使用UDP协议；
