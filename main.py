import turtle
from turtle import Turtle, Screen

import random
#import colorgram
#rgb_color = []
#color = colorgram.extract('dot.jpg', 25)
#for colors in color:
#    r = colors.rgb.r
#    g = colors.rgb.g
#    b = colors.rgb.b
#    new_color = (r,g,b)
#    rgb_color.append(new_color)
#print(rgb_color)
tim = Turtle()
tim.penup()
turtle.colormode(255)
possible_colors = [
                   (195, 172, 122),(156, 97, 59), (186, 159, 52), (9, 54, 78), (124, 38, 26),
                   (54, 35, 28), (110, 69, 85), (119, 162, 176), (29, 118, 162), (74, 37, 44), (85, 137, 66),
                   (71, 152, 131), (10, 63, 44), (119, 36, 42), (181, 99, 82), (208, 202, 144), (144, 176, 158),
                   (180, 153, 159), (177, 201, 188), (217, 180, 174), (32, 78, 61)]

def shit_art():
    for _ in range(10):
        for _ in range(10):
            tim.dot(10,random.choice(possible_colors))
            tim.forward(25)
        tim.left(180)
        tim.forward(250)
        tim.right(90)
        tim.forward(25)
        tim.right(90)

shit_art()



screen = Screen()
screen.exitonclick()