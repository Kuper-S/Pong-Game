from turtle import Screen, Turtle
from paddle_maker import Paddle
from turtle import Screen
from ball import Ball
from wall import Walls
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
up_wall = Walls((0, 360))
down_wall = Walls((0, -360))
score = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# to get reed of the first animation ,send paddle to his place
game_on = True
sleep = 0.1
while game_on:
    time.sleep(ball.acceleration)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.ball_reset_position()
        score.l_point()
    if ball.xcor() < -390:
        ball.ball_reset_position()
        score.r_point()

screen.exitonclick()
