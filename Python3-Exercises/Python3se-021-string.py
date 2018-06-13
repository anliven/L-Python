#! python3
# -*- coding: utf-8 -*-


def myipv4addr(var):
    if isinstance(var, str):
        return var.strip().split('.')
    else:
        print("Wrong IPv4 Address.")


test_ip = "192.168.123.111"
print(myipv4addr(test_ip))

# 编写函数：将IPv4地址转换成列表；
