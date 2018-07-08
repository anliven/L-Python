# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
### 简单的测试

import unittest


class IntegerArithmenticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin 'test*'
        self.assertEquals((2 + 2), 3)
        self.assertEquals(0 + 1, 1)

    def testMultiply(self):
        self.assertEquals((0 * 10), 0)
        self.assertEquals((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()

# ----------------------------------------------------------------------------------------------------------------------
