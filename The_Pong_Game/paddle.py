from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5)
        self.penup()
        self.setheading(90)

    def set_pos(self, x_pos, y_pos):
        self.goto(x_pos, y_pos)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

