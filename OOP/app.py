# from turtle import Screen, Turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")    #AliceBlue
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("City Name", ["Tashkent", "Seoul", "London"])
table.add_column("Population", [4.3, 20, 30])
print(table)