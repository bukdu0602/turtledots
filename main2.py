import turtle
from turtle import Turtle, Screen
import random

color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

x = -200
y = -200

for _2 in range(9):
    tim.speed(0)
    tim.up()
    tim.setposition(x, y)
    for _ in range(9):
        tim.dot(20, random.choice(color_list))
        tim.up()
        tim.forward(50)
        tim.dot(20, random.choice(color_list))
        if _ == 8:
            y += 50
            break

tim.home()
tim.sety(50)
tim.dot(20, random.choice(color_list))



screen = Screen()
screen.exitonclick()