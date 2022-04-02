from turtle import Turtle, Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball
import random
import time


screen = Screen()
screen.setup(height=400, width=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

"""TODO 1:Creating paddle"""

r_paddle = Paddle((270, 0))
l_paddle = Paddle((-270, 0))
#ball
ball = Ball()
scoreboard = Scoreboard()
#move
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 180 or ball.ycor() < -180:
        ball.y_bounce()


    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 250 or ball.distance(l_paddle) < 50 and ball.xcor() < -250:
        ball.x_bounce()

    # detect R paddle misses
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()
