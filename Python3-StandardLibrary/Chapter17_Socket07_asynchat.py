from asyncore import dispatcher
from asynchat import async_chat
import socket
import asyncore

PORT = 5005  # 设置端口
NAME = b'TestChat'


class ChatSession(async_chat):  # 从async_chat类派生
    """负责处理服务器和单个用户间的连接"""

    def __init__(self, server, sock):
        """标准的设置"""
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator(b'\r\n')  # 设置行结束符
        self.data = []  # 存储已读取的数据
        self.push(b'Welcome to %s\r\n' % self.server.name)  # 问候用户

    def collect_incoming_data(self, data):  # 重写方法
        """从套接字读取数据"""
        # print("### data", data)
        try:
            self.data.append(data.decode('utf-8'))
        except UnicodeDecodeError as err:
            print("# Invalid data", err)

    def found_terminator(self):  # 重写方法
        """如果遇到行结束符，就将这行内容广播给每个人"""
        # print("### self.data", self.data)
        line = ''.join(self.data)  # 使用join方法合并字符串
        self.data = []  # 重置为空列表
        self.server.broadcast(bytes(line.encode()))

    def handle_close(self):
        """客户端断开连接后，将其从会话列表中删除"""
        async_chat.handle_close(self)
        self.server.disconnect(self)


class ChatServer(dispatcher):  # 从dispatcher类派生
    """接收连接并创建会话，进行会话广播"""

    def __init__(self, port, name):  # 重写初始化方法
        """标准的设置"""
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
        self.set_reuse_addr()  # 重用原来的地址（端口号）
        self.bind(('', port))  # 绑定地址和端口，空字符串表明localhost
        self.listen(5)  # 监听连接，最大连接数为5
        self.name = name
        self.sessions = []  # 存储会话列表

    def disconnect(self, session):
        """断开连接"""
        self.sessions.remove(session)

    def broadcast(self, line):
        """广播给其他用户"""
        for session in self.sessions:
            session.push(line + b'\r\n')  # 利用push方法将数据写入async_chat对象
            print("# Broadcast data", (line + b'\r\n'))

    def handle_accept(self):  # 重写事件处理方法
        """创建新的ChatSession对象"""
        conn, address = self.accept()  # 允许客户端连接，返回一个连接(客户端对应的套接字)和地址
        self.sessions.append(ChatSession(self, conn))  # 附加到会话列表末尾
        print('Connection attempt from', address[0])  # 打印客户端IP地址


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()  # 启动服务器的监听循环
    except KeyboardInterrupt as e:  # 避免“使用键盘快捷键关闭服务器显示栈跟踪”
        print(e)

# ### 脚本说明
# 实现基本的服务器程序；
#
# ### 执行脚本
# 1- 启动服务器“python Chapter17_Socket07_asynchat”;
# 2- 使用telnet命令充当客户端“telnet -e 127.0.0.1 5005”，并输入内容;
# 3- 启用多个客户端，并输入内容；
# 4- 服务器端将显示各个客户端的连接信息，然后将显示各个客户端输入的内容；
