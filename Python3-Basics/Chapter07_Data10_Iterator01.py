# -*- coding: utf-8 -*-


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):  # 声明返回迭代器的方法__iter__
        return self  # 返回迭代器本身


fibs = Fibs()
for f in fibs:  # 在for循环中使用可迭代对象
    if f > 1000:
        print(f)
        break

it = iter([111, 222, 333])  # 对可迭代对象调用内置函数iter，获得一个迭代器
print(next(it))  # 每次调用都返回下一个值
print(next(it))
print(next(it))


# print(next(it))  # 没有可返回的值，引发StopIteration异常


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


t = TestIterator()
print(hasattr(t, '__iter__'), t)
print(list(t))  # 使用list()显示将迭代器转换为列表

# ### 迭代（iterate）
# 迭代意味着重复多次，实现了方法__iter__的对象都是可迭代的；
#
# ### 方法__next__
# 实现了此方法的对象是迭代器；
# 调用此方法时，迭代器应返回其下一个值，如果迭代器没有可返回的值，将引发StopIteration异常；
# 也可利用内置函数next()，在这种情况下，next(it)与it.__next__()等效；
#
# ### 方法__iter__
# 实现了方法__iter__的对象是可迭代的；
# 方法__iter__返回一个迭代器（包含方法__next__的对象），调用时可不提供任何参数；
#
# ### iter()
# https://docs.python.org/3/library/functions.html#iter
# 对可迭代对象调用内置函数iter()，可以获得一个迭代器；
# 也可使用iter()从函数或其他可调用对象创建可迭代对象；
#
# ### next()
# https://docs.python.org/3/library/functions.html#next
# 对迭代器调用其__next__()方法来获取下一个值；
#
# ### 从迭代器创建序列
# 可以将迭代器和可迭代对象转换为序列，例如：可使用list()显示将迭代器转换为列表；
