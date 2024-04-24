from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=0, starty=0)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(player_no=1)
r_paddle = Paddle(player_no=2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(1/60)
    screen.update()
    ball.move()

    if abs(ball.ycor()) > 285:
        ball.bounce_y()

    if (r_paddle.distance(ball) < 50 or l_paddle.distance(ball) < 50) and abs(ball.xcor()) > 335:
        ball.bounce_x()
        ball.accelerate()

    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update()

    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update()

screen.exitonclick()
