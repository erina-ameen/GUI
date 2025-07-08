from tkinter import*
from tkinter.ttk import*

screen=Tk()
screen.geometry("500x600")

screen.config(background="pink")

email=Label(screen, text="Email")
email.place(x=50, y=90)
password=Label(screen, text="Password")
password.place(x=50, y=120)
food=Label(screen, text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich or None?")
food.place(x=50, y=180)
bev=Label(screen, text="What drink would you like: Coke, Fanta, Orange Juice or None?")
bev.place(x=50, y=270)
dessert=Label(screen, text="What dessert would you like: Ice Cream, Ice Lolly, Chocolate Cake or None?")
dessert.place(x=50, y=360)

email_entry=Entry(screen)
email_entry.place(x=170, y=90)
pass_entry=Entry(screen, show="*")
pass_entry.place(x=170, y=120)
food_entry=Entry(screen)
food_entry.place(x=50, y=220)
bev_entry=Entry(screen)
bev_entry.place(x=50, y=310)
dessert_entry=Entry(screen)
dessert_entry.place(x=50, y=400)

food_spin = Spinbox(screen, from_=0, to=10)
food_spin.place(x=200, y=220)
bev_spin = Spinbox(screen, from_=0, to=10)
bev_spin.place(x=200, y=310)
dessert_spin = Spinbox(screen, from_=0, to=10)
dessert_spin.place(x=200, y=400)

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
pg.place(x=50, y=500)

submit=Button(screen, text="Submit", command=progress)
submit.place(x=50, y=450)

screen.mainloop()