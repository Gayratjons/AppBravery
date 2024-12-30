from turtle import Turtle

X_COR = 350
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, goto_x, goto_y):
        super().__init__()
        self.goto_x = goto_x
        self.goto_y = goto_y
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch to make it paddle-like
        self.penup()
        self.goto(self.goto_x, self.goto_y)  # Use both x and y positions

    def up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
    def down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
