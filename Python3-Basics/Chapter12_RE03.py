# coding=utf-8
import fileinput
import re

pat = re.compile('From: (.*)(.*?)$')  # 编译正则表达式，提高效率
for line in fileinput.input(files='Chapter12_RE03_sample.txt', openhook=fileinput.hook_encoded("utf-8")):
    m = pat.match(line)
    if m:
        print("# Sender: ", m.group(1))

pat2 = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
email_addresses = set()
for line in fileinput.input(files='Chapter12_RE03_sample.txt', openhook=fileinput.hook_encoded("utf-8")):
    for address in pat2.findall(line):
        email_addresses.add(address)
for address in sorted(email_addresses):
    print("# Email address:", address)

# ### 示例：找出邮件地址
# re.compile('From: (.*)(.*?)$')
# - 为提高效率，使用re.compile()来编译正则表达式；
# - 提取文本的子模式放在圆括号内，使其成为一个编组；
# - 使用非贪婪模式，只匹配最后一对圆括号；
# - “$”符号表示匹配整行（直到行尾）；
