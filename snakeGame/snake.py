from turtle import Turtle

#   ____              _           ____ _
#  / ___| _ __   __ _| | _____   / ___| | __ _ ___ ___
#  \___ \| '_ \ / _` | |/ / _ \ | |   | |/ _` / __/ __|
#   ___) | | | | (_| |   <  __/ | |___| | (_| \__ \__ \
#  |____/|_| |_|\__,_|_|\_\___|  \____|_|\__,_|___/___/

START_POS = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []
MOVE = 20

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for start_pos in START_POS:
            self.add_body(start_pos)

    def reset(self):
        for  seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def add_body(self, start_pos):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.speed(0)
        snake.goto(start_pos)
        self.snake_body.append(snake)  # Adding the body parts

    def extend(self):
        self.add_body(self.snake_body[-1].position())


    def move_snake(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)
            self.move_snake()

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
            self.move_snake()

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
            self.move_snake()

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
            self.move_snake()

