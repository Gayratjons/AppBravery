from turtle import Turtle, Screen
import random as rand
timmy = Turtle()
timmy.shape('turtle')
timmy.speed('fastest')
def random_color():
    rgb = ['#']
    hex_chars = ["A", "B", "C", "D", "E", "F","0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for _ in range(6):
        rgb.append(rand.choice(hex_chars))
    return "".join(rgb)
def draw_figure(n):

    '''directions = [30, -30]
    angles = [90, -90]''' 

    for _ in range(0, n, 2):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 2)
        '''timmy.forward(rand.choice(directions))
        timmy.right(rand.choice(angles))'''
draw_figure(360)



screen = Screen()
screen.exitonclick()