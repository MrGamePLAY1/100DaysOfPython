from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        left_x = self.xcor() - MOVE_DISTANCE
        self.goto(left_x, self.ycor())

    def move_right(self):
        right_x = self.xcor() + MOVE_DISTANCE
        self.goto(right_x, self.ycor())

    def reset(self):
        self.goto(STARTING_POSITION)
