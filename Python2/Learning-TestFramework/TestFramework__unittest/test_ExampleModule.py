# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 测试模块中的函数 --- 单元测试模块

import unittest
import ExampleModule

class mytest(unittest.TestCase):

    ##初始化工作
    def setUp(self):
        pass

    #退出清理工作
    def tearDown(self):
        pass

    #具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual(ExampleModule.Sum(1, 2), 3, 'test sum fail')
    def testsub(self):
        self.assertEqual(ExampleModule.Sub(2, 1), 1, 'test sub fail')

if __name__ =='__main__':
    unittest.main()
