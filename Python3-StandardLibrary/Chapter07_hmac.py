# -*- coding: utf-8 -*-
import hmac
import random

message = b'Hello, world!'
key = b'12345'
hm = hmac.new(key, message, digestmod='MD5')
hm.update('Hello'.encode('utf-8'))
hm.update(' Python!'.encode('utf-8'))  # 针对长消息可以多次调用h.update(msg)
print(hm.hexdigest())


def hmac_md5(k, s):
    return hmac.new(k.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'xxx': User('xxx', '123456'),
    'yyy': User('yyy', 'abc999')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


assert login('xxx', '123456')
assert not login('xxx', '123456789')
print('login ok')

# ### 标准库hmac模块
# - Keyed-Hashing for Message Authentication
# - https://docs.python.org/3/library/hmac.html
#
# ### Hmac算法（Keyed-Hashing for Message Authentication）
# 通过一个标准算法，在计算哈希的过程中，把key混入计算过程中；
# 实现了“加盐”的过程，并且针对所有哈希算法都通用；
