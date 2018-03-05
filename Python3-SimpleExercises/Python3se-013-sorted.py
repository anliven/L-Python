#! python3
# -*- coding: utf-8 -*-

test_list = [7, -8, 5, 4, 0, -2, -5]

print(sorted(test_list, key=lambda x: (x < 0, abs(x))))

# 对包含负数和正数的列表进行排序：1.正数在前负数在后，2.整数从小到大，3.负数从大到小；
