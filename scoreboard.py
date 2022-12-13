from turtle import Turtle

STYLE = ('Courier', 50, 'bold')


class Scoreboard(Turtle):
    """
    Inheritance from the class Turtle. Tracks the score of each player
    ==== Own Attributes: ====
    self.p1_score: player 1's score
    self.p2_score: player 2's score
    self.game_is_on: states whether the game is over
    ==== Own Methods: =======
    self.update()
    self.p1_scored()
    self.p2_scored()
    self.game_over()
    """
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.game_is_on = True
        self.pencolor('white')
        self.update()

    def update(self):
        """
        Shows the score of each player in the screen.
        """
        self.clear()
        self.goto(x=-50, y=220)
        self.write(arg=f"{self.p1_score}", align='center', font=STYLE)
        self.goto(x=50, y=220)
        self.write(arg=f"{self.p2_score}", align='center', font=STYLE)

    def p1_scored(self):
        """
        Increases the first player's score by 1
        """
        self.p1_score += 1
        self.update()

    def p2_scored(self):
        """
        Increases the second player's score by 1
        """
        self.p2_score += 1
        self.update()

    def game_over(self):
        """
        Turn off the condition to continue the game "game_is_on"
        """
        self.game_is_on = False
