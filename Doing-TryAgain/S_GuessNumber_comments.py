# -*- coding: utf-8 -*-
###说明当前Python源程序文件用使用的编码.缺省情况下程序需要使用ascii码来写,但如果在其中写中文的话,python解释器一般会报错,但如果加上utf-8编码，python就会自动处理不再报错。
###上述格式还可以写成：#coding=utf-8 或 #coding:utf-8


##引入随机数模块
from random import randint
##输入名字
##raw_input()将所有输入作为字符串看待并返回字符串类型
name = raw_input('请输入你的名字: ')

##分行读取文件内容并赋值给相关变量
f = open('S_GuessNumber.txt')
lines = f.readlines()
f.close()

##初始化一个空字典scores,并定义相关的键和值
scores = {}
for l in lines:
    s = l.split()  # 每一行数据拆分成list
    scores[s[0]] = s[1:]  # 第一项作为字典的key,剩下的作为value

##查找当前玩家数据,如果没找到,初始化数据
score = scores.get(name)  # 字典的get方法是按照给定key寻找对应项，如果不存在这样的key，就返回空值None
if score is None:
    score = [0, 0, 0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
print "历史记录: 已经玩了%d 次，最少%d 轮猜出答案" % (game_times, min_times)

##定义比较函数


def GuessNumber(num1, num2):
    if num1 > num2:
        print "too big! please try again!"
        return False
    elif num1 < num2:
        print "too small! please try again!"
        return False
    else:
        print "BingGo!"
        return True

##获取随机数
r_number = randint(1, 100)
#print r_number

##单次游戏尝试轮数变量
times = 0

##循环比较
print "Please input your number"
bing = False
while(bing == False):
    t_number = input()
    if t_number < 0 or t_number > 100:
        print "Wrong number! Exit game"
        break
    times += 1
    bing = GuessNumber(t_number, r_number)
print "本次游戏尝试轮数: ", times

##游戏次数
game_times += 1
##单次最少尝试轮数
if times < min_times or min_times == 0:
    min_times = times
##总尝试轮数
total_times = total_times + times
##平均每次尝试轮数
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

##打印相关结果
print "已经玩了%d 次，最少%d 轮猜出答案，平均%.2f 轮猜出答案" % (game_times, min_times, avg_times)

##更新成绩到对应的玩家数据
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'  # !!!
    result += line
##相关结果写入文件
f = open('S_GuessNumber.txt', 'w')
f.write(result)
f.close()


##详细讲解  line = n + ' ' + ' '.join(scores[n]) + '\n' 
## n --- 字典的键
## ' ' --- 空格隔开
## scores[n] --- 字典的值
## ' '.join(scores[n]) --- 以空格将字典的值连接起来
## '\n' --- 换行

#################################################################
