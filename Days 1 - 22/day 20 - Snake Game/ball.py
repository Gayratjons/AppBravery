from turtle import Turtle
import random
class Ball:
    def __init__(self):
        self.ball = Turtle(shape="circle")
    def rand_num(self):
        return random.randint(-250, 250)
    def generate_ball(self):
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(self.rand_num(), self.rand_num())