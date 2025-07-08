from tkinter import*
import calendar

screen=Tk()
screen.geometry("500x300")

screen.title("Calendar")
screen.config(background="light grey")

def year_submit():
    new_screen=Tk()
    new_screen.geometry("500x600")

    new_screen.title("Calendar Display")
    new_screen.config(background="light pink")
    
    year_entry=int(year.get())
    content=calendar.calendar(year_entry)

    label=Label(new_screen, text=content, font=("Monospace", 11))
    label.grid(row=5, column=1)

    new_screen.mainloop()

title_label=Label(screen, text="Calendar", font=("Comic Sans MS", 25), fg="white", bg="black")
title_label.place(x=200, y=30)
title_label=Label(screen, text="Enter Year", font=("Comic Sans MS", 20), fg="white", bg="black")
title_label.place(x=195, y=90)

year=Entry(screen, font=("Comic Sans MS", 15))
year.place(x=150, y=150)

submit=Button(screen, text="Submit", command=year_submit)
submit.place(x=250, y=200)

screen.mainloop()
