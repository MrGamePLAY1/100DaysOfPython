import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player creation
player = Player()

# Scoreboard creation
scoreboard = Scoreboard()

# Car creation
cars = []

for _ in range(10):
    car = CarManager()
    cars.append(car)

# Controls
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    for car in cars:
        car.move() # move all cars
        time.sleep(0.1)

    screen.update()

screen.exitonclick()
