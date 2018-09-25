# -*- coding: utf-8 -*-
import hashlib
import random

md5 = hashlib.md5()
md5.update('This is a test.'.encode('utf-8'))
print("md5: ", md5.hexdigest())  # 计算MD5值

md5_2 = hashlib.md5()
md5_2.update('This is'.encode('utf-8'))
md5_2.update(' a test.'.encode('utf-8'))
print("md5: ", md5_2.hexdigest())  # 分块多次调用update()后计算MD5值

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print("sha1: ", sha1.hexdigest())

db = {
    'aaa': 'e10adc3949ba59abbe56e057f20f883e',
    'BBB': '878ef96e86145580c38c87f0410ad153'
}


def login(user, password):  # 用户登录验证
    pw_md5 = hashlib.md5()
    pw_md5.update(password.encode('utf-8'))
    return pw_md5.hexdigest() == db[user]


assert login('aaa', '123456')
assert not login('aaa', '123456789')
print('login ok')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):  # 通过对原始口令加一个复杂字符串("加盐")来避免弱口令
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
        print(self.username, self.salt, self.password)


db2 = {
    'xxx': User('xxx', '123456'),
    'yyy': User('yyy', 'abc999')
}


def login2(username, password):
    user = db2[username]
    return user.password == get_md5(password + user.salt)


assert login2('xxx', '123456')
assert not login2('xxx', '123456789')
print('login2 ok')

# ### 标准库hashlib模块
# - Secure hashes and message digests
# - https://docs.python.org/3/library/hashlib.html
#
# ### 摘要算法
# 也称为哈希算法或散列算法：通过摘要函数对任意长度的数据计算出固定长度的摘要digest（通常用16进制的字符串表示）；
# 摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改；
# - 摘要函数是一个单向函数，计算出digest容易，但通过digest反推data却非常困难；
# - 对原始数据做一个bit的修改，都会导致计算出的摘要完全不同；
#
# ### MD5
# 最常见的摘要算法，速度很快，生成结果是固定的128bit长度，通常用一个32位的16进制字符串表示；
#
# ### SHA1
# SHA1的生成结果是固定的160bit长度，通常用一个40位的16进制字符串表示；
# 比SHA1更安全的算法是SHA256和SHA512，越安全的算法生成结果的速度越慢，摘要更长；
#
# ### “加盐”（salt）
# 将随机生成的一个字符串当做“口令”，计算数据的哈希时，根据不通口令计算出不同的哈希，例如计算MD5时采用md5(message + salt)；
# 要验证哈希值，必须同时提供正确的salt；
