# Python3-SimpleExercises

## 001 - 005

### 001-if：不使用列表或排序算法，对输入的三个整数数排序；
```python
print("Please input 3 numbers : ")
a, b, c = input(), input(), input()
if a >= b:
    first = a
    second = b
else:
    first = b
    second = a

if c >= first:
    third = second
    second = first
    first = c
else:
    if c >= second:
        third = second
        second = c
    else:
        third = c
print(first, second, third)
print(third, second, first)
```
### 002-if：实现菜单选项的功能：（1）求和、（2）求平均值、（X）退出；
```python
from random import randint

a = randint(1, 1000)
b = randint(1, 1000)
c = randint(1, 1000)

print("There are 3 numbers : ", a, b, c)
print("Please select : (1)summary (2)average (X)exit :")
option = input()
if option == "1":
    print(a + b + c)
elif option == "2":
    print((a + b + c) / 5)
elif option == "X":
    print("None Selected!")
    exit()
```
### 003-while：计算等差数列“1 4 7 10 13 16 19 ...”前 100 项的和；
```python
x = 1  # 初始值
Diff = 3  # 差值
Num = 1  # 数目
Sum = 1  # 相加之和

while Num < 100:
    x += Diff
    Num += 1
    Sum += x

print("Sum: ", Sum)
```
### 004-while：输入一个100以内正整数，满足条件显示成功并退出，否则提示再次输入，直到满足条件为止；
```python
try_number = int(input("please input a number between 1 and 100:"))
while try_number > 100 or try_number < 1:
    print("It's wrong.")
    try_number = int(input("please input a number between 1 and 100:"))
print("Right!")
```
### 005-logic：判断给定年份是否是闰年；
```python
print("Input a particular year:")
your_year = int(input())
test_year = (your_year % 4 == 0 and your_year % 100 != 0) or your_year % 400 == 0
if test_year:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
```



## 006 - 010

### 006-function：编写函数：反转字符串的大小写；
```python
def str_swap1(string):
    return string.swapcase()  # 利用string的swapcase方法


def str_swap2(in_string):  # 利用ASCII码
    out_string = ""
    for letter in in_string:
        if 97 <= ord(letter) <= 122:
            out_string += chr(ord(letter) - 32)
        elif 65 <= ord(letter) <= 90:
            out_string += chr(ord(letter) + 32)
        else:
            out_string = out_string + letter
    return out_string


input_string = input('Input a string :')
print(str_swap1(input_string))
print(str_swap2(input_string))
```
### 007-string：编写函数：接受一个字符串，然后返回一个仅首字母变成大写的字符串；
```python
def firstCharUpper(s):
    return s[0].upper() + s[1:]
    # return s.title()


print(firstCharUpper('hello'))
```
### 008-string：编写函数：按单词反转字符串；
```python
import re


def reverse_word(st):
    return ' '.join(st.split()[::-1])


def reverse_word2(st):
    return ''.join(reversed(re.split(r'(\s+|\w+)', st)))  # split by space and word


s = 'Hello  World!'
print(reverse_word(s))
print(reverse_word2(s))
```
### 009-list：编写函数：接受一个list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略；
```python
def toUppers(L):
    return [x.upper() for x in L if type(x) == str]


print(toUppers(['Hello', 'world', 101]))
```
### 010-list：找出所有对称的2位数和3位数；
```python
print([x for x in range(10, 100) if x % 11 == 0])
print([x for x in range(100, 1000) if int(x / 100) == x % 10])
```



## 011 - 015

