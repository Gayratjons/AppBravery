from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [
    (300, 250),
    (300, 210),
    (300, 170),
    (300, 130),
    (300, 90),
    (300, 50),
    (300, 10),
    (300, -30),
    (300, -70),
    (300, -110),
    (300, -150),
    (300, -190),
    (300, -230),
    (300, -250)
]



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_number = random.randint(1,6)
        if random_number == 1:    
            car = Turtle(shape = "square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(random.choice(POSITIONS))
            self.cars.append(car)
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT