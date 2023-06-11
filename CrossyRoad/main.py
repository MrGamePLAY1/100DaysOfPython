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
car_manager = CarManager()

# Controls
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()  # create new car
    car_manager.move()  # move all cars

    # Detect collision with car
    for car in car_manager.all_cars:
        car.distance(player)
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # --------------------------------------------------------------------
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
