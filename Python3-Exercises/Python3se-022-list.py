#! python3
# -*- coding: utf-8 -*-


def myswitch(var):
    if isinstance(var, str):
        return var.strip().split(',')
    elif isinstance(var, list):
        return ",".join(var)
    else:
        print("Wrong Data Type.")


test_str = "1,a,A"
test_list = ["1", "a", "A"]
print(myswitch(test_str))
print(myswitch(test_list))

# 编写函数：实现字符串和列表的互换，例如"1,a,A" 和 ["1", "a", "A"]；
