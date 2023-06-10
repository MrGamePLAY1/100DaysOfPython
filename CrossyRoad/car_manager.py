from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = +5
MOVE_INCREMENT = +10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(295, random.randint(-250, 250))
        self.all_cars.append(self)
        self.showturtle()

    def move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())

