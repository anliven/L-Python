# -*- coding: utf-8 -*-


def check_index(key):
    if not isinstance(key, int):
        raise TypeError  # 如果索引key的类型非法，则引发TypeError异常
    if key < 0:
        raise IndexError  # 如果索引key在不允许的范围内，则引发IndexError异常


class ArithmeticSequence:  # 实现一个无穷算术序列（没有__len__方法）
    def __init__(self, st, sp):
        self.start = st  # 起始值
        self.step = sp  # 步长
        self.changed = {}  # 声明一个空字典

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed['key']  # 如果元素的值存在， 则返回，否则会报错KeyError
        except KeyError:
            return self.start + key * self.step  # 返回计算后元素的值

    def __setitem__(self, key, value):
        check_index(key)
        self.changed['key'] = value  # 存储修改后的值


s = ArithmeticSequence(1, 2)
print(type(s), s)
print(s[9])
s[9] = 111
print(s[9])

# ### 基本序列和映射协议
# 序列和映射基本上是元素（item）的集合，实现其基本行为（协议），不可变对象要实现2个方法，而可变对象需要实现4个；
# - __len__(self) ： 返回集合包含的项数；
# - __getitem__(self, key) ： 返回与指定键相关联的值；
# - __setitem__(self, key, value) ：储存指定键相关联的值；
# - __delitem__(self, key) ： 删除指定键相关的值，仅当对象可变（且允许被删除）时才需要实现；
