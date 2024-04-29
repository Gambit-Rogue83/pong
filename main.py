from turtle import Turtle, Screen
from paddle import Paddle
import random
import time

screen = Screen()
screen.setup(width=1100, height=825)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle((500, 0))
player2 = Paddle((-505, 0))

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")


game_over = False

while not game_over:
    screen.update()








screen.exitonclick()