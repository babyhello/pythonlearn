import tkinter
from tkinter.font import Font

sample = "move to:(%d,%d)" % (0, 0)


def motionLog(ev):
    message.config(text="move to:(%d,%d)" % (ev.x, ev.y))
    #print("move to:(%d,%d)" % (ev.x, ev.y))


top = tkinter.Tk()
font1 = Font(family="Carlito", size=30)
font2 = Font(family="Source Code Pro Black", size=30)
message = tkinter.Message(top, text=sample, font=font1)
message.pack()
top.bind('<Motion>', motionLog)
top.minsize(400, 600)
top.maxsize(400, 600)
top.mainloop()