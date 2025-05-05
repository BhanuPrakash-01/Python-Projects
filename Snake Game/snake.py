from turtle import Turtle

POS = [(0, 0), (-20, 0), (-40, 0)]
UP,DOWN,LEFT,RIGHT=90,270,180,0
DISTANCE=20
class Snake:
    def __init__(self):
        b=Turtle()
        b.color('white')
        b.penup()
        b.goto(350,350)
        b.pendown()
        b.goto(350, -350)
        b.goto(-350,-350)
        b.goto(-350, 350)
        b.goto(350, 350)
        b.hideturtle()
        self.game=False

        self.t=[]
        self.create()
        self.head=self.t[0]


    def create(self):
        for i in POS:
            self.increase(i)
    def increase(self,positon):
        t1 = Turtle(shape='circle')
        t1.color('white')
        t1.penup()
        t1.goto(positon)
        self.t.append(t1)
    def extend(self):
        self.increase(self.t[-1].pos())

    def move(self):
        if not self.t:
            return
        for i in range(len(self.t) - 1, 0, -1):
            cord = self.t[i - 1].pos()
            self.t[i].goto(cord[0], cord[1])
        self.head.forward(DISTANCE)

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
    def pause(self):
            self.game=not self.game
    def reset(self):
        for i in self.t:
            i.hideturtle()
        self.t.clear()
        self.create()
        self.head=self.t[0]
        self.game=False

