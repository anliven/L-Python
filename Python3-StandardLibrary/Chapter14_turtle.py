#! python3
# -*- coding: utf-8 -*-
from turtle import Turtle

t = Turtle()
for i in range(5):
    t.forward(150)
    t.right(144)
t.reset()

t2 = Turtle()
for i in range(3):
    t2.forward(150)
    t2.right(120)
t2.clear()

t3 = Turtle()
t3.color('red', 'yellow')
t3.begin_fill()
while True:
    t3.forward(200)
    t3.left(170)
    if abs(t3.pos()) < 1:
        break
t3.end_fill()
t3.clear()

# ### 标准库turtle模块
# turtle — Turtle graphics
# https://docs.python.org/3/library/turtle.html
