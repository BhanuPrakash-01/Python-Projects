from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
LOC1 = (-380, 0)
LOC2= (380, 0)
sc=Screen()
sc.tracer(0)
sc.screensize(800,600)
sc.bgcolor('black')
sc.title("Pong Game")
l_paddle=Paddle(LOC1)
r_paddle=Paddle(LOC2)

sc.listen()
sc.onkeypress(l_paddle.moveup, "s")
sc.onkeyrelease(l_paddle.stop_moveup, "s")
sc.onkeypress(l_paddle.movedown, "x")
sc.onkeyrelease(l_paddle.stop_movedown, "x")
sc.onkeypress(r_paddle.moveup, 'Up')
sc.onkeyrelease(r_paddle.stop_moveup, 'Up')
sc.onkeypress(r_paddle.movedown, 'Down')
sc.onkeyrelease(r_paddle.stop_movedown, 'Down')
sc.onkey(l_paddle.pause,'space')

score=Score()

t=Turtle()
t.width(5)
t.color('white')
t.hideturtle()
t.penup()
t.goto(0,300)
for i in range(0,600,10):
    if(i%10==0 and i%20==0):
        t.penup()
    else:
        t.pendown()
    t.goto(0,300-i)
t.penup()
t.goto(400,300)
t.pendown()
t.goto(400,-300)
t.goto(-400,-300)
t.goto(-400,300)
t.goto(400,300)
t.width(0)
sc.update()

b=Ball()
x=0
while(True):
    b.hideturtle()
    while(l_paddle.game):
        b.move()
        b.showturtle()
        r_paddle.update_position()
        l_paddle.update_position()
        time.sleep(b.time)
        if(b.ycor()<-280 or b.ycor()>280):
            b.bounce()
        if((b.xcor()>350 and b.distance(r_paddle)<53 and b.heading()==0)
                or ((b.xcor()<-350) and b.distance(l_paddle)<53) and b.heading()==180):
           b.paddle_bounce()
        if(b.xcor()>390):
            score.l+=1
            b.reset_position()
        elif(b.xcor()<-390):
            score.r+=1
            b.reset_position()
        score.update()
        if(score.l>=10 or score.r>=10):
            b.hideturtle()
            score.winner()
            l_paddle.game=False
        sc.update()
    while not l_paddle.game:
        sc.update()
        time.sleep(0.1)
