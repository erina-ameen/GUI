from tkinter import *
from tkinter.ttk import *
from time import strftime

screen=Tk()
screen.title("Digital Clock")

def timing():
    string=strftime('%H:%M:%S %p')
    clock.config(text=string)
    clock.after(1000, timing)

clock=Label(screen, text="", font=("Comic Sans MS", 60), background="pink")
clock.pack()

timing()

screen.mainloop()