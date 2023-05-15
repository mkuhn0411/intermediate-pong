from turtle import Turtle

TOP_Y = 270
BOTTOM_Y = -270


class Paddle(Turtle):

    def __init__(self, screen, starting_x):
        super().__init__()
        self.screen = screen
        self.starting_x = starting_x
        self.set_up()

    def up(self):
        new_y = self.ycor() + 20
        new_y < TOP_Y and self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        new_y > BOTTOM_Y and self.goto(self.xcor(), new_y)

    def set_up(self):
        self.penup()
        self.goto(self.starting_x, 0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("deep pink")


