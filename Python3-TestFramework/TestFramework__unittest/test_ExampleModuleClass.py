# -*- coding: utf-8 -*-
import unittest
import ExampleModuleClass


class MyTest(unittest.TestCase):

    def setUp(self):  # 初始化工作
        self.testclass = ExampleModuleClass.MyClass()  # 实例化了被测试模块中的类

    def tearDown(self):  # 退出清理工作
        pass

    def test_sum(self):  # 具体的测试用例，一定要以test开头
        self.assertEqual(self.testclass.e_sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
