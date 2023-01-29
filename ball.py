from turtle import Turtle

bound = 280


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_value = 10
        self.y_value = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_value
        new_y = self.ycor() + self.y_value
        self.goto(new_x, new_y)

    def check_for_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_value *= -1
            self.speed *= 0.95

    def invert_x_movement(self):
        self.x_value *= -1
        self.speed *= 0.95

    def reset_ball(self):
        self.home()
        self.speed = 0.1
        self.invert_x_movement()
