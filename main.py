import time
from turtle import  Turtle,Screen

from Ball import Ball
from Score import Score
from paddle import Paddle

screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((720, 0))
l_paddle=Paddle((-720, 0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

is_game_on=True
while is_game_on:
    time.sleep(0.018)
    screen.update()
    ball.move()

    if ball.ycor()>380 or ball.ycor()<-380:
        ball.bouncey()

    if (r_paddle.distance(ball)<50 and ball.xcor()>690) or (l_paddle.distance(ball)<50 and ball.xcor()> -700) :
        ball.bouncex()

    if ball.xcor()>740:
        ball.resetPosition()
        score.updateRight()
    if ball.xcor() < -740:
        ball.resetPosition()
        score.updateLeft()


screen.exitonclick()