from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Game On
game_on = True

# CONSTANTS:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong!")

# Ball
ball = Ball()

# Paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

# Listen for keyboard input
screen.listen()

while game_on:
    # time.sleep(0.3)
    screen.update()
    ball.move()
    ball.wall_collision()


# Score










# Exit
screen.exitonclick()