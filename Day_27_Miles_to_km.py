from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=100)

my_label2 = Label(text="is equal to", font=("Arial", 18))
my_label2.grid(column=0, row=1)

my_label3 = Label(text=" Miles", font=("Arial", 18))
my_label3.grid(column=2, row=0)

my_label3 = Label(text="KM", font=("Arial", 18))
my_label3.grid(column=2, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)

def MiletoKm():
    km = round(int(input.get()) * 1.61, 3)
    lable4.config(text=km)
lable4 = Label(text= 0)
lable4.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=MiletoKm)
calc_button.grid(column=1, row=2)


window.mainloop()