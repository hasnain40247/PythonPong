from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.goto(position)
    def go_up(self):
         new_y=self.ycor()+38
         self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 38
        self.goto(self.xcor(), new_y)