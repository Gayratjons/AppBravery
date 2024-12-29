from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=500, width=600)
user_bet = screen.textinput(title="Make you bets", prompt="Which turtle will win the race ? Enter a color: ")
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
def createTurtle(new_turtle):
    global colors
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    return new_turtle
def moveTurtle(turtle,y_axis):
    turtle.penup()
    turtle.goto(x=-270, y=y_axis)
y = -100
all_turtles = []
is_race_on = False

for i in colors:
    turtle = createTurtle(i)
    moveTurtle(turtle, y)
    y += 40
    all_turtles.append(turtle)

if user_bet and user_bet in colors:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won ! The {winning_color} turtle won)))")
            else:
                print(f"You lost! The {winning_color} turtle won(((")
        rand_num = random.randint(0,10)
        turtle.forward(rand_num)

screen.exitonclick()