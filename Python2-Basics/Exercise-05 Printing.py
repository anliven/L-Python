# -*- coding: utf-8 -*-
__author__ = 'Anliven'

w = "This is the left side of... "
e = "a string with a right side."
print w + e  # 拼接字符串

print '%s %s %s' % (1, 2.3, ['one', 'two', 'three'])  # 如无特殊需求,都可以使用“%s”来转换成string类型输出

print '%6.2f' % 1.235  # 输出的长度为6个字符，其中小数2位,实际上输出结果中小数点也占用了一位
print '%06.2f' % 1.235  # 如果输出的位数不足6位就用0补足6位
print '%*.*f' % (6, 2, 1.235)  # 不事先指定输出长度和位数，在程序运行过程中再产生
print "." * 10

print '%(name)s:%(score)06.1f' % {'score': 9.5, 'name': 'newsim'}
# 在要输出的内容为dictionary数据类型时，小括号中的(name)和(score)对应于后面的键值对中的键

end1 = "A"
end2 = "B"
end3 = "C"
print end1 + end2 + end3,  # 在print语句的结尾加了逗号后，换行就变成了空格
print end1 + end2 + end3
