from turtle import Turtle

#   ____              _           ____ _
#  / ___| _ __   __ _| | _____   / ___| | __ _ ___ ___
#  \___ \| '_ \ / _` | |/ / _ \ | |   | |/ _` / __/ __|
#   ___) | | | | (_| |   <  __/ | |___| | (_| \__ \__ \
#  |____/|_| |_|\__,_|_|\_\___|  \____|_|\__,_|___/___/

START_POS = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []
MOVE = 20

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for start_pos in START_POS:
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.speed(0)
            snake.goto(start_pos)
            self.snake_body.append(snake)  # Adding the body parts


    def move_snake(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE)

    def up(self):
        self.snake_body[0].setheading(90)
        self.move_snake()

    def left(self):
        self.snake_body[0].setheading(180)
        self.move_snake()

    def right(self):
        self.snake_body[0].setheading(0)
        self.move_snake()

    def down(self):
        self.snake_body[0].setheading(270)
        self.move_snake()

