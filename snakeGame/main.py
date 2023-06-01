from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
new_snake = Snake()

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









# CLICK TO EXIT
screen.exitonclick()
