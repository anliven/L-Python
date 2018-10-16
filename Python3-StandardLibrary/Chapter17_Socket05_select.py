# coding=utf-8
import socket
import select

s = socket.socket()

# host = socket.gethostname()
host = '127.0.0.1'
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [], 5)  # select函数
    for r in rs:
        if r is s:
            c, address = s.accept()
            print('Got connection from', address)
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print(r.getpeername(), 'disconnected')
                inputs.remove(r)
            else:
                print(data)

# ### 脚本说明
# 实现功能：打印所有来自客户端的数据；
#   - 模块select的select函数实现异步I/O；
#   - 只处理当前正在通信的客户端，监听后将客户端加入队列；
#   - 客户端程序可使用：Chapter17_Socket04_Client.py；
#
# ### select.select()
# - 第1个必选参数：序列，需要输入的连接；
# - 第2个必选参数：序列，需要输出的连接；
# - 第3个必选参数：序列，发生异常（错误）的连接；
# - 第4个可选参数：超时时间（单位为秒），如果不指定，select将阻断（等待）直到准备就绪，如果为零，select将不断轮询（不阻断）；
# 返回一个元组（包含3个序列），每个序列都包含相应参数中处于活动状态的文件描述符；
