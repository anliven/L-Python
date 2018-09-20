# -*- coding: utf-8 -*-
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个基于IPv4和TCP协议的Socket
s.bind(('127.0.0.1', 9999))  # 绑定IP地址和监听端口
s.listen(5)  # listen()方法开始监听端口，传入的参数指定等待连接的最大数量
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')  # 发送消息
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':  # 如果接收到exit字符串，直接关闭连接
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:  # 服务器程序通过一个永久循环来接受来自客户端的连接，不会自动退出，必须按Ctrl+C退出程序
    sock, addr = s.accept()  # 接受一个新连接，accept()会等待并返回一个客户端的连接
    t = threading.Thread(target=tcplink, args=(sock, addr))  # 创建新线程来处理TCP连接
    t.start()

# ###Socket（套接字）
# 应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯；
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
