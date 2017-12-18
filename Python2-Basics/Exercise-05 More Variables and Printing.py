# -*- coding: utf-8 -*-
__author__ = 'Anliven'

my_name = 'Anliven'  # 变量名以字母开头
my_age = 35
my_height = 175
my_weight = 72
my_eyes = 'Black'
my_hair = 'Black'

print "Let's talk about %s." % my_name  # "%s"格式化字符串(formatstring);"%"运算符实际上是一种“格式控制工具”
print "He's %d inches tall and %d kilos heavy." % (my_height, my_weight)  # 两个及以上的值则需要用小括号括起来
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# %实际上是一种“格式控制工具”：把右边的变量带到字符串中，并且把变量值放到 %code(字符串格式化代码) 所在的位置上。
# %% 	百分号标记，即在”格式标记字符串“中输出%本身
# %c 	字符及其ASCII码
# %s 	字符串
# %r    打印所有内容
# %d 	有符号整数(十进制)
# %u 	无符号整数(十进制)
# %o 	无符号整数(八进制)
# %x 	无符号整数(十六进制)
# %X 	无符号整数(十六进制大写字符)
# %e 	浮点数字(科学计数法)
# %E 	浮点数字(科学计数法，用E代替e)
# %f 	浮点数字(用小数点符号)
# %g 	浮点数字(根据值的大小采用%e或%f)
# %G 	浮点数字(类似于%g)
# %p 	指针(用十六进制打印值的内存地址)
# %n 	存储输出字符的数量放进参数列表的下一个变量中

# 在python中格式化字符%r，表示打印的是对象，不管什么都打印出来
test = """hello,\nworld"""
print "this is test1: %s" % test
print "this is test2: %r" % test

# 在python中所有东西都可以转换成string类型，因此，如无特殊需求完全可以全部使用’%s‘来标记。
print '%s %s %s' % (1, 2.3, ['one', 'two', 'three'])
# 实际上在这个过程中，Python会先调用整型数的函数，把第一个值也就是1转成string类型，然后再调用str()函数来输出。

print '%6.2f' % 1.235  # 输出的长度为6个字符，其中小数2位,实际上输出结果中小数点也占用了一位
print '%06.2f' % 1.235  # 如果输出的位数不足6位就用0补足6位
print '%*.*f' % (6, 2, 1.235)  # 不事先指定输出长度和位数，在程序运行过程中再产生

print '%(name)s:%(score)06.1f' % {'score': 9.5, 'name': 'newsim'}
# 在要输出的内容为dictionary数据类型时，小括号中的(name)和(score)对应于后面的键值对中的键。
