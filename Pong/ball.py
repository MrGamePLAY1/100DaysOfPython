from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.color("white")
        self.x = + 5
        self.y = + 10
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def wall_hit_y(self):
        self.y *= -1

    def paddle_hit_x(self):
        self.x *= -1

