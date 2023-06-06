from turtle import Turtle

# Paddle
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1

# Right Paddle
X_COR = 350
Y_COR = 0

# Left Paddle
X_COR_LEFT = -350
Y_COR_LEFT = 0

# Directions
UP = 90
DOWN = 270


class Paddle:
    def __init__(self):
        self.paddle = []
        self.create_paddle_right()
        self.create_paddle_left()

    def create_paddle_right(self):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.shapesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        new_paddle.penup()
        new_paddle.goto(X_COR, Y_COR)
        self.paddle.append(new_paddle)

    def create_paddle_left(self):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.shapesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        new_paddle.penup()
        new_paddle.goto(X_COR_LEFT, Y_COR_LEFT)
        self.paddle.append(new_paddle)



    def up(self):
        new_y = self.paddle[0].ycor() + 20
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def down(self):
        new_y = self.paddle[0].ycor() - 20
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)
