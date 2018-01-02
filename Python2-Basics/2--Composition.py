# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# 合成(Composition)就是直接使用别的类和模块，实现与继承相同功能的方法。

class Other(object):
    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"


class Child(object):
    def __init__(self):
        self.other = Other()  # 直接使用Other类实例化对象

    def implicit(self):
        self.other.implicit()  # 直接调用Other类的implicit方法

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()  # 直接调用Other类的altered方法
        print "CHILD, AFTER OTHER altered()"


son = Child()
son.implicit()
son.override()
son.altered()

# 继承和合成都能够解决代码重用的问题，可依据需求和习惯来使用

# 建议性指引
# 1. 不惜一切代价地避免多重继承，它带来的麻烦比能解决的问题都多。如果非要用，请准备专研类的层次结构以及花时间去找各种东西的来龙去脉吧。
# 2. 如果有一些代码会在不同位置和场合应用到，那就用合成来把它们做成模块。
# 3. 只有在代码之间有清楚的关联，可以通过一个单独的共性联系起来的时候使用继承，或者受现有代码或者不可抗拒因素所限非用不可的话，那也用吧。

# 提高解决问题能力的唯一方法就是独立自主地去努力解决尽可能多的问题。
