from  turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s=-1
        with open('data.txt') as file:
            self.high_score=int(file.read())
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update()
        self.goto(350,350)
        self.write('Press "Space" to play or pause',False,'right',font=('Courier', 20, 'bold'))

    def update(self):
        self.s+=1
        self.goto(0,290)
        self.clear()
        self.write(f"Score : {self.s}\t\t\tHigh Score : {self.high_score}",True,'center',font=('Courier', 20, 'bold'))
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", True, 'center', font=('Courier', 20, 'bold'))
    def reset_game(self):
        if self.s>self.high_score:
            self.high_score=self.s
            with open('data.txt','w') as file:
                file.write(str(self.s))
        self.s=-1
        self.update()