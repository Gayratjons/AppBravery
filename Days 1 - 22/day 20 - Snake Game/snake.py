from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class CreateSnake:
    def __init__(self):
        self.turtles = []
        self.createSnake()

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)
    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def createSnake(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.turtles.append(turtle)

    def moveSnake(self):
        for turtle_num in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)
        # self.turtles[0].left(90)