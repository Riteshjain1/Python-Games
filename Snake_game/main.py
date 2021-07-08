from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
f = Food()
sc = ScoreBoard()
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    #Detect collision with food
    if s.head.distance(f) < 15:
        f.refresh()
        sc.increase_score()
        s.extend()

    #Detect collision with wall
    if s.head.xcor() > 290 or s.head.xcor() < -300 or s.head.ycor() > 290 or s.head.ycor() < -290:
        s.reset_game()
        sc.res()

    #Detect collision from tale
    for segment in s.segments[1:]:
        if s.head.distance(segment) < 10:
            s.reset_game()
            sc.res()

screen.exitonclick()

