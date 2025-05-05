from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,loc):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 5)
        self.color('white')
        self.setheading(90)
        self.penup()
        self.goto(loc)
        self.moving_up=False
        self.moving_down=False
        self.game=False
    def moveup(self):
        self.moving_up=True

    def movedown(self):
        self.moving_down=True
    def stop_moveup(self):
        self.moving_up=False
    def stop_movedown(self):
        self.moving_down=False
    def update_position(self):
        if self.moving_up and self.ycor()<240:
            self.sety(self.ycor()+20)
        if self.moving_down and self.ycor()>-240:
            self.sety(self.ycor()-20)
    def pause(self):
        self.game=not self.game