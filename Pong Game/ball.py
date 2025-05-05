from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x=10
        self.y=10
        self.time=0.01
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    def bounce(self):
        self.y*=-1
    def paddle_bounce(self):
        self.x*=-1
        self.time*=0.9
        if(self.heading()==0):
            self.setheading(180)
        else:
            self.setheading(0)
    def reset_position(self):
        self.goto(0,0)
        self.paddle_bounce()
        self.time=0.02;




