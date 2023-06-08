from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

# Scoreboard
scoreboard = Scoreboard()

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
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_hit_y()

    # Collision with paddle (right)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_hit_x()


    # Ball beyond bounds
    if ball.xcor() > 350:
        # Score for left size increase by 1
        scoreboard.l_score += 1
        scoreboard.clear()
        scoreboard.update_scoreboard()
        game_on = False
        ball.reset_position()
        game_on = True



    if ball.xcor() < -360:
        scoreboard.r_score += 1
        scoreboard.clear()
        scoreboard.update_scoreboard()
        game_on = False
        ball.reset_position()
        game_on = True








# Exit
screen.exitonclick()