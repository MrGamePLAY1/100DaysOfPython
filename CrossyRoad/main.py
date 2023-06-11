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
        time.sleep(0.01)
        car.move() # move all cars

        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            # player.reset()


        if player.ycor() > 280:
            player.reset()
            car.car_speed += 0.10
            scoreboard.increase_level()

        # Making sure the player cant go backwards
        if player.ycor() < -280:
            print('out of bounds')
            player.goto(player.xcor(), -280)

        if player.xcor() > 280:
            print('out of bounds')
            player.goto(280, player.ycor())

        if player.xcor() < -280:
            print('out of bounds')
            player.goto(-280, player.ycor())

    screen.update()

screen.exitonclick()
