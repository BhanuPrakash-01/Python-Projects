from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l=0
        self.r=0
    def update(self):
        self.clear()
        self.goto(-200,310)
        self.write(f'score : {self.l}',True,'left',font=('Courier', 20, 'bold'))
        self.goto(200,310)
        self.write(f'score : {self.r}', True, 'right',font=('Courier', 20, 'bold'))
    def winner(self):
        self.goto(-200,0)
        if(self.l==10):
            self.write(f'Winner : left', True, 'left', font=('Courier', 50, 'bold'))
        else:
            self.write(f'Winner : right', True, 'left', font=('Courier', 50, 'bold'))

