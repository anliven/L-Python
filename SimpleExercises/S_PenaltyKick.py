# -*- coding: utf-8 -*-
__author__ = 'Anliven'

###random模块的choice方法的作用是从一个list中随机挑选一个元素.
from random import choice
###定义双方分数为一个list,初始值都为0,第一个数字为自己分数,第二个为电脑分数
score = [0, 0]
###定义射门和防守方向为一个list
direction = ['left', 'center', 'right']

###函数kick()


def kick():
    print '===You Kick!=== Please choose one side to shoot: left, center, right'
    you = raw_input()
    com = choice(direction)   # random模块的choice方法
    print 'You kickd ' + you + ' --VS-- Computer saved ' + com
    if you == 'left' or you == 'center' or you == 'right':   # 判定方向选择输入是否正确
        if you != com:  # 射门,方向不一致,得一分
            print 'Goal!'
            score[0] += 1   # 分数list的第一个元素的赋值加1
            print 'Score: %d(you) - %d(computer)\n' % (score[0], score[1])
        else:
            print 'Oops...'
            print 'Score: %d(you) - %d(computer)\n' % (score[0], score[1])
    else:
        print 'Typing errors! Exit game!'   # 提示输入出现错误,退出游戏
        exit()

    print '===You Save!=== Please choose one side to save: left, center, right'
    you = raw_input()
    com = choice(direction)
    print 'You saved ' + you + ' --VS-- Computer kicked ' + com
    if you == 'left' or you == 'center' or you == 'right':
        if you == com:
            print 'Saved!'
            print 'Score: %d(you) - %d(computer)\n' % (score[0], score[1])
        else:
            print 'Oops...'
            score[1] += 1
            print 'Score: %d(you) - %d(computer)\n' % (score[0], score[1])
    else:
        print 'Typing errors! Exit game!'
        exit()

times = 0

for times in range(5):   # 点球持续5轮
    print '#Round %d' % (times+1)
    kick()
     
while score[0] == score[1]:  # 打破平局
    times += 1
    print '#Round %d' % (times+1)
    kick()
     
if score[0] > score[1]:  # 打印最终结果
    print 'You Win!'
else:
    print 'Computer Win!.'