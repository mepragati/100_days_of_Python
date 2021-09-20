from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

#-------------------Adding Functionalities-------------------#

data_dict = pandas.read_csv("Day 031\\data\\french_words.csv").to_dict(orient="records")
current_card = {}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title_card,text = "French",fill="black")
    canvas.itemconfig(word_card,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image,image=my_card_img_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image,image=my_card_img_back)
    canvas.itemconfig(title_card,text = "English",fill="white")
    canvas.itemconfig(word_card,text=current_card["English"],fill="white")

def is_known():
    data_dict.remove(current_card)
    data=pandas.DataFrame(data_dict)
    data.to_csv("Day 031\data\words_to_learn.csv")
    next_card()


#--------------------------UI Code---------------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526 )
my_card_img_front = PhotoImage(file="Day 031\images\card_front.png")
my_card_img_back = PhotoImage(file="Day 031\images\card_back.png")
canvas_image = canvas.create_image(400,263,image=my_card_img_front)
title_card=canvas.create_text(400,150,text="Title",font=(FONT_NAME,40,"italic"))
word_card=canvas.create_text(400,263,text="word",font=(FONT_NAME,60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)


#Button
my_image_right = PhotoImage(file="Day 031\\images\\right.png")
button = Button(image=my_image_right, highlightthickness=0,command=is_known)
button.grid(column=1,row=1)

my_image_wrong = PhotoImage(file="Day 031\\images\\wrong.png")
button = Button(image=my_image_wrong, highlightthickness=0,command=next_card)
button.grid(column=0,row=1)

next_card()

window.mainloop()

 