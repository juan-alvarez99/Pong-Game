from turtle import Turtle


class Court(Turtle):
    """
    Draws the lines in the middle field using the Turtle class
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.pensize(3)
        self.draw_midfield()

    def draw_midfield(self):
        self.goto(x=0, y=250)
        self.setheading(270)
        for y in range(25):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
