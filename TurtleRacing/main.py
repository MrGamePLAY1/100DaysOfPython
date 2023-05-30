from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Please make a bet", prompt="What is your bet?")
all_turtles = [] # List of turtles

# attributes of turtles
y_pos = [-180, -140, -100, -60, -20, 20]
colours = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']

# Checking if race is on
race_on = False
# If the user inputs value in textbox then race is on
if user_choice:
    race_on = True

    for i in range(6):

        # Turtle
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.goto(x=-240, y=-y_pos[i])
        new_turtle.color(colours[i])
        all_turtles.append(new_turtle)

while race_on:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)




screen.exitonclick()
