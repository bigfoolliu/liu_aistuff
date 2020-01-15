#!-*-coding:utf-8-*-
# !@Date: 2018/8/16 21:02
# !@Author: Liu Rui
# !@github: bigfoolliu


import turtle
from turtle import Turtle


def write_text(pensize=5, color="blue", speed=2, start_x=0, start_y=0):
    """书写文本"""
    turtle.penup()
    turtle.pensize(pensize)
    turtle.color(color)
    turtle.speed(speed)

    turtle.home()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    turtle.write("你好", font=("arial", 30))
    turtle.penup()


def draw_triangle(length=50, pensize=5, color="green", speed=2, start_x=0, start_y=0):
    """画一个等边三角形"""
    turtle.penup()
    turtle.pensize(pensize)
    turtle.color(color)
    turtle.speed(speed)
    turtle.home()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    turtle.fd(length)  # 向东移动
    turtle.lt(120)  # 方向设为东偏北120°
    turtle.fd(length)
    turtle.lt(120)  # 方向设为东偏北240°
    turtle.fd(length)

    turtle.penup()


def draw_square(start_x=0, start_y=0, length=20, pensize=5, color="red", speed=2):
    """画一个正方形"""
    turtle.penup()
    turtle.pensize(pensize)
    turtle.color(color)
    turtle.speed(speed)
    turtle.home()

    turtle.goto(start_x, start_y)
    turtle.pendown()

    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)

    turtle.penup()


def main():
    turtle.setup(640, 480, 0, 0)
    turtle.shape("classic")

    draw_triangle(length=200)
    draw_square(start_x=100, start_y=100, length=100)
    write_text()

    turtle.done()


if __name__ == '__main__':
    main()

"""
画python蟒蛇
"""
# import turtle
#
#
# def draw_snake(rad, angle, num, neckrad):
# 	for i in range(num):
# 		turtle.circle(rad, angle)
# 		turtle.circle(-rad, angle)
# 	turtle.circle(rad, angle / 2)
# 	turtle.fd(rad)
# 	turtle.circle(neckrad + 1, 180)
# 	turtle.fd(rad * 2 / 3)
#
#
# def main():
# 	turtle.setup(1300, 800, 0, 0)
# 	python_size = 30
# 	turtle.pensize(python_size)
# 	turtle.pencolor("green")
# 	turtle.seth(-40)
# 	draw_snake(40, 80, 3, python_size / 2)
#
#
# if __name__ == '__main__':
# 	main()
