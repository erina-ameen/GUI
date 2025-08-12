from tkinter import*
import random

screen=Tk()
screen.geometry("350x350")

screen.config(background="pink")

guess_title=Label(screen, text="Guess the Number")
guess_title.place(x=70, y=30)
range_label=Label(screen, text="Pick a number from 1-100")
range_label.place(x=70, y=65)
entry=Entry(screen)
entry.place(x=70, y=90)
submit=Button(screen, text="Submit Answer")
submit.place(x=70, y=115)
reset=Button(screen, text="Reset Game")
reset.place(x=70, y=150)

screen.mainloop()