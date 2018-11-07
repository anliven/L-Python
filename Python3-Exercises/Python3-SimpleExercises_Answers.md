
# 001 - 005

### 001 不使用列表，对输入的三个整数做升序排序；
```python
print("Please input 3 numbers : ")
a, b, c = input(), input(), input()
if a >= b:
    first, second = b, a
else:
    first, second = a, b

if c <= first:
    first, second, third = c, first, second
else:
    if c <= second:
        third, second = second, c
    else:
        third = c
print(first, second, third)
```
### 002 实现菜单选项：（1）求和、（2）求平均值、（X）退出；
```python
from random import randint

a, b, c = [randint(1, 1000) for _ in range(3)]
print("There are 3 numbers : ", a, b, c,
      "\nPlease select: (S)summary (A)average (X)exit:")
option = input()
if option == "S":
    print("Sum:", a + b + c)
elif option == "A":
    print("Average:", (a + b + c) / 5)
elif option == "X":
    print("None Selected!")
    exit()
```
### 003 使用while循环计算等差数列“1 4 7 10 13 16 ...”前100项的和；
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
### 004 输入一个100以内正整数，满足条件显示成功并退出，否则提示再次输入，直到满足条件为止；
```python
try_number = int(input("please input a number between 1 and 100:"))
while try_number > 100 or try_number < 1:
    print("It's wrong.")
    try_number = int(input("please input a number between 1 and 100:"))
print("Right!")
```
### 005 判断给定年份是否是闰年；
```python
print("Input a particular year:")
your_year = int(input())
test_year = (your_year % 4 == 0 and your_year % 100 != 0) or your_year % 400 == 0
if test_year:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
```



# 006 - 010

### 006 反转字符串的大小写；
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
### 007 接受一个字符串，然后返回一个仅首字母变成大写的字符串；
```python
def firstCharUpper(s):
    return s[0].upper() + s[1:]
    # return s.title()


print(firstCharUpper('hello'))
```
### 008 按单词反转字符串；
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
### 009 接受一个list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略；
```python
def toUppers(L):
    return [x.upper() for x in L if type(x) == str]


print(toUppers(['Hello', 'world', 101]))
```
### 010 找出所有对称的2位数和3位数；
```python
print([x for x in range(10, 100) if x % 11 == 0])
print([x for x in range(100, 1000) if int(x / 100) == x % 10])
```



# 011 - 015

### 011 以文件形式保存输入内容, 文件名以日期时间作为前缀；
```python
import time

input_content = input("Enter your words:")

localtime = time.strftime("%Y%m%d%H%M%S")
filename = localtime + "_Sample.txt"

f = open(filename, 'wt')
f.write("Some words : %s " % input_content)
f.close()
```
### 012 忽略大小写对一个列表进行排序；
```python
test_list = ['bbb', 'aaa', 'DDD', '111', 'CCC', 'E22']
print(sorted(test_list, key=str.lower))
```
### 013 对包含负数和正数的列表进行排序：1.正数在前负数在后，2.整数从小到大，3.负数从大到小；
```python
test_list = [7, -8, 5, 4, 0, -2, -5]
print(sorted(test_list, key=lambda x: (x < 0, abs(x))))
```
### 014 将一个list所有元素的首字母大写；
```python
def format_name(s):
    return s[:1].upper() + s[1:].lower()


print(list(map(format_name, ['aaa', 'BBB', '1CC', '2dd', '333'])))
```
### 015 对输入的整数进行正向和逆向排序；
```python
import sys

print("Input your numbers and spaces are used between numbers: ")
in_numbers = list(map(int, sys.stdin.readline().split()))
print(sorted(in_numbers))
print(sorted(in_numbers, reverse=True))
```



# 016 - 020

### 016 求一个整数列表所有元素的积；
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
### 017 筛选出1~100中平方根是整数的数；
```python
import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


print(list(filter(is_sqr, range(1, 101))))
```
### 018 去除列表中的空白字符和空值；
```python
test_list = ['aaa', None, '', '111', ' ', '   ']
f = list(filter(lambda s: s and len(s.strip()) > 0, test_list))
print(f)
```
### 019 实现一个装饰器（@performance），打印出函数调用的时间；
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
### 020 创建一个类，可以统计出一共创建了多少个类的实例；
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



# 021 - 025

### 021 将IPv4地址转换成列表；
```python
def myipv4addr(var):
    if isinstance(var, str):
        return var.strip().split('.')
    else:
        print("Wrong IPv4 Address.")


test_ip = "192.168.123.111"
print(myipv4addr(test_ip))
```
### 022 实现字符串和列表的互换，例如"1,a,A" 和 ["1", "a", "A"]；
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
### 023 实现类似字符串"CbaBc"到字符串"C-Bb-Aaa-Bbbb-Ccccc"的转换；
```python
def convert(s):
    return '-'.join(y.upper() + y.lower() * x for x, y in enumerate(s))
```
### 024 将任何非负整数以降序的数字返回，例如“58769”的返回结果为“98765”；
```python
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
```
### 025 以二进制形式返回两个整数的和；
```python
def add_binary(n1, n2):
    return format(n1 + n2, 'b')
```



# 026 - 030

### 026 以位数扩展的形式来表示一个非负整数，例如321的对应表示为“300 + 20 + 1”；
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
### 027 统计指定字符在字符串中出现的次数；
```python
def countChars(s, c):
    return format(s, 's').count(c)
```
### 028 判断字符串中的括号是否有效；
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
### 029 统计字符串中重复元素的个数；
```python
def duplicate(datas):
    d = {}
    for k in datas:
        if k not in d:
            d[k] = 0
        d[k] += 1
    return d
```
### 030 打印列表的索引和对应的元素；
```python
def iterate(datas):
    for i, v in enumerate(datas):
        print("Index: %s - Value: %s" % (i, v))
```



# 031 - 035

### 031 统计一个字符串中相邻n个字符的子字符重复次数；
```python
def get_items(seq, n, r=1):
    items = [seq[pos:pos + n] for pos in range(len(seq) - (n - 1))]  # 利用切片获得所有组合
    for item in set(items):
        rn = items.count(item)
        if rn >= int(r):
            print("The number of '%s' is %d." % (item, rn))  # 打印大于等于指定次数的结果
```
### 032 打印九九乘法表；
```python
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
```
### 033 实现一个带访问计数器的列表；
```python
class CountList(list):
    """A list with access counters"""

    counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CountList, self).__getitem__(index)


t = CountList()
t.append('AAA')
print(t, t[0])
print(t.counter)

t2 = CountList([111, 222, 333])
t2.append(666)
print(t2, t2[0], t2[1], t2[2], t2[3])
print(t2.counter)
```
### 034 合并两个列表排除重复元素；
```
def merge_list(*args):
    s = set()
    for i in args:
        s = s.union(i)
    print(s)
    return s


a = ['a', 'b', 'c', ]
b = ['a', 'A', 'B', 'C']
merge_list(a, b)
```
### 035 将目录路径作为输入参数，返回该目录及子目录中文件的路径；
```
def print_directory_contents(path):
    import os
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


print_directory_contents("D:/AAA/BBB/")
```