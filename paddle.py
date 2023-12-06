from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.move_speed = 15

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+self.move_speed)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-self.move_speed)
