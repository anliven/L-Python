#! python3
# -*- coding: utf-8 -*-
import chardet

print("encode: ", 'ABC'.encode('ascii'))  # encode()方法转换str为指定的bytes
print("encode: ", '中文'.encode('utf-8'))  # 中文使用UTF-8编码
print("decode: ", b'ABC'.decode('ascii'))  # decode()方法将bytes变为str
print("decode: ", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore'))  # 传入errors='ignore'忽略错误的字节

data = b'\xe6\xb5\x8b\xe8\xaf\x95\xe7\xbc\x96\xe7\xa0\x81\xe6\xa0\xbc\xe5\xbc\x8f'
print(chardet.detect(data))  # 确认编码后，易于转换为str
print("decode: ", data.decode('utf-8'))

print(chardet.detect('野火烧不尽，春风吹又生。'.encode('gbk')))
print(chardet.detect('野火烧不尽，春风吹又生。'.encode('utf-8')))
print(chardet.detect('最新のニュース'.encode('EUC-JP')))

# ### chardet
# Universal encoding detector for Python 2 and 3
# PYPI: https://pypi.python.org/pypi/chardet/
# Home Page: https://github.com/chardet/chardet
# Documentation: https://chardet.readthedocs.io
#
# 通过encode()和decode()可以转换Unicode表示的str和bytes两种数据类型，如果不知道编码，需要先“猜测”编码，难以有效对bytes做decode()；
# 使用chardet可以对未知编码的bytes做检测，确认编码后，易于转换为str；
