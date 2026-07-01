import random
from random import choice
from turtle import Turtle, Screen

timy_the_turtle = Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

for i in range(3,9):
    #timy_the_turtle.color(random.sample(colors,1))
    timy_the_turtle.color(random.choice(colors))
    degree = 360/i
    for j in range(i):
        timy_the_turtle.forward(50)
        timy_the_turtle.right(degree)







screen = Screen()
screen.exitonclick()