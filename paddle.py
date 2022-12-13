from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    Defines the characteristics of the paddle of each player. Is an inheritance from the Turtle class
    ====Own Methods:====
    self.up()
    self.down()
    """
    def __init__(self, coordinates):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setpos(coordinates)
        # Shape square, 20x100 pixels
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        """
        Moves the paddle upwards
        """
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        """
        Moves the paddle downwards
        """
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
