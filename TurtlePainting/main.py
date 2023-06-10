import turtle
from turtle import Turtle, Screen
import random

# Creating tutle boi
squidward = Turtle()
turtle.colormode(255)
squidward.shape('turtle')
squidward.color('green')
squidward.speed('fastest')


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(degree):
    for _ in range(degree):
        squidward.color(random_colour())
        squidward.circle(100)
        squidward.left(360 / degree)


# draw_spirograph(20)

def million_euro_painting():
    pass


# Draw shape
def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        squidward.forward(100)
        squidward.right(angle)


# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


def random_walk():
    angles = [0, 90, 180, 270]
    squidward.pensize(10)
    squidward.speed('fastest')

    for _ in range(500):
        squidward.hideturtle()
        squidward.pencolor(random_colour())
        # squidward.color(random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'black']))
        squidward.forward(25)
        squidward.setheading(random.choice(angles))


# random_walk()

# Drawing a dotted line
# def draw_dotted(space, x):
#     for i in range(x):
#         squidward.penup()
#         for j in range(x):
#             squidward.dot()
#
#             squidward.forward(space)
#         squidward.backward(space*x)
#     squidward.penup()
#
#
#     squidward.hideturtle()
#
# draw_dotted(15, 20)
# Make a square
# for _ in range(4):
#     squidward.forward(100)
#     squidward.right(90)


# Creating screen module
screen = Screen()
screen.exitonclick()
