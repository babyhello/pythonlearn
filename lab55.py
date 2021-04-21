import tkinter
from tkinter.font import Font


def display(ev):
    label1.config(text="your input is:%s" % entry1.get())


top = tkinter.Tk()
font1 = Font(family="Carlito", size=30)
font2 = Font(family="Source Code Pro Black", size=30)
label1 = tkinter.Label(top, text="Input something", font=font1)
entry1 = tkinter.Entry(top, text="", font=font2)
button1 = tkinter.Button(top, text="submit", font=font2)
label1.pack()
entry1.pack()
button1.pack()
entry1.bind("<Return>", display)
button1.bind("<Button-1>", display)
top.mainloop()