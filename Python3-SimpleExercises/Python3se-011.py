#! python3
# -*- coding: utf-8 -*-

print("Input a particular year: ")
your_year = int(input())
test_year = (your_year % 4 == 0 and your_year % 100 != 0) or your_year % 400 == 0
if test_year:
    print("This is a leap year.")
else:
    print("This is not a leap year.")

# 判断给定年份是否是闰年
