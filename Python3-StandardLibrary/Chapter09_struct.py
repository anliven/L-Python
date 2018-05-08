#! python3
# -*- coding: utf-8 -*-
import struct

print(struct.pack('>I', 123456789))  # 第一个参数'>I'是处理指令，">"表示字节顺序是big-endian(网络序)，"I"表示4字节无符号整数
print(struct.pack('>H', 789))  # "H"表示2字节无符号整数
print(struct.pack('>IH', 123456789, 789))  # 参数个数与处理指令个数保持一致
print(struct.calcsize('IH'))

print(struct.pack('>i', '1234'))  # "H"表示2字节无符号整数

print(struct.unpack('>IH', b'\x07[\xcd\x15\x03\x15'))

# ### 标准库struct模块
# - Interpret bytes as packed binary data
# - 官方文档：https://docs.python.org/3/library/struct.html
# - Python不适合编写底层操作字节流的代码，但可以利用struct应对性能要求不高的场景；
#
# ### 一些方法
# - pack(fmt,v1,v2…)：按照给定的格式(fmt)，把数据转换成字符串(字节流)，并将该字符串返回；
# - unpack(fmt,v1,v2…..)：按照给定的格式(fmt)解析字节流，转换成相应的数据类型，并以元组的形式返回解析结果；
# - calcsize(fmt)：计算给定的格式(fmt)占用多少字节的内存；
