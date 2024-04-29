from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        #Remove ball bouncing on itself back into the wall
        if self.y_move > 0:
            self.y_move += 10
            self.move()
            self.y_move = 10
        else:
            self.y_move -= 10
            self.move()
            self.y_move = -10

    def bounce_x(self):
        self.x_move *= -1
        self.velocity *= 0.9

        #Remove ball bouncing on itself back into the paddle
        if self.x_move > 0:
            self.x_move += 10
            self.move()
            self.x_move = 10
        else:
            self.x_move -= 10
            self.move()
            self.x_move = -10

    def point(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.bounce_x()