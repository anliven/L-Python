# -*- coding: utf-8 -*-
from socketserver import TCPServer, StreamRequestHandler  # 引入服务器类和处理请求处理器类


class Handler(StreamRequestHandler):  # 从StreamRequestHandler请求处理器类派生子类

    def handle(self):  # 将所有操作都放置在方法handle
        address = self.request.getpeername()
        print('Got connection from', address)
        self.wfile.write(b'Thank you for connecting')  # 属性self.wfile用于写入
        print(self.rfile.read())  # 属性self.rfile用于读取


server = TCPServer(('', 1234), Handler)  # 主机名''表示在本机
server.serve_forever()

# ### 脚本说明
# 基于SocketServer的极简服务器；
# 客户端程序可使用：Chapter17_Socket04_Client.py；
#
# ### 模块SocketServer
# A framework for network servers
# 详细信息：https://docs.python.org/3/library/socketserver.html
# 通过此服务器模块可以创建功能丰富的套接字服务器；
# SocketServer包括四个基本服务器：
#   - TCPServer（支持TCP套接字流，常用）
#   - UDPServer（支持UDP数据包套接字）
#   - UnixStreamServer
#   - UnixDatagramServer
#
# ### 编写与使用
# - 使用模块SocketServer编写服务器时，大部分代码都位于请求处理器中；
# - 每当服务器收到客户端请求时，都将实例化一个清楚处理程序，并对其调用各种处理方法来处理请求；
# - 具体调用的方法取决于使用的服务器类和请求处理程序类；
# - 也可从已有的请求处理程序类派生出子类，从而让服务器调用有一组自定义的处理方法；
#
# ### BaseRequestHandler（基本请求处理类）与StreamRequestHandler（流请求处理类）
# - socketserver.BaseRequestHandler：将所有操作都放在一个服务器调用的方法handle中，可通过属性self.request来访问客户端套接字；
# - socketserver.StreamRequestHandler：处理流（使用TCPSerer时），使用完成连接后将其关闭；
#
# ### 与客户端通信
# - StreamRequestHandler类的对象具有属性self.wfile(用于写入)和属性self.rfile(用于读取)；
# - 通过这两个属性可以与客户端建立通信；
