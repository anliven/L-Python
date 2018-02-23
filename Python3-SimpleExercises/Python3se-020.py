#! python3
# -*- coding: utf-8 -*-

test_list = ['aaa', None, '', '111', ' ', '   ']
f = list(filter(lambda s: s and len(s.strip()) > 0, test_list))
print(f)

# 去除列表中的空白字符和空值；
