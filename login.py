from tkinter import*

screen=Tk()
screen.geometry("500x300")

screen.config(background="pink")

#Details
def open_file():
    user_store=user_entry.get()
    pass_store=pass_entry.get()

    #File Handling
    details=open("details.txt", "a")
    details.write(f"Username: {user_store}, Password: {pass_store}\n")

    user_entry.delete(0, END)
    pass_entry.delete(0, END)

username=Label(screen, text="Username")
username.place(x=100, y=100)
password=Label(screen, text="Password")
password.place(x=100, y=130)

user_entry=Entry(screen)
user_entry.place(x=170, y=100)
pass_entry=Entry(screen, show="*")
pass_entry.place(x=170, y=130)

submit=Button(screen, text="Submit", command=open_file)
submit.place(x=100, y=170)

screen.mainloop()from tkinter import*

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
