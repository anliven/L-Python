# -*- coding: utf-8 -*-
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn, TCPServer):  # 服务器类
    pass


class Handler(StreamRequestHandler):  # 请求处理程序类

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write(b'Thank you for connecting')


server = Server(('', 1234), Handler)
server.serve_forever()

# ### 脚本说明
# 以分叉（forking）实现同时处理多个客户端连接请求的服务器；
# 客户端程序可使用：Chapter17_Socket04_Client.py；
# 特别注意：本脚本必须在Linux环境下运行，Windows不支持分叉；
#
# ### 多连接
# 实现多连接的主要三种方式
# - 分叉（forking）：适用UNIX和Linux系统，占用资源多，且在客户端数量巨大时可伸缩性不佳；
# - 线程化：由于线程是共享进程内存，必须确保线程安全，否则可能带来同步问题；
# - 异步I/O：模块select中的select函数，或者实现异步I/O的高级框架（模块asyncore和asynchat）；
