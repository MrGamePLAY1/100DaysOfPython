import colorgram
import turtle
from turtle import Turtle, Screen
import random

# Turtle object
squiddy = Turtle()
squiddy.penup()
# turtle.setworldcoordinates(-1, -1, 20, 20)
# == Attributes ==
squiddy.shape('turtle')
turtle.colormode(255)
squiddy.color('red')
squiddy.speed('fastest')

# colour_search = 25
# colours = colorgram.extract('hirst.jpg', colour_search) # Extracting the colours


colours_extracted = [
    # R   G    B
    (246, 245, 243),
    (233, 239, 246),
    (246, 239, 242),
    (240, 246, 243),
    (132, 166, 205),
    (221, 148, 106),
    (32, 42, 61),
    (199, 135, 148),
    (166, 58, 48),
    (141, 184, 162),
    (39, 105, 157),
    (237, 212, 90),
    (150, 59, 66),
    (216, 82, 71),
    (168, 29, 33),
    (235, 165, 157),
    (51, 111, 90),
    (35, 61, 55),
    (156, 33, 31),
    (17, 97, 71),
    (52, 44, 49),
    (230, 161, 166),
    (170, 188, 221),
    (57, 51, 48),
    (184, 103, 113)
]


# == Main ==
squiddy.penup()
squiddy.setheading(225)
squiddy.forward(300)
squiddy.setheading(0)
num_of_dots = 101


def million_euro_painting():
    # TODO: Print the dots in a 10x10 grid
    # Printing a dot every 10 spaces
    for dot_count in range(1, num_of_dots):
        squiddy.penup()
        squiddy.hideturtle()
        squiddy.dot(20, random.choice(colours_extracted))
        squiddy.fd(50)

        if dot_count % 10 == 0:
            squiddy.setheading(90)
            squiddy.fd(50)
            squiddy.setheading(180)
            squiddy.fd(500)
            squiddy.setheading(0)



million_euro_painting()

# == Functions ==

# def colour_from_colorgram():
# # Loop that finds displays most common colours in rgb
#     for _ in range(colour_search):
#         rgb_colours = []
#         r = colours[_].rgb.r
#         g = colours[_].rgb.g
#         b = colours[_].rgb.b
#
#         colour = (r, g, b)
#         rgb_colours.append(colour)
#         print(rgb_colours)
#
# colour_from_colorgram()

# Creating screen module
screen = Screen()
screen.exitonclick()
