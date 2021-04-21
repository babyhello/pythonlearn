import tkinter
from tkinter.font import Font


def func1():
    label1.config(text="pixel5")


def func2():
    label1.config(text="iphone12")


def funcX():
    if sel.get() == 1:
        label1.config(text="pixel5")
    elif sel.get() == 2:
        label1.config(text="iphone12")


top = tkinter.Tk()
sel = tkinter.IntVar()
sel.set(1)
font1 = Font(family="Carlito", size=30)
font2 = Font(family="Source Code Pro Black", size=30)
label1 = tkinter.Label(top, text="something", font=font2)
button1 = tkinter.Radiobutton(top, text="Google", font=font1, value=1, variable=sel, command=funcX)
button2 = tkinter.Radiobutton(top, text="Apple", font=font1, value=2, variable=sel, command=funcX)
label1.pack()
button1.pack()
button2.pack()
top.mainloop()