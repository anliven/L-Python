# coding=utf-8
import turtle

t = turtle.Turtle()
t.goto(-50, 0)
for j in range(3):
    t.forward(180)
    t.right(120)
t.reset()  # 清空窗口，重置turtle状态为起始状态

t2 = turtle.Turtle()
t2.speed(50)
for i in range(5):
    t2.forward(150)
    t2.right(144)

turtle.exitonclick()  # 保持图案，直到鼠标点击才退出

# ### 标准库turtle模块
# turtle — Turtle graphics
# https://docs.python.org/3/library/turtle.html
#
# ### Turtle motion
# turtle.goto(x,y)  定位到坐标
# turtle.forward()  向前运动
# turtle.backward()  向后运动
# turtle.right()  向右偏转角度
# turtle.left()  向左偏转角度
# turtle.home()  回到起点
# turtle.speed()  运动速度
# ......
