from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    ball.speed("slow")
    time.sleep(ball.ball_speed)

    #detecting collision with the ball
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.ball_bounce_y()

    #detecting collision with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.ball_bounce_x()

    #detecting right paddle miss
    if ball.xcor()>380:
        ball.reset_ball()
        score.increase_left()

    #detecting left paddle miss
    if ball.xcor()<-380:
        ball.reset_ball()
        score.increase_right()
        

screen.exitonclick()