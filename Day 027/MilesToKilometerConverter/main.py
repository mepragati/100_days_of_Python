from tkinter import *

FONT = ("Arial",18,"normal")

def button_clicked():
    miles = float(input.get())
    my_label_km_value.config(text=f"{miles*1.609}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

#Labels
my_label_miles = Label(text="Miles", font=FONT)
my_label_miles.grid(column=2,row=0)

my_label_is_equal = Label(text="is equal to", font=FONT)
my_label_is_equal.grid(column=0,row=1)

my_label_km_value = Label(text="0", font=FONT)
my_label_km_value.grid(column=1,row=1)

my_label_km = Label(text="Km", font=FONT)
my_label_km.grid(column=2,row=1)

#Entry
input = Entry(width=7)
input.grid(column=1,row=0)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()
