from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


sc=Screen()
sc.title("SNAKE GAME")
sc.screensize(600,600)
sc.bgcolor('black')
sc.tracer(0)
snake=Snake()
pa=True
sc.listen()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")
sc.onkey(snake.pause,'space')


food=Food()
score=Score()
def game_on():
    while True:
        while snake.game :
            sc.update()
            time.sleep(0.1)
            snake.move()
            if snake.head.distance(food)<=15 :
                food.refresh()
                score.update()
                snake.extend()
            if snake.head.xcor()>340 or snake.head.xcor()<-340 or snake.head.ycor()>340 or snake.head.ycor()<-340 :
                snake.reset()
                score.reset_game()
            for j in range(1,len(snake.t)):
                if j>=len(snake.t):
                    pass
                else:
                    if snake.head.distance(snake.t[j])<10 :
                        snake.reset()
                        score.reset_game()
        while not snake.game:
            sc.update()
            time.sleep(0.1)

game_on()
sc.mainloop()