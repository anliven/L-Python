#! python3
# -*- coding: utf-8 -*-

import base64

en = base64.b64encode(b'Testing ! \x00')
print(en)
de = base64.b64decode(b'VGhpcyBpcyBhIHRlc3Qh')
print(de)

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # 标准的Base64编码后可能出现字符+和/，在URL中不能直接作为参数
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # 使用"url safe"的base64编码，把字符+和/分别变成-和_
print(base64.urlsafe_b64decode('abcd--__'))


def safe_base64_decode(s):  # 解码去掉“=”的Base64编码
    m = len(s) % 4
    ss = s.decode('ascii')
    for i in range(4 - m):
        ss += '='
    return base64.b64decode(ss.encode())


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

# ### 标准库base64模块
# - Base16, Base32, Base64, Base85 Data Encodings
# - 官方文档：https://docs.python.org/3/library/base64.html
#
# ### Base64
# - 是一种任意二进制到文本字符串的编码方法，适用于小段内容的编码，常用于在URL、Cookie、数字证书签名、网页中传输少量二进制数据;
# - 实际是通过查找已定义编码表的方式来进行编码和解码，可以自定义Base64编码表；
# - 不能用于加密；
