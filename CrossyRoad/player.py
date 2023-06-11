from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)


    def move_up(self):
        # print(self.ycor())
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
        self.setheading(90)
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

