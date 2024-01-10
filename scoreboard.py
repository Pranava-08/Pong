from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def score(self, score, player, y):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(0,y)
        self.color("white")
        self.write(f"{player}: {score}", align="center", font=("courier", 14, "normal"))
    
    def game_over(self):
        self.goto(0,20)
        self.color("white")
        self.write("Game Over!!!", align="center", font=("courier", 24, "normal"))

    def winner(self, win):
        self.goto(0,-20)
        self.color("white")
        self.write(f"WINNER IS {win}", align="center", font=("courier", 18, "normal"))
