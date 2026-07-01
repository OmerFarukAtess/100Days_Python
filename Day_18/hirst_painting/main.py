# import colorgram
#
# colors = colorgram.extract('hirst_spot.jpg', 30)
#
# rgb_color = []
# for color in colors:
#     available_color_rgb = color.rgb
#     available_color_tuple = (available_color_rgb[0], available_color_rgb[1], available_color_rgb[2])
#     rgb_color.append(available_color_tuple)
# print(rgb_color)

color_list = [ (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]


import turtle
import random

tim = turtle.Turtle()
tim.hideturtle()
turtle.colormode(255)
tim.penup()
tim.goto(-200,-200)

x = 0
def get_start_position():
    tim.speed("fastest")
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)

    for i in range(10):
        tim.forward(50)
    tim.speed("normal")
    tim.setheading(0)

for _ in range(10):
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
        x+=1
    get_start_position()



screen = turtle.Screen()
screen.exitonclick()
