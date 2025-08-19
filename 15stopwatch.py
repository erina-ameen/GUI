from tkinter import*
import time
from tkinter import messagebox

screen=Tk()
screen.geometry("300x300")
screen.config(background="purple")

screen.title("Stopwatch")

#Variables
hours=StringVar()
mins=StringVar()
secs=StringVar()

hours.set("00")
mins.set("00")
secs.set("00")

stop_label=Label(screen, text="Stopwatch")
stop_label.place(x=120,y=20)
h=Entry(screen, textvariable=hours, width=3)
h.place(x=100, y=70)
m=Entry(screen, textvariable=mins, width=3)
m.place(x=135, y=70)
s=Entry(screen, textvariable=secs, width=3)
s.place(x=170, y=70)

screen.mainloop()