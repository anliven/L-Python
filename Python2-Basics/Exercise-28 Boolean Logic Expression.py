# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 布尔逻辑表达式(boolean logic expression)：逻辑组合的正式名称
# 判断顺序：相等判断的部分 (== or !=) ---- 括号里的 and/or ---- 每一个 not ---- 剩下的 and/or

print 3 != 4 and not ("testing" != "test" or "Python" == "Python")

print True and True
print False and True
print 1 == 1 and 2 == 1
print "test" == "test"
print 1 == 1 or 2 != 1
print True and 1 == 1
print False and 0 != 0
print True or 1 == 1
print "test" == "testing"
print 1 != 0 and 2 == 1
print "test" != "testing"
print "test" == 1
print not (True and False)
print not (1 == 1 and 0 != 1)
print not (10 == 1 or 1000 == 1000)
print not (1 != 10 or 3 == 4)
print not ("testing" == "testing" and "Zed" == "Cool Guy")
print 1 == 1 and not ("testing" == 1 or 1 == 0)
print "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

#Python 和很多语言一样，都是返回两个被操作对象中的一个，而非它们的布尔表达式True 或 False 。
#打印顺序：从右至左
#注意如下示例的情况：说明python识别出了两个被操作的对象，但只按照从右至左的顺序打印了第一个对象的内容。
print "show" and "test"
print "test" and "hi"
print 1 and 1
print 1 and 3
