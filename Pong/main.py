from turtle import Screen
from paddle import Paddle

# CONSTANTS:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong!")

paddle = Paddle()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


# Listen for keyboard input
screen.listen()






# Exit
screen.exitonclick()