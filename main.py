"""
Portfolio Repository
Created by: Juan Alvarez
Date: 11.12.2022
#100DaysOfCode #Day22
Github: https://github.com/juan-alvarez99
Linkedin: https://www.linkedin.com/in/juan-alv/
========================================================================================================
This are the rules:
    - It is a two-player game.
    - Player 1 controls the left paddle with the "w" and "s" keys.
    - Player 2 controls the right paddle with the up and down arrow keys.
    - The ball speeds up every time it hits a paddle.
    - The player who fails to hit the ball misses the point.
    - Press "space" to end the game.
Did you like it? You can play as many times as you want!
Enjoy!
========================================================================================================
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from court import Court
import time

PLAYER1_COORDINATES = (-350, 0)
PLAYER2_COORDINATES = (350, 0)

# Screen set up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

court = Court()
player_1 = Paddle(PLAYER1_COORDINATES)
player_2 = Paddle(PLAYER2_COORDINATES)
ball = Ball()
scoreboard = Scoreboard()

# Set control keys
screen.listen()
# Player 1 movement
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")
# Player 2 movement
screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")
# Press space to exit the game
screen.onkey(scoreboard.game_over, "space")

# Start game
while scoreboard.game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()

    # Detect collision with walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect player scoring a point
    if ball.xcor() > 360:
        scoreboard.p1_scored()
        time.sleep(0.5)
        ball.restart()
    elif ball.xcor() < -360:
        scoreboard.p2_scored()
        time.sleep(0.5)
        ball.restart()
    # Detect collision with paddles
    elif ball.xcor() <= -340 and ball.distance(player_1) < 50:
        ball.bounce_x()
    elif ball.xcor() >= 340 and ball.distance(player_2) < 50:
        ball.bounce_x()

    ball.move()

screen.exitonclick()
