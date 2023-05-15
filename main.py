from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
# screen.tracer(0)


def set_key_listeners(paddle_left, paddle_right):
    screen.listen()
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")
    screen.onkey(paddle_right.up, "Up")
    screen.onkey(paddle_right.down, "Down")


def run():
    game_is_on = True

    paddle_left = Paddle(screen, -390)
    paddle_right = Paddle(screen, 380)
    ball = Ball(paddle_left, paddle_right)
    scoreboard = Scoreboard()

    set_key_listeners(paddle_left, paddle_right)

    while game_is_on:
        time.sleep(ball.move_speed)
        wall_is_hit = ball.move()

        if wall_is_hit:
            game_is_on = False
            scoreboard.update_score(wall_is_hit)
            ball.restart_game(wall_is_hit)
            game_is_on = True


run()

screen.exitonclick()
