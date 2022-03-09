import tkinter

screen = tkinter.Tk()
screen.title("Mile to KM converter")
text = tkinter.Label(height=5, width=15)
# text.focus()
text["text"] = "Enter distance:"
text.grid(column=0, row=0)
user_input = tkinter.Entry(width=10)
user_input.grid(column=0, row=1)
text1 = tkinter.Label(height=5, width=10)
text1["text"] = "Mile"
text1.grid(column=1, row=1)
label = tkinter.Label(text="")
label.grid(column=0, row=2)


def calculate():
    label["text"] = "is equal to " + str((int(user_input.get()))*1.609)+"  KM"


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=0, row=3)
screen.mainloop()
