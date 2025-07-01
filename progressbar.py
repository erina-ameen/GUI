from tkinter import*
from tkinter.ttk import*

screen=Tk()
screen.geometry("300x100")

#Function for the Progress Bar
def progress():
    import time

    pg["value"]=20
    screen.update_idletasks()
    time.sleep(1)
    pg["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    pg["value"]=60
    screen.update_idletasks()
    time.sleep(1)
    pg["value"]=80
    screen.update_idletasks()
    time.sleep(1)
    pg["value"]=100

pg=Progressbar(screen, orient=HORIZONTAL, length=270, mode='determinate')
pg.place(x=15, y=20)

start=Button(screen, text="Start", command=progress)
start.place(x=110, y=50)

screen.mainloop()