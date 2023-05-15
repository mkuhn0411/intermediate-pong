from turtle import Turtle

WALL_VERTICAL = 280
WALL_HORIZONTAL = 370
MOVE_SPEED_BASE = 0.05


class Ball(Turtle):

    def __init__(self, paddle_left, paddle_right):
        super().__init__()
        self.set_up()
        self.x_move = 10
        self.y_move = 10
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.move_speed = MOVE_SPEED_BASE

    def set_up(self):
        self.penup()
        self.shape("circle")
        self.color("green")

    def has_hit_vertical_wall(self):
        return self.ycor() > WALL_VERTICAL or self.ycor() < WALL_VERTICAL * -1

    def has_hit_horizontal_wall(self):
        if self.xcor() > WALL_HORIZONTAL or self.xcor() < WALL_HORIZONTAL * -1:
            return self.xcor()

        return False

    def has_hit_paddle(self):
        distance_paddle_left = self.distance(self.paddle_left) < 50 and self.xcor() < -340
        distance_paddle_right = self.distance(self.paddle_right) < 50 and self.xcor() > 340

        return distance_paddle_left or distance_paddle_right

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(self.x_move, self.y_move)

        self.goto(new_x, new_y)

        if self.has_hit_vertical_wall():
            self.bounce_y()
        elif self.has_hit_paddle():
            self.bounce_x()

        wall_hit = self.has_hit_horizontal_wall()
        print(wall_hit)

        if wall_hit:
            return wall_hit

        return False

    def restart_game(self, wall_is_hit):
        self.hideturtle()
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED_BASE
        self.bounce_x()
        self.showturtle()


