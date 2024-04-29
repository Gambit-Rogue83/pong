from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
# import random
import time

screen = Screen()
screen.setup(width=1100, height=825)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle((500, 0))
player2 = Paddle((-505, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")


game_over = False

while not game_over:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    #Strike wall
    if ball.ycor() > 390 or ball.ycor() < -375:
        ball.bounce_y()

    #Strike paddle
    if ball.distance(player1) < 40 and ball.xcor() > 475 or ball.distance(player2) < 40 and ball.xcor() < -475:
        ball.bounce_x()

    #Score point
    if ball.xcor() > 520:
        ball.point()
        score.l_score()

    if ball.xcor() < -525:
        ball.point()
        score.r_score()





screen.exitonclick()