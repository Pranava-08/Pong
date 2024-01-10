from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.x_step = 10
        self.y_step = 10
        self.ballspeed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_step, self.ycor()+self.y_step)
        
    def bounce(self):
        self.y_step*= -1
    def pitch(self):
        self.x_step*= -1
        self.ballspeed*= 0.9
    
    def refresh(self):
        self.goto(0,0)
        self.ballspeed = 0.1

