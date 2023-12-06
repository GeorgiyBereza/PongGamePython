from turtle import Turtle, Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

#setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Good Old Pong")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

#creating paddles
left_paddle = Paddle()
left_paddle.setpos(-387,0)
screen.onkeypress(left_paddle.move_up,"w")
screen.onkeypress(left_paddle.move_down,"s")

right_paddle = Paddle()
right_paddle.setpos(380,0)
screen.onkeypress(right_paddle.move_up,"Up")
screen.onkeypress(right_paddle.move_down,"Down")

ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()
    #checking collision with borders
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
    #checking collisions with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 355 or ball.distance(left_paddle) < 50 and ball.xcor() < -365:
        ball.bounce_x()
        ball.time_speed *= 0.7

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_scores()

    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_scores()


screen.exitonclick()
