from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BACKGROUND = "#FFDEDE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    title_label.config(text = "Timer")
    checked_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60      #3 ##for checking
    short_break_sec = WORK_MIN*60   #2 ##for checking
    long_break_sec= LONG_BREAK_MIN*60   #5 ##for checking 

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_minute = math.floor(count/60)
    count_seconds = count%60

    if count_seconds < 10:
        count_seconds =f"0{count_seconds}"

    if count_minute < 10:
        count_minute =f"0{count_minute}"

    canvas.itemconfig(timer_text,text = f"{count_minute}:{count_seconds}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks +="✔"
        checked_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="Day 028\\pomodoro\\tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#Labels
title_label = Label(text="Timer",font=(FONT_NAME,28,"bold"),fg=GREEN,bg=YELLOW)
title_label.grid(column=1,row=0)

#Button
button_start = Button(text="Start",highlightthickness=0,command=start_timer)
button_start.grid(column=0,row=2)

button_reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
button_reset.grid(column=2,row=2)

#Checkmark
checked_marks = Label(fg=GREEN,bg=YELLOW)
checked_marks.grid(column=1,row=3)

window.mainloop()