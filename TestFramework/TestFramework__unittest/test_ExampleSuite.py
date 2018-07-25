# -*- coding: utf-8 -*-
import random
import unittest


class TestSequenceFunctions(unittest.TestCase):  # 继承自unittest.TestCase类

    def setUp(self):  # 重写了setUp方法
        self.seq = range(10)

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
