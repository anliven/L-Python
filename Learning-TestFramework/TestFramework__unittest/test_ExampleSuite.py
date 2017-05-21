# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
# 测试套件举例
# 单元测试模块 --- test_ExampleSuite.py

import random
import unittest


class TestSequenceFunctions(unittest.TestCase):  # TestSequenceFunctions继承自unittest.TestCase类

    def setUp(self):  # 重写了setUp方法
        self.seq = range(10)

    def test_shuffle(self):  # 新定义了test_shuffle方法
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):  # 新定义了test_choice方法
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):  # 新定义了test_sample方法
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()

# random.choice(seq)可以从任何序列seq中返回随机的元素，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。
# random.shuffle(seq)可以将序列seq中的元素随机打乱。
# random.sample(seq,n)可以从指定的序列seq中，随机的截取指定长度n的片断，不作原地修改。

# ----------------------------------------------------------------------------------------------------------------------