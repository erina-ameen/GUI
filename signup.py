from tkinter import*

screen=Tk()
screen.geometry("470x385")

screen.config(background="pink")

#Details
def open_file():
    full_name_store=user_entry.get()
    email_name_store=email_entry.get()
    user_store=user_entry.get()
    pass_store=pass_entry.get()
    confirm_pass_store=confirm_pass_entry.get()

    #File Handling
    details=open("signupdeets.txt", "a")
    details.write(f"Full Name: {full_name_store}, Email: {email_name_store}, Username: {user_store}, Password: {pass_store}, Confirm Password: {confirm_pass_store}\n")

    name_entry.delete(0, END)
    email_entry.delete(0, END)
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    confirm_pass_entry.delete(0, END)


fullname=Label(screen, text="Full Name")
fullname.place(x=100, y=100)
email=Label(screen, text="Email")
email.place(x=100, y=130)
username=Label(screen, text="Username")
username.place(x=100, y=160)
password=Label(screen, text="Password")
password.place(x=100, y=190)
confirm_password=Label(screen, text="Confirm Password")
confirm_password.place(x=100, y=220)

name_entry=Entry(screen)
name_entry.place(x=220, y=100)
email_entry=Entry(screen)
email_entry.place(x=220, y=130)
user_entry=Entry(screen)
user_entry.place(x=220, y=160)
pass_entry=Entry(screen, show="*")
pass_entry.place(x=220, y=190)
confirm_pass_entry=Entry(screen, show="*")
confirm_pass_entry.place(x=220, y=220)

submit=Button(screen, text="Submit", command=open_file)
submit.place(x=100, y=270)
clear=Button(screen, text="Clear")
clear.place(x=160, y=270)

screen.mainloop()