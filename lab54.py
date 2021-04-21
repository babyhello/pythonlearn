import tkinter
from tkinter.font import Font


def display(scale):
    label1.config(text=message % int(scale))


message = "status=%d"
top = tkinter.Tk()
font1 = Font(family="Carlito", size=30)
font2 = Font(family="Source Code Pro Black", size=20)
label1 = tkinter.Label(top, text=message % 0, font=font1)
scale1 = tkinter.Scale(top, label="Volume", font=font2, orient="h", from_=0, to=100, command=display)
label1.pack()
scale1.pack()
top.minsize(600, 200)
top.maxsize(600, 200)
top.mainloop()
