from turtle import Turtle

class CreateBall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white") 
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.speed_of_ball = 0.1
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
    def collision_y(self):
        self.move_y *= -1

    def collision_x(self):
        self.move_x *= -1
        self.speed_of_ball *= 0.95
        
    
    def reset_position(self):
        self.goto(0,0)
        self.collision_x()