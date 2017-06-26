# -*- coding: utf-8 -*-
__author__ = 'Anliven'

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' #'snow'是字符串，不是变量。
print "And everywhere that Mary went."
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, #注意逗号（comma symbol）的使用方法，从输出结果上来区分
print end7 + end8 + end9 + end10 + end11 + end12

print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

#Python逗号的使用方法
#1.逗号在参数传递中的使用：例如def  abc(a,b)或者abc(1,2)
#2.逗号在类型转化中的使用：主要是元组的转换
test = 123
test1 = (test)
test2 = (test,)
test3 = (test,456)
test4 = (test,456,)
print test,test1,test2,test3,test4
#3.逗号在输出语句print中的使用： print语句默认的会在后面加了逗号之后,换行就变成了空格

#友好的Python代码风格:对于代码行的最大长度不超过80个字符