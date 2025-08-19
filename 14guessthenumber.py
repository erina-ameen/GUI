from tkinter import*
import random

screen=Tk()
screen.geometry("350x350")

screen.config(background="pink")

num=random.randint(0,100)
attempts=0

def checking():
    global attempts
    guess=entry.get()
    guess=int(guess)
    attempts+=1
    if num==guess:
        win_label.config(text=f"Correct! It took you {attempts} tries.", fg="white", bg="green")
        win_label.place(x=70, y=200)
    elif num<guess:
        win_label.config(text="Too HIGH", fg="white", bg="red")
        win_label.place(x=70, y=200)
    else:
        win_label.config(text="Too LOW", fg="white", bg="red")
        win_label.place(x=70, y=200)    

guess_title=Label(screen, text="Guess the Number")
guess_title.place(x=70, y=30)
range_label=Label(screen, text="Pick a number from 1-100")
range_label.place(x=70, y=65)
entry=Entry(screen)
entry.place(x=70, y=90)
submit=Button(screen, text="Submit Answer", command=checking)
submit.place(x=70, y=120)
reset=Button(screen, text="Reset Game")
reset.place(x=70, y=155)
win_label=Label(screen)
win_label.place_forget()

screen.mainloop()
