from turtle import Turtle


class Ball(Turtle):
    """
    Inheritance from the Turtle class.
    ==== Own Attributes: ====
    self.x_move: defines the direction of the ball in the x-axis
    self.y_move: defines the direction of the ball in the y-axis
    self.ball_speed: defines the speed of the ball, the lower this value is, the faster the ball goes.
    ==== Own Methods: =======
    self.move()
    self.bounce_x()
    self.bounce_y()
    self.restart()
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.fillcolor('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """
        Moves the ball following a diagonal trajectory defined by the attributes 'x_move' and 'y_move'
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """
        Changes the direction in the x-axis and speeds up the ball
        """
        self.x_move *= -1
        self.ball_speed *= 0.8

    def bounce_y(self):
        """
        Changes the direction of the ball in the y-axis
        """
        self.y_move *= -1

    def restart(self):
        """
        Moves the ball to the middle field and goes back to the normal speed
        """
        self.goto(x=0, y=0)
        self.x_move *= -1
        self.ball_speed = 0.1
