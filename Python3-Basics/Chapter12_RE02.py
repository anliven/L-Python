# -*- coding: utf-8 -*-
import re

m = re.match(r'^(\d{3})-(\d{3,8})$', '028-12345678')
print("# match and groups: ", m)
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 预编译正则表达式，提高匹配效率
print("# match and groups: ", re_telephone.match('028-12345678'))
print("# match and groups: ", m.groups(), m.group(),
      m.group(0), m.group(1), m.group(2))  # group(0)是原始字符串，group(1)、group(2)……表示第1、2……个子串

m2 = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print("# groups():{} group():{} group(0):{} group(1):{}".format(m2.groups(), m2.group(), m2.group(0), m2.group(1)))
print("# start(1):{} end(1):{} span(1):{}".format(m2.start(1), m2.end(1), m2.span(1)))

g = re.search(r'www.(.+).com$', 'www.this.is.a.test.com')
print("# search and groups: ", g.groups(), g.group(), g.group(0), g.group(1))

pat = re.compile(r'''
\*    # 起始突出标志：一个星号
(    # 编组的起始位置
[^\*]+    # 与除星号外的其他字符都匹配
)    # 编组结束
\*    # 结束突出标志：一个星号
''', re.VERBOSE)  # 使用re.VERBOSE，忽略在模式中添加的空格、制表符、换行符等，还可以添加注释
print(re.sub(pat, r'<em>\1<em>', 'Hello *world*!'))  # 在替代字符串中使用组号，替换为与模式中编组1匹配的字符串

print(re.sub(r'\*(.+)\*', r'<em>\1<em>', '*This* is *it*!'))  # 贪婪匹配
print(re.sub(r'\*(.+?)\*', r'<em>\1<em>', '*This* is *it*!'))  # 非贪婪匹配

# ### 模式对象
# 每次调用search、match等函数时，在内部必须将字符串表示的的正则表达式转换成为模式对象；
# 使用re.compile()对正则表达式进行转化后（创建模式对象），每次使用时无需再次进行转换，可以提高匹配效率；
# 编译后的正则表达式对象也可用于模块re的普通函数中；
# re.search(REs, string)等价于“pat = re.compile(REs); pat.search(string)”；
#
# ### re匹配对象的重要方法
# 编组（group）就是放在圆括号中的子模式，根据左边的括号数编号的，编组0指的是整个模式；
# 指定一个编组号（或使用默认值0），将只返回一个字符串，否则返回一个元组（包含与给定编组匹配的子串）；
# 除了整个模式（原始字符串，编组为0）外，最多可以有99个编组，编号为1~99；
# - group()：获取与给定子模式（编组）匹配的字符串，等同于group(0)；
# - groups()：所有group组成的一个元组；
# - group(index)：group(1)是第一个匹配成功的子串，group(2)是第二个，依次类推，如果index超了边界，抛出IndexError；
# - start()：返回与给定编组匹配的子串的起始位置；
# - end()：返回与给定编组匹配的子串的起始位置（不包含终止位置）；
# - span()：返回发一个元组，包含与给定编组匹配的子串的起始索引和终止索引；
#
# ### 在替代字符串中使用组号
# 调用re.sub()时，可以在替代字符串中使用组号；
# 在替代字符串中，任何类似“\n”的转义序列都将被替换为与模式中编组n匹配的字符串；
#
# ### 贪婪匹配
# 重复运算符默认是贪婪匹配，也就是匹配尽可能多的字符；
# 对于所有的重复运算符，都可以通过在后面加上“?”来将其指定为非贪婪的（也就是尽可能少匹配）；
