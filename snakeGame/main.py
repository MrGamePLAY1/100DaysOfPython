from turtle import Turtle, Screen
import time

#   ____              _           ____
#  / ___| _ __   __ _| | _____   / ___| __ _ _ __ ___   ___   _
#  \___ \| '_ \ / _` | |/ / _ \ | |  _ / _` | '_ ` _ \ / _ \ (_)
#   ___) | | | | (_| |   <  __/ | |_| | (_| | | | | | |  __/  _
#  |____/|_| |_|\__,_|_|\_\___|  \____|\__,_|_| |_| |_|\___| (_)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake_coords = [(0, 0), (-20, 0), (-40, 0)]
food_coords = [(0, 20), (20, 20), (40, 20, 40)]

# Snake body
body = []

# Creating the snake
for pos in snake_coords:
    snake = Turtle(shape='square')
    snake.penup()
    snake.speed(0)
    snake.color('white')
    snake.goto(pos)
    body.append(snake)



game_on = True
while game_on:
    screen.update()
    for bod in body:
        bod.forward(20)
        time.sleep(0.1)

        for bod_num in range (len(body) -1, 0, -1):
            new_x = body[bod_num - 1].xcor() # second last pos of snake (x)
            new_y = body[bod_num - 1].ycor() # Second last pos of snake (y)
            body[bod_num].goto(new_x, new_y)

    body[0].forward(20)
    body[0].left(90)



screen.exitonclick()
