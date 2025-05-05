from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_w=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_w)
    timer.config(text="TIMER",fg=GREEN)
    canva.itemconfig(timer_text,text="00:00")
    global reps
    reps*=0
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_f():
    global reps
    if(reps==8 or reps==0):
        reps*=0
        start_timer()
    else:
        reset_timer()
        start_timer()

def start_timer():
    global reps
    reps+=1
    if(reps==8):
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="Break",fg=RED)
    elif(reps%2==0):
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Break",fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if (count <0):
        if(reps<8):
            start_timer()
            if(reps%2==0):
                checkmark.config(text="✔"*(reps//2), bg=YELLOW, fg=GREEN)
        return
    min=count//60
    sec=count%60
    if(sec <10):
        sec=f"0{sec}"
    if(min<10):
        min=f"0{min}"
    canva.itemconfig(timer_text, text=f"{min}:{sec}")
    global timer_w
    timer_w=window.after(1000,count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
canva=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
window.config(padx=100,pady=100,bg=YELLOW)
image=PhotoImage(file="tomato.png")
canva.create_image(100,112,image=image)
timer_text=canva.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canva.grid(row=1,column=1)
timer=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,'normal'))
timer.grid(row=0,column=1)
start=Button(text="Start",fg=GREEN,highlightbackground=YELLOW,command=start_f)
start.grid(row=2,column=0)
reset=Button(text="Reset",fg=GREEN,highlightbackground=YELLOW,command=reset_timer)
reset.grid(row=2,column=2)
checkmark=Label(text="",bg=YELLOW,fg=GREEN)
checkmark.grid(row=3,column=1)
window.mainloop()