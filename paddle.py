from turtle import Turtle

POSITION_1 = (-350, 0)
POSITION_2 = (350, 0)


class Paddle(Turtle):

    def __init__(self, player_no: int):
        super().__init__()
        self.shape("square")
        self.set_paddle(player_no)

    def set_paddle(self, player_no):
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        if player_no == 1:
            self.setposition(POSITION_1)
        elif player_no == 2:
            self.setposition(POSITION_2)

    def move_up(self):
        new_y = (self.ycor() + 20)
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = (self.ycor() - 20)
        self.goto(x=self.xcor(), y=new_y)
