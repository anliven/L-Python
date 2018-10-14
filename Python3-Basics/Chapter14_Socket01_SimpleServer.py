# coding=utf-8
import socket

s = socket.socket(family=socket.AF_INET,  # 地址族
                  type=socket.SOCK_STREAM,  # 套接字类型
                  proto=0)  # 协议

# host = socket.gethostname()  # 获取当前主机名
# port = 1234  # 端口号
# address = (host, port)  # 地址是格式为(host, port)的元组
# print("Server address: ", address)
# s.bind(address)  # 绑定地址
s.bind(('127.0.0.1', 1234))  # 绑定地址
s.listen(5)  # 监听地址，指定最多可有5个连接在队列中等待接纳，超出数量将拒绝连接

while True:  # 通常在一个无限循环中完成新连接的建立和处理
    c, addr = s.accept()  # 方法accept将等待，直到客户端连接到来，返回格式为(client, address)的元组
    print('Got connection from', addr)
    c.send(b'Thanks for connecting.')  # # 传输数据，调用方法send发送数据
    c.close()

# ###　脚本说明
# 实现一个最简单的服务端；
# 服务器端套接字必须准备随时处理客户端的一个或多个连接；
# 这里的服务器编程形式为阻断（同步）网络编程；
#
# ### 套接字（socket）
# 套接字基本上是一个信息通道，两端各有一个程序（服务器套接字和客户端套接字），通过套接字可以向对方发送消息；
# 创建服务器套接字后，将在某个网络地址（IP地址和端口号）处监听，等待客户端连接请求，直到和客户端套接字建立连接，双方就能通信；
#
# ### Python中的套接字
# Python中的套接字是模块socket中socket类的实例；
# 在Python中大多数网络编程都隐藏了模块socket的基本工作原理，不会与套接字直接交互；
# 详细信息：https://docs.python.org/3/library/socket.html
