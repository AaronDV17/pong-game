from turtle import Turtle

BALL_SPEED = 3
ACC_VALUE = 1.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.delta_y = BALL_SPEED
        self.delta_x = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.delta_y *= -1

    def bounce_x(self):
        self.delta_x *= -1

    def reset_position(self):
        self.home()
        self.delta_x = BALL_SPEED if self.delta_x > 0 else -BALL_SPEED
        self.bounce_x()

    def accelerate(self):
        self.delta_x *= ACC_VALUE
