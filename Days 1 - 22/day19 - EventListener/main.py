import turtle
timmy = turtle.Turtle()
screen = turtle.Screen()
def move_d():
    timmy.setheading(0)
    timmy.forward(20)
def move_w():
    timmy.setheading(90)
    timmy.forward(20)
def move_a():
    timmy.setheading(180)
    timmy.forward(20)
def move_s():
    timmy.setheading(270)
    timmy.forward(20)

screen.listen()
screen.onkey(fun=move_w, key='w')
screen.onkey(fun=move_a, key='a')
screen.onkey(fun=move_s, key='s')
screen.onkey(fun=move_d, key='d')

screen.exitonclick()



