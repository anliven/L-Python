# -*- coding: utf-8 -*-
import unittest


class IntegerTestCase(unittest.TestCase):  # 继承自unittest.TestCase类
    def testAdd(self):  # 具体的测试用例，一定要以test开头
        self.assertEqual((2 + 2), 3)  # 使用断言判断程序执行结果和预期值是否相符
        self.assertEqual(0 + 1, 1)

    def test_Multiply(self):
        self.assertEqual((0 * 10), 0)  # 断言失败，表明测试不通过
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()
