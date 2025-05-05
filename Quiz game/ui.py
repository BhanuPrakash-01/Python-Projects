THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizzInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizz")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.label=Label(text=f"Score : 0",font=('Arial',15,'normal'),bg=THEME_COLOR)
        self.label.grid(row=0,column=1,padx=10,pady=10)

        self.canva=Canvas(width=300,height=250,bg='white')
        self.text=self.canva.create_text(150,125,width=280,text="Text",fill=THEME_COLOR,font=('Arial',20,'italic'))
        self.canva.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

        right_image=PhotoImage(file='./images/true.png')
        self.right_button=Button(image=right_image, command=self.right)
        self.right_button.grid(row=2,column=0,padx=30,pady=30)

        left_image = PhotoImage(file='./images/false.png')
        self.left = Button(image=left_image,command=self.wrong)
        self.left.grid(row=2, column=1,padx=10,pady=10)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canva.config(bg='white')
        self.label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canva.itemconfig(self.text,text=q_text)
        else:
            self.canva.itemconfig(self.text, text=f"You've completed the quiz\n"
                                                  f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state='disabled')
            self.left.config(state='disabled')
    def right(self):
        self.feedback(self.quiz.check_answer(True))
    def wrong(self):
       self.feedback(self.quiz.check_answer(False))
    def feedback(self,answer):
        if(answer):
            self.canva.config(bg="#B1DDC6")
        else:
            self.canva.config(bg='#f54242')
        self.window.after(1000, self.get_next_question)


