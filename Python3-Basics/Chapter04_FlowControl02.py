# -*- coding: utf-8 -*-

x = 123
if x:  # 非零数值、非空字符串、非空list等判断为True，否则为False
    print('Yes, it is true')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

names = 'ABC'
for name in names:
    print(name)

for x, y in [(1, 1), (2, 4), (3, 9)]:  # for循环里同时引用2个变量
    print(x, y)

count = 0
for i in range(0, 101, 1):  # 计算1-100的整数之和
    count += i
else:  # 结合else语句使用
    print("1+2+3...+100 : ", count)

count2 = 0
n = 99
while n > 0:  # 计算1-100的整数之和
    count2 += n
    n -= 2
print("1+3+5...+99 :", count2)

number = 29
running = True
while running:
    guess = int(input('Enter an integer : '))  # input()返回的数据类型是str，不能直接和整数比较，必须转换成整数int()
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')

while True:
    s = input("Enter something or quit: ")
    if s == 'quit':
        break
    if len(s) < 3:  # 内置len函数获取字符串的长度
        print('Too small')
        continue
    print('Input is of sufficient length')

# ### FlowControl
# - Python中有三种控制流语句:if，for和while；
# - 条件语句：if...elif...else；
# - 循环结构：while 和 for...in...；
#
# ### if
# 条件语句语法格式为“if...elif...else”，每个条件语句都是“:”结尾，下一段是表示满足条件时执行的语句块；
# - if语句用以检查条件：如果条件为真（True），运行if块语句，否则运行else语句；
# - “False None 0 "" () [] {}”用作if语句中的条件时，都被视为假；
# - elif语句实际上将“else if”语句缩减成elif，可以有多个elif；
# - elif和else语句都是可选的；
# - 可以嵌套使用if语句，在if块的一个if语句中设置另一个if语句；
#
# ### for
# - “for x in seq”就是把seq的每个迭代元素代入变量x，然后依次执行缩进的语句块；
# - for-in语句能够在一系列对象上进行迭代（Iterates），也就是遍历序列中的每一个项目；
# - for-in语句能在包含任何类型对象的队列中工作；
#
# ### while
# - while语句当其后的判断条件满足时，执行缩进的语句块，否则运行else语句；
# - else子句是可选项；
# - while循环中的else部分总是被执行，除非通过break语句来中断循环；
#
# ### range()
# https://docs.python.org/3/library/functions.html#func-range
# - 内置range函数用来生成数字序列，每次只会生成一个数字；
# - range()默认以0作为开始数字，默认以1逐步递增，可以指定起始、结束和步长；
# - Python3中range()返回的是“range object”，而不是实际的list值，但可通过list(range()方式得到一个有序数字列表；
# - 特别注意：生成的序列结束范围；
#
# ### 跳出循环
# 使用break和“continue可以提前跳出循环，break是跳出整个循环，而continue是跳出当前循环；
# 特别注意：break和continue会造成代码执行逻辑分叉过多，容易出错，不要滥用break和continue语句；
# break语句
# - 可以立刻中断循环语句的执行，无论循环条件是否为真；
# - 在for或while循环使用了break语句后，任何相应循环中的else块都将不会被执行；
# continue语句
# - 用于跳过当前的这次循环，直接开始下一次循环；
# - 适用于for和while循环；
#
# ### 注意
# - 冒号的使用：if、elif、else、while所在逻辑行必须以英文冒号结束；
