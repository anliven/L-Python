# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
# 测试套件举例
# 被测模块 --- ExampleSuite.py

import random


class SFunc:

    def SShuffle(self, req1):
        return random.shuffle(req1)

    def SChoice(self, req2):
        return random.choice(req2)

    def SSample(self, req3, n):
        return random.sample(req3, n)

# random.choice(seq)可以从任何序列seq中返回随机的元素，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。
# random.shuffle(seq)可以将序列seq中的元素随机打乱。
# random.sample(seq,n)可以从指定的序列seq中，随机的截取指定长度n的片断，不作原地修改。

# ----------------------------------------------------------------------------------------------------------------------

### 纯手工测试示例

# >>> import ExampleSuite
# >>>
# >>> dir(ExampleSuite.SFunc)
# ['SChoice', 'SSample', 'SShuffle', '__doc__', '__module__']
# >>>
# >>> test = ExampleSuite.SFunc()
# >>> print test
# <ExampleSuite.SFunc instance at 0x0000000001F02548>
# >>>
# >>> lg = range(10)
# >>> print lg
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>>
# >>> test.SChoice(lg)
# 2
# >>>
# >>> test.SSample(lg,3)
# [2, 4, 9]
# >>>
# >>> print lg
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> test.SShuffle(lg)
# >>> print lg
# [8, 0, 7, 4, 2, 1, 3, 5, 6, 9]
# >>>

# ----------------------------------------------------------------------------------------------------------------------

