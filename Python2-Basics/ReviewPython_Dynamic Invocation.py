# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 利用getattr函数实现动态加载

class_name = "TestClass"  # 类名
module_name = "ReviewPython_Dynamic Invocation module file"  # 模块名
method_name = "echo"  # 方法名

module = __import__(module_name)  # 相当于 import module，import是调用内建函数__import__来工作的。
print "# module name:", module  # 打印module对应的模块文件

cla = getattr(module, class_name)  # 利用getattr获取对象module的class_name属性,并赋予cla，此时cla已是一个定义完成的类。

obj = cla()  # 实例化一个cla类的对象obj
print "# obj name:", obj  # 打印obj对应的实例
obj.echo()  # 调用对象obj的echo方法

mtd = getattr(obj, method_name)  # 利用getattr获取对象obj的echo方法属性
print "# method name:", mtd  # 打印mtd对应的方法
mtd()  # 实际上是调用了对象obj的echo方法

mtd_add = getattr(obj, "add")  # 利用getattr获取对象obj的add方法属性
print " # this is a test for add :", mtd_add(1, 2)  # 实际上是调用了对象obj的add方法

mtd_sub = getattr(obj, "sub")  # 利用getattr获取对象obj的sub方法属性
print " # this is a test for sub :", mtd_sub(2, 1)  # 实际上是调用了对象obj的sub方法


# 将如下内容保存在同一个目录下，并命名为 ReviewPython_Dynamic Invocation module file.py的文件
# class TestClass:
#     def sub(self, a, b):
#         return a-b
#
#     def add(self, a, b):
#         return a+b
#
#     def echo(self):
#         print "This is an show for test method"
