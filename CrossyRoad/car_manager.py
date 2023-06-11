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
        self.hideturtle()
        self.penup()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)

    def create_car(self):
        random_chance_create_car = random.randint(1, 4)
        if random_chance_create_car == 2:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(100, 500), random.randint(-250, 250))
            self.all_cars.append(new_car)

    def car_reset(self):
        self.goto(300, random.randint(-250, 250))
        self.showturtle()

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
