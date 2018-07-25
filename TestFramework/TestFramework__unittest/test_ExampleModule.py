# -*- coding: utf-8 -*-
import unittest
import ExampleModule


class MyTest(unittest.TestCase):

    def setUp(self):  # 初始化工作
        pass

    def tearDown(self):  # 退出清理工作
        pass

    def test_sum(self):  # 具体的测试用例，一定要以test开头
        self.assertEqual(ExampleModule.e_sum(1, 2), 3, 'test sum fail')

    def test_sub(self):
        self.assertEqual(ExampleModule.e_sub(2, 1), 1, 'test sub fail')


if __name__ == '__main__':
    unittest.main()
