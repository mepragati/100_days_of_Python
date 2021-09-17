from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5,8)  
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers
    random.shuffle(password_list)
    
    password = "".join(password_list)
    input_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entered = input_website.get()
    email_entered = input_email.get()
    password_entered = input_password.get()

    if len(website_entered) == 0 or len(password_entered) == 0:
        messagebox.showinfo(title="Oops", message = "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entered , message = f"These are the details entered: \n Email: {email_entered}\n Password: {password_entered} \n Is it ok to save?")

        if is_ok:
            with open("Day 029\password-manager\data.txt", "a") as file:
                file.write(f"{website_entered} | {email_entered} | {password_entered}\n")
                input_password.delete(0,END)
                input_website.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="Day 029\\password-manager\\logo.png")
canvas.create_image(100,100,image=my_pass_img)
canvas.grid(column=1,row=0)

#Labels
label_website = Label(text="Website:")
label_website.grid(column=0,row=1)
label_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(column=0,row=2)

label_password = Label(text="Password:")
label_password.grid(column=0,row=3)

#Entry
input_website = Entry(width=35)
input_website.grid(column=1,row=1,columnspan=2)


input_email = Entry(width=35)
input_email.grid(column=1,row=2,columnspan=2)
input_email.insert(0,"pragati@gmail.com")


input_password = Entry(width=21)
input_password.grid(column=1,row=3)


#Button
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2,row=3)

button_add = Button(text="Add",width=36,command=save)
button_add.grid(column=1,row=4,columnspan=2)


window.mainloop()