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

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")


# Listen for keyboard input
screen.listen()






# Exit
screen.exitonclick()