# -*- coding: utf-8 -*-

print('字符串: %s 整数: %d 浮点: %f 原样打印: %r' % ('abc', 122, 1.0, 'test\n'))  # 可打印任意数据
print(r'This is the 1st line.\nThis is the 1st line too.')  # 打印原始字符串

print("abc'ABC", '''abc'ABC"123''')  # 双引号之间可以包含单引号，三引号之间可以包含单引号和双引号
print(111, '222', "333", '''444''', """555""")  # 多个字符串之间用逗号“,”隔开
print(111, '222', "333", '''444''', """555""", sep="-")  # 默认以空格作为换行符，可使用sep参数指定分隔符
print('ABC', end=' ')  # 结束默认换行，可使用end参数指定结束符
print('123')

print('(100 + 100)*3 - 45 =', (100 + 100) * 3 - 45)  # 支持数值计算

# n = 12345; print(n)  # 不建议的书写方式
name = 'Anliven'  # 声明变量，使用赋值运算符（=）赋值给变量
age = 29
print('I\'m', name)  # 转义字符\
print("I'm {0}.".format(age))
print(name + ' was ' + str(age) + ' years old.')  # 丑陋易错的方式，不建议使用
print("%s was %s years old." % (name, age))  #
print('{0} was {1} years old.'.format(name, age))
print('{} was {} years old.'.format(name, age))  # 索引数字是可选项

print('{0:.3f}'.format(10.0 / 3))  # 对于浮点数保留小数点(.)后三位
print('{0:_^9}'.format('WOW'))  # 使用下划线填充文本，并保持文字处于中间位置；使用 (^) 定义字符串长度为9

print('This is the 1st line.\nThis is the 2nd line.')  # 换行显示
print('This is the 1st line. \
This is the 2nd line.')  # 换行书写，显式行连接（Explicit Line Joining）
print('''This is the 1st line.
This is the 2nd line.''')  # 用'''...'''格式换行书写

print(repr("Test, \nTest"))  # 使用repr通常会得到内容的合法Python表达式表示
print(str("Test, \nTest"))  # 使用str能以合理方式将内容显示给用户

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
# “%”运算符用来格式化字符串；
# 在字符串内部，“%s”表示用字符串替换，“%d”表示用整数替换，“%f”表示用浮点数替换，“%x”表示用十六进制整数替换；
# 用“%%”来表示字符串里面的普通字符“%”；
# format()方法也可以格式化字符串，{0}对应该格式化方法中的第一个参数，{1}对应第二个参数，以此类推；
#
# ### 索引的计数
# Python从0开始计数，索引中的第一位是0，第二位是1，以此类推；
#
# ### 转义序列（Escape Sequence）
# - 通过反斜杠（\）可以转义特殊字符；
# - 使用转义序列（\\）来指定反斜杠本身；
# - 常用转义序列：换行（\n）、制表（\t）、等等；
# - 在一个字符串中，一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行；
#
# ### 原始字符串
# - 在字符串前增加“r”或“R”来指定一个原始（Raw）字符串；
# - 利用原始字符串可以指定一些未经过特殊处理的字符串，比如转义序列；
#
# ### 物理行（Physical Line）与逻辑行（Logical Line）
# - 物理行：代码的实际所在行；
# - 逻辑行：Python解释器识别的单个语句；
# - 使用分号“;”可以明确表明逻辑行或语句的结束，可以指定多行逻辑行在一行物理行中；
# - Python默认并鼓励每一物理行会对应一个逻辑行，从而使得代码更加可读；
# - 强烈建议：每一行物理行最多对应一行逻辑行，也就是避免使用分号；
#
# ### 缩进（Indentation）
# - Python使用缩进来表示代码块，同一个代码块其语句必须保持相同缩进数；
# - 逻辑行的缩进级别可用于确定语句的分组；
# - 缩进一致:放置在一起的语句（块，block）必须拥有相同的缩进；
# - Python语言官方建议使用四个空格（或者使用定义为4个空格的tab键）作为缩进的单位；
# - 错误的缩进可能会导致运行错误，或引发不期望的行为；
#
# ### 多行语句（多行书写）
# 在Python shell界面或IDE中可以用反斜\或'''...'''实现多行语句；
#
# ### print()
# https://docs.python.org/3/library/functions.html#print
# 内置print()函数用来打印（输出）指定内容；
# 强制参数：
#   - value    打印的值，可多个
# 可选参数：
#   - file     输出流，默认是sys.stdout
#   - sep      多个值之间的分隔符
#   - end      结束符，默认是换行符“\n”
#   - flush    是否强制刷新到输出流，默认否
#
# ### repr()
# https://docs.python.org/3/library/functions.html#repr
# 内置repr()函数用来返回指定对象的合法Python表达式表示；
#
# ### str()
# https://docs.python.org/3/library/functions.html#func-str
# 返回指定对象的字符串形式；
