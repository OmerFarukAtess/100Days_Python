import turtle
import random

timy = turtle.Turtle()
turtle.colormode(255)
timy.speed("fastest")

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timy.pencolor(randomcolor())
        timy.circle(80)
        timy.setheading(timy.heading() + size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()

