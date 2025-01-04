import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.createCar()
    car.move_cars()
    
    if player.is_on_finish_line():
        player.go_to_start()

    for car in car.cars:
        if car.distance(player) < 20:
            game_is_on = False
