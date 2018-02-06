#! python3
# -*- coding: utf-8 -*-
import socket  # 导入socket库

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个socket连接对象
s.connect(('127.0.0.1', 9999))  # 建立连接，注意参数是一个tuple，包含地址和端口号

print(s.recv(1024).decode('utf-8'))  # 接收消息，recv(max)方法设置一次最多接收指定的字节数

for data in [b'AAA', b'BBB', b'CCC']:
    s.send(data)  # 发送数据
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()  # 关闭连接

# ### TCP传输控制协议（Transmission Control Protocol）
# 创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器；
# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据；
#
# ### Socket连接
# Python中用socket（）函数来创建套接字；
# AF_INET ： 指定使用IPv4协议
# AF_INET6 ： 指定使用IPv6协议
# SOCK_STREAM ： 指定使用面向流的TCP协议；
# 服务器地址、服务器端口、客户端地址、客户端端口可以唯一确定一个Socket连接；
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接；
#
# ### 用TCP协议进行Socket编程
# 对于客户端，要主动连接服务器的IP和指定端口，
# 对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去；
# 同一个端口，被一个Socket绑定了以后，就无法被别的Socket绑定；
