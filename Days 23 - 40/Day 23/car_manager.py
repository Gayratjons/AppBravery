from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS =[(300, 300),
 (300, 260),
 (300, 220),
 (300, 180),
 (300, 140),
 (300, 100),
 (300, 60),
 (300, 20),
 (300, -20),
 (300, -60),
 (300, -100),
 (300, -140),
 (300, -180),
 (300, -220),
 (300, -260)]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.create_car()

    def create_car(self):
        car = Turtle(shape = "square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(random.choice(POSITIONS))
        self.cars.append(car)