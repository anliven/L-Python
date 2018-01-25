#! python3
# -*- coding: utf-8 -*-

import unittest


class Dict(dict):  # 待测试的类，一般都是放在单独的.py文件中，放在这里是仅作为举例说明

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):  # 编写一个测试类，从unittest.TestCase继承

    def setUp(self):
        print('# This is setUp()...')

    def test_init(self):  # 测试时，执行以test开头的方法；不以test开头的方法不会被执行；
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言返回的结果是否复合预计
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))  # 断言是否为True

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 断言是否抛出期待的指定类型Error
            value = d['empty']  # 通过d['empty']访问不存在的key时抛出KeyError

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty  # 通过d.empty访问不存在的key时抛出AttributeError

    def tearDown(self):
        print('# This is tearDown()...')


if __name__ == '__main__':  # 把单元测试文件当做正常的python脚本运行
    unittest.main()

# ### 单元测试（Unit Test）
# - 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试
# - 通过单元测试可以说明当前修改不会对程序原有的行为造成影响，但并不意味着程序就一定没有bug；
# - 如果测试不通过，说明当前修改与原有行为不一致，需要进一步的确认和调整；
#
# ### 编写单元测试
# - 编写一个测试类，从unittest.TestCase继承；
# - 对每一类测试编写以test开头的测试方法，测试时会被执行；
# - 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常;
# - unittest.TestCase提供了很多内置的条件判断，只需要调用这些方法就可以断言输出是否是所期望的；
# - 特殊的setUp()和tearDown()方法会分别在每调用一个测试方法的前后被执行；
# - 单元测试代码本身应该非常简洁，如果测试代码太复杂，那么测试代码本身就可能含有bug；
#
# ### 测试驱动开发（TDD：Test-Driven Development）
# - 以测试为驱动的开发模式能够确保一个程序模块的行为通过设计的测试用例；
# - 在后期修改或维护的时，可以极大程度地保证该模块行为仍然是正确的；
#
# ### 运行单元测试
# - 把单元测试文件当做正常的python脚本运行；
# - 在当前目录命令行下通过参数“-m unittest”直接运行单元测试（可以一次批量运行很多单元测试，推荐）；
