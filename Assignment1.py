from turtle import *
import turtle as t
t.screensize(500, 500)
# 【头部轮廓】
t.pensize(5)
t.home()
t.seth(0)
t.pd()
t.color('black')
t.circle(20, 80)  # 0
t.circle(200, 30)  # 1
t.circle(30, 60)  # 2
t.circle(200, 29.5)  # 3
t.color('black')
t.circle(20, 60)  # 4
t.circle(-150, 22)  # 5
t.circle(-50, 10)  # 6
t.circle(50, 70)  # 7
# 确定鼻头大概位置
x_nose = t.xcor()
y_nose = t.ycor()
t.circle(30, 62)  # 8
t.circle(200, 15)  # 9
# 【鼻子】
t.pu()
t.goto(x_nose, y_nose + 25)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(8)
t.end_fill()
# 【眼睛】
t.pu()
t.goto(x_nose + 48, y_nose + 55)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(8)
t.end_fill()
# 【耳朵】
t.pu()
t.color('#444444')
t.goto(x_nose + 100, y_nose + 110)
t.seth(182)
t.pd()
t.circle(15, 45)  # 1
t.color('black')
t.circle(10, 15)  # 2
t.circle(90, 70)  # 3
t.circle(25, 110)  # 4
t.rt(4)
t.circle(90, 70)  # 5
t.circle(10, 15)  # 6
t.color('#444444')
t.circle(15, 45)  # 7
# 【身体】
t.pu()
t.color('black')
t.goto(x_nose + 90, y_nose - 30)
t.seth(-130)
t.pd()
t.circle(250, 28)  # 1
t.circle(10, 140)  # 2
t.circle(-250, 25)  # 3
t.circle(-200, 25)  # 4
t.circle(-50, 85)  # 5
t.circle(8, 145)  # 6
t.circle(90, 45)  # 7
t.circle(550, 5)  # 8
# 【尾巴】
t.seth(0)
t.circle(60, 85)  # 1
t.circle(40, 65)  # 2
t.circle(40, 60)  # 3
t.lt(150)
t.circle(-40, 90)  # 4
t.circle(-25, 100)  # 5
t.lt(5)
t.fd(20)
t.circle(10, 60)  # 6
# 【背部】
t.rt(80)
t.circle(200, 35)
# 【项圈】
t.pensize(20)
t.color('#F03C3F')
t.lt(10)
t.circle(-200, 25)  # 5
# 【爱心铃铛】
t.pu()
t.fd(18)
t.lt(90)
t.fd(18)
t.pensize(6)
t.seth(35)
t.color('#FDAF17')
t.begin_fill()
t.lt(135)
t.fd(6)
t.right(180)  # 画笔掉头
t.circle(6, -180)
t.backward(8)
t.right(90)
t.forward(6)
t.circle(-6, 180)
t.fd(15)
t.end_fill()
# 【前小腿】
t.pensize(5)
t.pu()
t.color('black')
t.goto(x_nose + 100, y_nose - 125)
t.pd()
t.seth(-50)
t.fd(25)
t.circle(10, 150)
t.fd(25)
# 【后小腿】
t.pensize(4)
t.pu()
t.goto(x_nose + 314, y_nose - 125)
t.pd()
t.seth(-95)
t.fd(25)
t.circle(-5, 150)
t.fd(2)
t.hideturtle()
t.done()

