#! python3
# -*- coding: utf-8 -*-

print('abc')
print("abc'ABC")  # 双引号之间可以包含单引号
print('''abc'ABC"123''')  # 三引号之间可以包含单引号和双引号
print(111, '222', "333", '''444''', """555""")  # 多个字符串用逗号“,”隔开，逗号“,”会输出一个空格
print('100 + 100 =', 100 + 100)  # 计算结果

name = 'Anliven'  # 声明变量，使用赋值运算符（=）赋值给变量
age = 29
print('I\'m', name)  # 转义字符\
print("I'm {0}.".format(age))
print(name + ' was ' + str(age) + ' years old.')  # 丑陋易错的方式；str(age)，类型转换；
print("%s was %s years old." % (name, age))  #
print('{0} was {1} years old.'.format(name, age))
print('{} was {} years old.'.format(name, age))  # 索引数字是可选项

print('{0:.3f}'.format(10.0/3))  # 对于浮点数保留小数点(.)后三位
print('{0:_^9}'.format('WOW'))  # 使用下划线填充文本，并保持文字处于中间位置；使用 (^) 定义字符串长度为9

print('This is the 1st line.\nThis is the 2nd line.')  # 换行显示
print('This is the 1st line. \
This is the 2nd line.')  # 换行书写，显式行连接（Explicit Line Joining）
print('''This is the 1st line.
This is the 2nd line.''')  # 用'''...'''格式换行书写

print(r'This is the 1st line.\nThis is the 2nd line.')  # 原始字符串

# n = 12345; print(n)  # 不建议的书写方式

print("abc")  # print()函数默认会换行，可以使用语法print(str,end='')实现不换行输出
print('ABC', end=' ')  # 以空格结尾，不换行
print('123')

x = "hi"  # Python中的变量不需要声明类型，其在使用前必须赋值
if not isinstance(x, (int, float)):  # 内置函数isinstance()实现数据类型检查
    print('Bad operand type.')

a = b = c = 1
i, j, k = 3.5, 'hello', "python"  # 多个变量同时赋值
print(x, a, b, c, i, j, k)

a = 555  # 重新赋值
b = 888
print('a:', a, 'b:', b)
a, b = b, a  # the fastest way to swap two variables in Python
print('a:', a, 'b:', b)


# ### 一些定义
# - 字面常量（Literal Constants）：表示本身字面意义上的值或内容，常量不能被改变，通常用全部大写的变量名表示；
# - 数字：包括整数（Integers）与浮点数（Floats），例如“11.3E-4”表示“11.3 * 10^-4”
# - 字符串（String）：字符（Characters）的序列（Sequence）
#
# ### 引号
# - 单引号(')：指定字符串，所有引号内的空间，诸如空格与制表符，都将按原样保留；
# - 双引号(")：等同于单引号；
# - 三引号('''或""")：指定多行字符串，可以在三引号之间自由地使用单引号与双引号；
#
# ### 格式化字符串
# %运算符用来格式化字符串；
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，%f表示用浮点数替换，%x表示用十六进制整数替换；
# 用%%来表示字符串里面的普通字符%；
# format()方法也可以格式化字符串，{0}对应该格式化方法中的第一个参数，{1}对应第二个参数，以此类推；
#
# ### Python从0开始计数，索引中的第一位是0，第二位是1，以此类推；
#
# ### 变量（Variables）
# Python中的变量不需要声明类型，其在使用前必须赋值
# Python允许多个变量同时赋值
# 等号=是赋值语句，可以把任意数据类型赋值给变量，可以反复赋值，而且可以赋不同类型的值;
#
# ### 变量的标识符（Identifiers）
# - 首字符必须是字母或下划线（_）；
# - 标识符的其它部分是字符、下划线（_）、数字（0~9）；
# - 标识符名称区分大小写；
#
# ### 数据类型（Data Type）
# - 变量可以将各种形式的值保存为不同的数据类型；
# - python具有基本的数据类型，也可以通过类（Classes）创建自定义的数据类型；
# - 内置的数据类型转换函数：int(),str(),chr(),float(),bool(),hex()等;
# - 内置函数isinstance()实现数据类型检查;
#
# ### 转义序列（Escape Sequence）
# - 通过反斜杠（\）可以转义特殊字符；
# - 使用转义序列（\\）来指定反斜杠本身；
# - 常用转义序列：换行（\n）、制表（\t）、等等；
# - 在一个字符串中，一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行；
#
# ### 原始字符串
# - 在字符串前增加r或R来指定一个原始（Raw）字符串
# - 利用原始字符串可以指定一些未经过特殊处理的字符串，比如转义序列；
#
# ### 物理行（Physical Line）与逻辑行（Logical Line）
# - 物理行：代码的实际所在行
# - 逻辑行：Python解释器识别的单个语句；
# - 使用分号(;)可以明确表明逻辑行或语句的结束，可以指定多行逻辑行在一行物理行中；
# - Python默认并鼓励每一物理行会对应一个逻辑行，从而使得代码更加可读；
# - 强烈建议每一行物理行最多对应一行逻辑行，也就是避免使用分号；
#
# ### print的结尾
# - 默认情况下，print是以一个不可见的换行符（\n）结尾；
# - 如果想避免换行符（\n）出现，可以通过end指定以空白或空格结尾；
#
# ### 缩进（Indentation）
# - Python用缩进来表示代码块，同一个代码块其语句必须保持相同缩进数。
# - 逻辑行的缩进级别可用于确定语句的分组；
# - 缩进一致:放置在一起的语句（块，block）必须拥有相同的缩进；
# - Python语言官方建议使用四个空格（也就是键盘上的Tab键）作为缩进的单位；
# - 错误的缩进可能会导致运行错误，或引发不期望的行为；
#
# ### 多行语句（多行书写）
# 在Python shell界面或IDE中可以用反斜\或'''...'''实现多行语句;
#
# ### Python是动态语言
# 动态语言:变量本身类型不固定；和静态语言相比，动态语言更灵活；
# 静态语言:在定义变量时必须指定变量类型，如果赋值的时类型不匹配，会报错；
