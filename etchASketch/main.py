# Building a etch-a-sketch game using turtle module
import turtle
from turtle import Turtle, Screen

# Creating the turtle object
stiffy = Turtle()
stiffy.pencolor('black')

# Screen Object
screen = Screen()


def foward():
    stiffy.fd(10)


def turn_left():
    stiffy.left(15)


def turn_right():
    stiffy.right(15)


def backwards():
    stiffy.backward(10)


def clear():
    stiffy.clear()


def go_home():
    stiffy.home()


screen.onkeypress(foward, 'w')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(backwards, 's')
screen.onkeypress(clear, 'space')
screen.onkeypress(go_home, 'h')

screen.listen()

screen.exitonclick()
