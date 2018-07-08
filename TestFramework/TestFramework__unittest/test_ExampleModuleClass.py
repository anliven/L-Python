# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 测试模块类中的函数 --- 单元测试模块

import unittest
import ExampleModuleClass

class mytest(unittest.TestCase):

##初始化工作
    def setUp(self):
        self.testclass = ExampleModuleClass.Myclass()   ##实例化了被测试模块中的类

    #退出清理工作
    def tearDown(self):
        pass

    #具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual(self.testclass.Sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

