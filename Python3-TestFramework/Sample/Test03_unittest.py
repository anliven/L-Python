# coding=utf-8
import unittest
import Test_source_code as Tsc


class ProductTestCase(unittest.TestCase):

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = Tsc.product(x, y)
                self.assertEqual(p, x * y, 'Integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x /= 10
                y /= 10
                p = Tsc.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')


if '__name__' == '__main__':
    unittest.main()  # 负责运行测试：实例化所有TestCase子类，并执行所有名称以test开头的方法；
