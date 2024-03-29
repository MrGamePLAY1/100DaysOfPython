from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
new_snake = Snake()  # Snake object
food = Food()  # Food object
score = Scoreboard()  # Scoreboard object


screen.listen()

# ------------- Controls --------------------
screen.onkey(new_snake.up, 'Up')
screen.onkey(new_snake.down, 'Down')
screen.onkey(new_snake.left, 'Left')
screen.onkey(new_snake.right, 'Right')
# -------------------------------------------

#   ____              _           ____
#  / ___| _ __   __ _| | _____   / ___| __ _ _ __ ___   ___   _
#  \___ \| '_ \ / _` | |/ / _ \ | |  _ / _` | '_ ` _ \ / _ \ (_)
#   ___) | | | | (_| |   <  __/ | |_| | (_| | | | | | |  __/  _
#  |____/|_| |_|\__,_|_|\_\___|  \____|\__,_|_| |_| |_|\___| (_)

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move_snake()

    # Food Collision
    if new_snake.head.distance(food) < 22:
        food.refresh()
        new_snake.extend() # Function for the snake to grow
        score.increase_score()

    # Wall Collision
    if new_snake.head.xcor() > 290 or new_snake.head.xcor() < -290 or new_snake.head.ycor() > 290 or new_snake.head.ycor() < -290:
        score.reset()
        new_snake.reset()

    # Collision with snake body
    for bod in new_snake.snake_body[1:]:
        if new_snake.head.distance(bod) < 10:
            score.reset()
            new_snake.reset()


# CLICK TO EXIT
screen.exitonclick()
