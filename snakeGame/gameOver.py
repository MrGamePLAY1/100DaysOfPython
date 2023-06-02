from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.goto(0,0)
        self.hideturtle()

    def game_over(self):
        self.write('Game Over', align='center',
                   font=('Arial', 24, 'normal'))