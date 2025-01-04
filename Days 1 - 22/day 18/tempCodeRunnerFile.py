def draw_figure(n):
    angle = ((n - 2) * 180) / n
    print(angle)
    for _ in range(n):
        for _ in range(7):
            timmy.forward(10)
            timmy.penup()
            timmy.forward(10)
            timmy.pendown()
        timmy.right(180 - angle)



for i in range(3, 9):
    draw_figure(i)



screen = Screen()
screen.exitonclick()