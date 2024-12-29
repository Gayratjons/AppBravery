from paddle import Paddle
from ball import CreateBall
from turtle import Screen
from scoreboard import ScoreBoard
import time
# screen = gameScreeen()
r_paddle = Paddle(goto_x=350, goto_y = 0)
l_paddle = Paddle(goto_x=-350, goto_y = 0)
ball = CreateBall()
scoreBoard = ScoreBoard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The PONG")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_on = True
while is_on:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:  # Correct boundary for top and bottom walls
        ball.collision_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.collision_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreBoard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreBoard.r_point()
screen.exitonclick()
