# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# Python 测试框架的了解与使用：nose
#
# 仔细阅读nose文档 http://nose.readthedocs.org/en/latest/
#
# >>> import nose
# >>> dir(nose)
# ['DeprecatedTest', 'SkipTest', '__all__', '__author__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', '__versioninfo__', 'case', 'collector', 'config', 'core', 'exc', 'failure', 'importer', 'loader', 'main', 'plugins', 'proxy', 'pyversion', 'result', 'run', 'run_exit', 'runmodule', 'selector', 'suite', 'tools', 'util', 'with_setup']
# >>> dir(nose.tools)
# ['TimeExpired', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'assert_almost_equal', 'assert_almost_equals', 'assert_equal', 'assert_equals', 'assert_false', 'assert_not_almost_equal', 'assert_not_almost_equals', 'assert_not_equal', 'assert_not_equals', 'assert_raises', 'assert_true', 'eq_', 'istest', 'make_decorator', 'nontrivial', 'nontrivial_all', 'nottest', 'ok_', 'raises', 'set_trace', 'timed', 'trivial', 'trivial_all', 'with_setup']
# >>>


# 其他的Python单元测试框架:
#
# doctest---(Python自带的简单自动化测试工具，用于检查文档，也可用于简单一点的单元测试)
# unittest---(Python自带的单元测试框架模块，可用于解决较复杂详细的单元测试，是Junit的Python版本，也被称为PyUnit)
# 更多的单元测试工具，请查看 https://wiki.python.org/moin/PythonTestingToolsTaxonomy 的 Unit Testing Tools 部分。

# Python中assert用来判断语句的真假，如果为假的话将触发AssertionError错误。
# >>> a = 23
# >>> assert a == 23
# >>> assert a == 32
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError
# >>>
