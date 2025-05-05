from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.penup()
        self.refresh()
    def refresh(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)