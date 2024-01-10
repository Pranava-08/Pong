from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle, Wall
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=610)
screen.title('Pong')
screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
wall_up = Wall(295)
wall_down = Wall(-295)
score_player1 = Scoreboard()
score_player2 = Scoreboard()

game_onn = True
max_score = int(screen.textinput(title='Winning score', prompt='What do you want the winning score to be? '))
pts_player1 = 0
pts_player2= 0

screen.listen()
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle2.up, 'w')
screen.onkey(paddle2.down, 's')

while game_onn:
    time.sleep(ball.ballspeed)
    score_player1.score(pts_player1, "player 1", 270)
    score_player2.score(pts_player2, "player 2",-290)
    screen.update()
    ball.move()
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce()
    if ball.xcor()>330:
        if ball.distance(paddle1)<50:
            ball.pitch()
        else:
            if ball.xcor()>400:
                ball.refresh()
                ball.pitch()
                pts_player2+=1
                score_player2.score(pts_player2, "player 2",-290)
                if pts_player2 == max_score:
                    game_onn = False
                    score_player1.game_over()
                    score_player1.winner("PLAYER 2")
                    continue
                    
    if ball.xcor()<-330:
        if ball.distance(paddle2)<50:
            ball.pitch()
        else:
            if ball.xcor()<-400:
                ball.refresh()
                ball.pitch()
                pts_player1+=1
                score_player1.score(pts_player1, "player 1", 270)
                if pts_player1 == max_score:
                    game_onn = False
                    score_player2.game_over()
                    score_player2.winner("PLAYER 1")
                    
    
screen.exitonclick()