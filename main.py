from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_starting_x = screen.window_width() // 2 - 30

r_paddle = Paddle((paddle_starting_x, 0))
l_paddle = Paddle((-paddle_starting_x, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

speed = 0.08

screen.listen()

while True:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    ball.check_for_wall_collision()

    r_distance = ball.distance(r_paddle)
    l_distance = ball.distance(l_paddle)
    distance = 50

    r_paddle_zone = paddle_starting_x - 10
    l_paddle_zone = -paddle_starting_x + 10

    if r_distance < distance and ball.xcor() == r_paddle_zone or l_distance < distance and ball.xcor() == l_paddle_zone:
        ball.invert_x_movement()

    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.add_point_l()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.add_point_r()
