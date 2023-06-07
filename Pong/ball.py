from turtle import Turtle

# CONSTANTS:
SCREEN_BOTTOM = -300
SCREEN_HEIGHT = 300


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        # move_y = self.ycor() + 7.5
        move_x = self.xcor() + 10
        move_y = self.ycor() + 18
        self.goto(move_x, move_y)

    def wall_collision(self):
        if self.ycor() >= SCREEN_HEIGHT:
            # get the current x and y cordinate
            current_x = self.xcor()
            current_y = self.ycor()

            # invert the x and y coordinate
            current_y = current_y * -1
            current_x = current_x * 2
            self.goto(current_x, current_y)
