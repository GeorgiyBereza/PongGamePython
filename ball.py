from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.move_speed = 5
        self.time_speed = 0.03
        self.x_speed = self.move_speed
        self.y_speed = self.move_speed

    def move(self):
        self.goto(self.xcor()+self.x_speed,self.ycor()+self.y_speed)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.time_speed = 0.03
        self.bounce_x()