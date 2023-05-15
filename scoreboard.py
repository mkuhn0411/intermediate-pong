from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("deep pink")
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self, game_over = False):
        if game_over:
            self.goto(0, 0)
            self.write("Game Over! Sucks to suck", align=ALIGNMENT, font=FONT)
        else:
            self.clear()
            self.write(f"Left Player: {self.left_score} | Right Player: {self.right_score}", align=ALIGNMENT, font=FONT)

    def update_score(self, xcor):
        if xcor > 0:
            self.left_score += 1
        else:
            self.right_score += 1

        self.write_score()
