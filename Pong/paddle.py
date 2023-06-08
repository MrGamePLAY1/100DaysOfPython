from turtle import Turtle

# Paddle
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1

# Directions
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.color("white")
        self.shapesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.penup()
        self.goto(pos)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
