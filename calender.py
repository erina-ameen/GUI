from tkinter import*
import calendar

screen=Tk()
screen.geometry("500x500")

screen.title("Calender")
screen.config(background="light grey")

title_label=Label(screen, text="Calendar", font=("Comic Sans MS", 25), fg="white", bg="black")
title_label.place(x=200, y=30)
title_label=Label(screen, text="Enter Year", font=("Comic Sans MS", 20), fg="white", bg="black")
title_label.place(x=195, y=90)

year=Entry(screen, font=("Comic Sans MS", 15))
year.place(x=150, y=150)

screen.mainloop()