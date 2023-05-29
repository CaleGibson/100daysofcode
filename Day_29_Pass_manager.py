from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_ent.insert(END, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

        web = web_ent.get()
        email = email_ent.get()
        password = {pass_ent.get()}
        if password == "" or web == "":
            messagebox.showinfo(title="Oops", message="Don't leave shi blank")
        else:
            is_ok = messagebox.askokcancel(title=web, message=f"Is this correct?\n Email: {email}\n Password: {password}\n"
                                                      f" Is this okay to save? ")
            if is_ok:
                with open("pass_list.txt", "a") as file:
                    file.write(f"{web} | {email} | {password} \n")
                    pass_ent.delete(0,END)
                    web_ent.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_lable = Label(text="Website")
web_lable.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_lable = Label(text="Password:")
pass_lable.grid(column=0, row=3)

web_ent = Entry(width=35)
web_ent.grid(column=1, row=1, columnspan=2)
web_ent.focus()
email_ent = Entry(width=35)
email_ent.grid(column=1, row=2, columnspan=2)
email_ent.insert(END, string="cale1gibbyson@gmail.com")
pass_ent = Entry(width=21)
pass_ent.grid(column=1, row=3)


pass_button = Button(text="Generate Password",command=gen)
pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()