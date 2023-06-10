from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-190, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}",
                   align="center",
                   font=FONT)

