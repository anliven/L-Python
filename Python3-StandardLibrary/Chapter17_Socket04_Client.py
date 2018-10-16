# coding=utf-8
import socket

s = socket.socket()
s.connect(('127.0.0.1', 1234))
s.send(b'Hello 111.')
s.send(b'Hello 222.')
s.send(b'Hello 333')
print(s.recv(1024))
