from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(width=5)
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.setheading(270)
        while self.ycor() > -300:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()