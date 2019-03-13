# -*- coding: utf-8 -*-
import pprint
import sys

print("## sys.patch:", sys.path)
pprint.pprint(sys.path, indent=4)

testList = ['aaa', '111', ['bbb', '222', ['ccc', '333']]]
testDic = {'AAA': {'BBB': {'CCC': {'DDD': 333}}},
           'aaa': [123, [456, [789]]],
           'CCC': "test"}

pp = pprint.PrettyPrinter(width=40, indent=4, depth=2)
pp.pprint(testList)
pp.pprint(testDic)

# ### 标准库pprint模块
# - Data pretty printer
# - https://docs.python.org/3/library/pprint.html
# - 提供了打印任意python数据结构（Python的基本类型）的方法；
# - pprint可以让复杂的结构型对象以可读性更强的格式显示，适用于非普通数据结构的场景；
