from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 250:
            y = self.position()
            self.goto(y[0], y[1]+20)

    def down(self):
        if self.ycor() > -250:
            y = self.position()
            self.goto(y[0], y[1]-20)

class Wall(Turtle):
    def __init__(self, y):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.1, stretch_len=41)
        self.goto(0, y)