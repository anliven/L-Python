# coding=utf-8
import turtle

turtle.shape("arrow")  # 画笔显示方式
turtle.setup(startx=100, starty=100)  # 窗口起始坐标
turtle.screensize(canvwidth=300, canvheight=300, bg="black")  # 设置画布尺寸和背景

t = turtle.Turtle()
t.speed(50)
t.pensize(2)

t.color('white', 'gray')
t.begin_fill()
while True:
    t.forward(200)
    t.left(150)
    if abs(t.pos()) < 1:
        break
t.end_fill()

t.penup()
t.goto(-100, 100)
t.write("This is a test.", move=True, align="center",  font=("Arial", 8, "normal"))  # 写文本

turtle.exitonclick()

# ### Pen control
# turtle.pendown()  画笔落下
# turtle.penup()  画笔抬起
# turtle.pensize() 画笔粗细
# turtle.color()  画笔颜色和填充颜色
# turtle.begin_fill() 开始填充
# turtle.end_fill() 结束填充
# turtle.write()  文本显示
# ......
