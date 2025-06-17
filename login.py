from tkinter import*

screen=Tk()
screen.geometry("500x300")

screen.config(background="pink")

username=Label(screen, text="Username")
username.place(x=100, y=100)
password=Label(screen, text="Password")
password.place(x=100, y=120)

user_entry=Entry(screen)
user_entry.place(x=150, y=100)
pass_entry=Entry(screen)
pass_entry.place(x=150, y=120)

submit=Button(screen, text="Submit")
submit.place(x=100, y=130)

screen.mainloop()