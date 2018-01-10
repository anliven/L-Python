#! python3
# -*- coding: utf-8 -*-

if True:
    print('Yes, it is true')

for i in range(0, 3, 1):  # 内置range函数可以生成数字序列
    print(i)
else:
    print('The for loop is over')
print(list(range(3)))

number = 29
running = True
while running:
    guess = int(input('Enter an integer : '))  # input()函数获取用户输入；int()类型转换
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
print('Done')

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
# Python的条件语句语法格式为if...elif...else；每个条件语句都是:结尾，下一段表示满足条件时执行的语句块；
# - if语句用以检查条件：如果条件为真（True），运行if块语句，否则运行else语句；
# - elif语句实际上将“else if”语句缩减成elif；
# - elif和else语句都是可选的；
# - 可以嵌套使用if语句，在if块的一个if语句中设置另一个if语句；
#
# ### for
# - for x in seq就是把seq的每个迭代元素代入变量x，然后依次执行缩进的语句块；
# - for-in语句能够在一系列对象上进行迭代（Iterates），也就是遍历序列中的每一个项目；
# - for-in语句能在包含任何类型对象的队列中工作；
#
# ### while
# - while语句当其后的判断条件满足时，执行缩进的语句块，否则运行else语句；
# - else子句是可选项；
# - while循环中的else部分总是被执行，除非通过break语句来中断循环；
#
# ### range()
# - 内置的range函数可以生成数字序列，每次只会生成一个数字；
# - range()默认以0作为开始数字，以1逐步递增；
# - 通过list(range()方式可以获得完整的数字列表；
# - 注意生成的序列结束范围；
#
# ### 跳出循环
# 提前跳出循环有两种语法：break和continue。两者区别在于：break是跳出整个循环，而continue是跳出当前循环；
# break语句
# - 可以立刻中断（Break）循环语句的执行，无论循环条件是否为真；
# - 在for或while循环使用了break语句后，任何相应循环中的else块都将不会被执行；
# continue语句
# - 用于跳过当前循环块中的剩余语句，并继续该循环的下一次迭代；
# - 适用于for和while循环；
#
# ### 注意
# - 冒号的使用：if、elif、else、while所在逻辑行必须以冒号结束；
