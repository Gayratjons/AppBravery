import turtle
import random
import colorgram
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
colors = colorgram.extract('C:\\Python\\AppBravery\\AppBravery-2\\day 18\\img.jpg', 6)
i = 0
for _ in range(len(colors)):
    colors[i] = tuple(colors[i].rgb)
    i+=1
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
for _ in range(10):
    timmy.dot(20,random.choice(colors))
    timmy.forward(50)
var2 = 180
for i in range(1, 9):
    timmy.setheading(90)
    timmy.forward(50)
    timmy.dot(20, random.choice(colors))
    timmy.setheading(var2)
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    if i % 2 != 0:
        var2 = 0
    else:
        var2 = 180


screen = turtle.Screen()
screen.exitonclick()