### 011-file：以文件形式保存输入内容, 文件名以日期时间作为前缀；
```python
import time

input_content = input("Enter your words:")

localtime = time.strftime("%Y%m%d%H%M%S")
filename = localtime + "_Sample.txt"

f = open(filename, 'wt')
f.write("Some words : %s " % input_content)
f.close()
```
### 012-sorted：忽略大小写对一个列表进行排序；
```python
test_list = ['bbb', 'aaa', 'DDD', '111', 'CCC', 'E22']
print(sorted(test_list, key=str.lower))
```
### 013-sorted：对包含负数和正数的列表进行排序：1.正数在前负数在后，2.整数从小到大，3.负数从大到小；
```python
test_list = [7, -8, 5, 4, 0, -2, -5]
print(sorted(test_list, key=lambda x: (x < 0, abs(x))))
```
### 014-map：将一个list所有元素的首字母大写；
```python
def format_name(s):
    return s[:1].upper() + s[1:].lower()


print(list(map(format_name, ['aaa', 'BBB', '1CC', '2dd', '333'])))
```
### 015-map：对输入的整数进行正向和逆向排序；
```python
import sys

print("Input your numbers and spaces are used between numbers: ")
in_numbers = list(map(int, sys.stdin.readline().split()))
print(sorted(in_numbers))
print(sorted(in_numbers, reverse=True))
```



## 016 - 020

### 016-reduce：求一个整数列表所有元素的积；
```python
from functools import reduce  # 引入functools模块的reduce函数


def product(x, y):
    return x * y


print(reduce(product, [1, 4, 9, 16, 25]))


def calc_product(lst):
    def count():
        return reduce(lambda x, y: x * y, lst)

    return count


func = calc_product([1, 2, 3, 4])
print(func())
```
### 017-filter：筛选出1~100中平方根是整数的数；
```python
import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


print(list(filter(is_sqr, range(1, 101))))
```
### 018-filter：去除列表中的空白字符和空值；
```python
test_list = ['aaa', None, '', '111', ' ', '   ']
f = list(filter(lambda s: s and len(s.strip()) > 0, test_list))
print(f)
```
### 019-decorator：实现一个装饰器（@performance），打印出函数调用的时间；
```python
import time
from functools import reduce


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        print(time.asctime(time.localtime(time.time())))
        return r

    return fn


@performance
def factorial(n):
    time.sleep(1)  # 强制推迟执行1秒
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))
```
### 020-class：创建一个类，可以统计出一共创建了多少个类的实例；
```python
class Person(object):
    count = 0

    def __init__(self, name):
        Person.count += 1
        self.name = name


p1 = Person('AAA')
print(Person.count)

p2 = Person('BBB')
print(Person.count)

p3 = Person('CCC')
print(Person.count)
```



## 021 - 025

### 021-string：编写函数：将IPv4地址转换成列表；
```python
def myipv4addr(var):
    if isinstance(var, str):
        return var.strip().split('.')
    else:
        print("Wrong IPv4 Address.")


test_ip = "192.168.123.111"
print(myipv4addr(test_ip))
```
### 022-list： 编写函数：实现字符串和列表的互换，例如"1,a,A" 和 ["1", "a", "A"]；
```python
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
```
### 023：编写函数：实现类似字符串"CbaBc"到字符串"C-Bb-Aaa-Bbbb-Ccccc"的转换；
```python
def convert(s):
    return '-'.join(y.upper() + y.lower() * x for x, y in enumerate(s))
```
### 024：编写函数：将任何非负整数以降序的数字返回，例如“58769”的返回结果为“98765”；
```python
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
```
### 025：编写函数：以二进制形式返回两个整数的和；
```python
def add_binary(n1, n2):
    return format(n1 + n2, 'b')
```



## 026 - 030

### 026：编写函数：以位数扩展的形式来表示一个非负整数，例如321的对应表示为“300 + 20 + 1”；
```python
def expanded_form(num):
    nums = str(num)
    x = []
    for i in range(0, len(nums)):
        if int(nums[i]) != 0:
            s = str(int(nums[i]) * (10 ** (len(nums) - i - 1)))
            x.append(s)
    return ' + '.join(x)
```
### 027：编写函数：统计指定字符在字符串中出现的次数；
```python
def countChars(s, c):
    return format(s, 's').count(c)
```
### 028：编写函数：判断字符串中的括号是否有效；
```python
def valid_parentheses(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        if i == ")":
            cnt -= 1
    if cnt == 0:
        return True
    else:
        return False
```