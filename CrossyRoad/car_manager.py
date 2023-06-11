from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = +5
MOVE_INCREMENT = +10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.create_car()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)

    def create_car(self):
        self.setheading(180) # car heading
        self.car_speed = STARTING_MOVE_DISTANCE
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(100, 500),  random.randint(-230, 250))
        self.showturtle()

    def car_reset(self):
        self.goto(random.randint(300, 400),  random.randint(-250, 250))
        self.showturtle()


    def move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())




