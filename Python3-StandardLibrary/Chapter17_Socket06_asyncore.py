# coding=utf-8
import socket
import asyncore  # 模块asyncore让服务器能够依次为连接的所有用户提供服务

PORT = 5005  # 设置端口


class ChatServer(asyncore.dispatcher):

    def __init__(self, port):  # 重写初始化方法
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
        self.set_reuse_addr()  # 重用原来的地址端口号
        self.bind(('', port))  # 绑定地址和端口，空字符串表明localhost
        self.listen(5)  # 监听连接，最大连接数为5

    def handle_accept(self):  # 重写事件处理方法
        conn, address = self.accept()  # 允许客户端连接，返回一个连接(客户端对应的套接字)和地址
        print('Connection attempt from', address[0])  # 客户端IP地址


if __name__ == '__main__':
    s = ChatServer(PORT)
    try:
        asyncore.loop()  # 启动服务器的监听循环
    except KeyboardInterrupt:  # 避免“使用键盘快捷键关闭服务器显示栈跟踪”
        pass

# ### 脚本说明
# 实现极简的服务器程序示例;
#
# ### 执行脚本
# 1- 启动服务器“python Chapter17_Socket06_asyncore.py”;
# 2- 使用telnet命令充当客户端“telnet -e 127.0.0.1 5005”;
# 3- 服务器端将显示“Connection attempt from 127.0.0.1”，然后将断开与客户端的连接；
