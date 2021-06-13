import turtle
from turtle import Turtle, Screen
import random



tim = Turtle()
tim.shape("turtle")
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
heading = ["right", "left", "forward", "backward"]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for _ in range(100):
    tim.color(random_color())
    tim.speed(0)
    tim.circle(100)
    tim.left(5)



screen = Screen()
screen.exitonclick()
