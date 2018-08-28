# unittest
- Python自带的单元测试框架（The Python unit testing framework），简称为PyUnit，是JUnit的Python版本；
- PyUnit创建于1999，2001年被加入到python2.1的基础类库中，名为unittest；
- 可用于解决较复杂详细的单元测试；
- 更多内容：https://docs.python.org/3/library/unittest.html



# unittest的基本使用
1. 导入unittest模块“import unittest”；
2. 定义一个继承自unittest.TestCase的测试用例类；
3. 定义setUp和tearDown，在每个测试用例的前后做一些辅助工作；
4. 定义测试用例，名字以test开头，测试用例的目的和内容应很明确，一个测试用例应只测试一个方面；
5. 调用assertEqual、assertRaises等断言方法判断程序执行结果和预期值是否相符；
6. 调用unittest.main()启动测试；
7. 如果测试未通过，会输出相应的错误提示，使用-v参数可以获得更多的测试结果信息；



# 常用的断言
```
assertEqual(a, b) ---------- a == b
assertNotEqual(a, b) ---------- a != b
assertTrue(x) ---------- bool(x) is True
assertFalse(x) ---------- bool(x) is False
assertIs(a, b) ---------- a is b
assertIsNot(a, b) ---------- a is not b
assertIsNone(x) ---------- x is None
assertIsNotNone(x) ---------- x is not None
assertIn(a, b) ---------- a in b
assertNotIn(a, b) ---------- a not in b
assertIsInstance(a, b) ---------- isinstance(a, b)
assertNotIsInstance(a, b) ---------- not isinstance(a, b)
```



# 测试的对象与加载
```
单元测试是对程序中最小的可测试模块--函数来进行测试；
被测试对象一定要有输出结果，即使是异常的输出，以便单元测试模块能够捕获返回值，并且与预期值进行比较，从而得出测试通过与否；
unittest会为每一个符合名称要求的函数方法构建一个TestCase对象；

一个测试用例是一个完整的测试流程单元，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)；
通过运行这个测试流程单元，可以对某一个问题进行验证；

单元测试的加载执行方式有2种：
- 通过unittest.main()来启动单元测试的测试模块；
- 添加到TestSuite集合中再加载所有的被测试对象，而TestSuit里存放的就是单元测试的用例；
```



# 简单的测试
将如下内容保存到test_UsingUnittest.py中并执行:
- IDE：直接运行；
- 命令行：进入相应目录，执行“python test_UsingUnittest.py”；
```python
# -*- coding: utf-8 -*-
import unittest


class IntegerTestCase(unittest.TestCase):  # 继承自unittest.TestCase类
    def testAdd(self):  # 具体的测试用例，一定要以test开头
        self.assertEqual((2 + 2), 3)  # 使用断言判断程序执行结果和预期值是否相符
        self.assertEqual(0 + 1, 1)

    def test_Multiply(self):
        self.assertEquals((0 * 10), 0)  # 断言失败，表明测试不通过
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()
```

测试输出结果（命令行）如下：
```
F.    # F表示一个fail，点表示一个通过，E表示程序自身异常
======================================================================
FAIL: testAdd (__main__.IntegerArithmenticTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_UsingUnittest.py", line 11, in testAdd
    self.assertEquals((2 + 2), 3)
AssertionError: 4 != 3
----------------------------------------------------------------------
Ran 2 tests in 0.010s
FAILED (failures=1)  # failures标明测试用例失败个数
```

执行单个测试文件时使用-v参数可以获得更多的测试结果信息，执行“python test_UsingUnittest.py -v” 会给出如下信息：
```
testAdd (__main__.IntegerArithmenticTestCase) ... FAIL
testMultiply (__main__.IntegerArithmenticTestCase) ... ok
```



# 测试函数举例
测试模块中的函数，执行“python test_ExampleModule.py -v”
- 被测模块 --- ExampleModule.py
- 单元测试模块 --- test_ExampleModule.py

测试模块类中的函数，执行“python test_ExampleModuleClass.py -v”
- 被测模块 --- ExampleModuleClass.py
- 单元测试模块 --- test_ExampleModuleClass.py



# 测试套件（TestSuite）
- 一个测试用例是一个完整的测试流程单元，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)；
- 通过运行这个测试流程单元，可以对某一个问题进行验证；
- 多个测试用例集合在一起，组成了TestSuite，而且TestSuite也可以嵌套TestSuite；

unittest的整个过程集成在unittest.main模块中：
- 第一步：TestLoader根据传入的参数（自身的模块__main__）加载已写好TestCase，获得相应的测试用例，即对应具体的测试方法；
- 第二步：makeSuite把自身模块中的所有测试类中的测试方法提取出来，并组装成TestSuite；
- 第三步：然后由TextTestRunner来运行TestSuite进行具体的测试，运行的结果保存在TextTestResult；

unittest模块的成员
- 命令行下执行 import unittest 导入unittest模块，然后执行 dir(unittest) 可查看成员信息；
- 执行dir(unittest.TestCase)可查看TestCase的方法信息；

部分成员说明
- 'TestCase'       ----- 所有测试用例的基本类，给一个测试方法的名字，返回一个测试用例实例；
- 'TestLoader'     ----- 测试用例加载器，其包括多个加载测试用例的方法，返回一个测试套件；
- 'makeSuite'      ----- 通常是由单元测试框架调用的，用于生产testSuite对象的实例；
- 'TestSuite'      ----- 组织测试用例的实例，支持测试用例的添加和删除，最终将传递给testRunner进行测试执行；
- 'TextTestRunner' ----- 进行测试用例执行的实例，其中Text的意思是以文本形式显示测试结果；
- 'TestProgram'    ----- 命令行进行单元测试的调用方法，作用是执行一个测试用例；
- 'main'           ----- unittest.main()方法执行的其实就是TestProgram；

测试套件举例：执行“python test_ExampleSuite.py -v”
- 被测模块 --- ExampleSuite.py
- 单元测试模块 --- test_ExampleSuite.py


单元测试模块示例（test_ExampleSuite.py）
```python
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
```
