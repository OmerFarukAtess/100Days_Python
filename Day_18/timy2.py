from turtle import Turtle,Screen

timy_the_turtle = Turtle()


for i in range(15):
    timy_the_turtle.pendown()
    timy_the_turtle.forward(10)
    timy_the_turtle.penup()
    timy_the_turtle.forward(10)

screen = Screen()
screen.exitonclick()