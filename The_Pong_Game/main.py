from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.listen()
screen.tracer(0)

paddle1 = Paddle()
paddle1.set_pos(350, 0)


paddle2 = Paddle()
paddle2.set_pos(-350, 0)

ball = Ball()
sc = ScoreBoard()

screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    #Detect collision with left paddle
    if ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect collision with right and left wall
    if ball.xcor() > 380:
        ball.restart()
        sc.l_scores()

    if ball.xcor() < -380:
        ball.restart()
        sc.r_scores()


screen.exitonclick()

