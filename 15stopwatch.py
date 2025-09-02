from tkinter import*
import time
from tkinter import messagebox

screen=Tk()
screen.geometry("300x300")
screen.config(background="purple")

screen.title("Stopwatch")

#Function for timer
def timer():
    total_s=int(hours.get())*3600+int(mins.get())*60+int(secs.get())
    while total_s>=0:
        tm, ts=divmod(total_s,60)   #divmod combines division and modulus
        th=00
        if tm>60:
            th, tm=divmod(tm, 60)
        #Putting the variables on the entry box
        hours.set("{00:2d}".format(th))
        mins.set("{00:2d}".format(tm))
        secs.set("{00:2d}".format(ts))
        screen.update()
        time.sleep(1)
        if total_s==0:
            messagebox.showinfo("Time's Up", "Time's Up")
        total_s-=1

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

submit_time=Button(screen, text="Set Time Countdown", command=timer)
submit_time.place(x=90, y=130)

screen.mainloop()
