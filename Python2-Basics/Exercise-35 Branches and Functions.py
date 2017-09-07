# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 分支和函数（Branches and Functions）

from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    how_much = input("# type a number > ") # input 的参数是一个会被打印出来的字符串，这个字符串一般用来提示用户输入。
    if how_much < 50:
       print "Nice, you're not greedy, you win!"
       exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    while True: # while True 创建了一个无限循环
        nextstep  = raw_input("# take honey? taunt bear? open door? > ")
        if nextstep  == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif nextstep  == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif nextstep == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif nextstep == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    nextstep = raw_input("# flee? head? > ")
    if "flee" in nextstep :
        start()
    elif "head" in nextstep :
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)  # exit()可以中断某个程序，而其中的数字参数则用来表示程序是否是碰到错误而中断的退出代码。

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    nextstep = raw_input("# left? right? > ")
    if nextstep == "left":
        bear_room()
    elif nextstep == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

#sys.exit()是退出python解释器回到上级shell
