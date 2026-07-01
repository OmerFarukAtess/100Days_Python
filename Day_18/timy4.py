import random
import turtle as t



tim = t.Turtle()
t.colormode(255)
tim.pensize(10)
tim.speed(10)
tim.color("red")
tim.shape("triangle")
tim.shapesize(0.3)
directions = [0,90,180,270]


def colormode():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rgb = (r, g, b)
    return rgb

for _ in range(200):
    tim.pencolor(colormode())
    tim.setheading(random.choice(directions))
    tim.forward(20)
