from tkinter import *

def button_clicked():
    # my_label.config(text="Button Got Clicked")
    entered_data = input.get()
    my_label.config(text=entered_data)

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx=100,pady=200)


#Label
my_label = Label(text="I am a label.", font=("Arial",24,"bold"))
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#newbutton
button = Button(text="New Button", command=button_clicked)
# button.pack()
button.grid(column=2,row=0)

#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3,row=2)

# Grid and pack can't be used together

window.mainloop()

# def add(*args):
#     sum=0
#     for n in args:
#         sum+=n
#     return sum

# print(add(2,3,5,7,9))
# print(add(3,6))
# print(add(2,5,7,8))