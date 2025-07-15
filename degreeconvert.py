from tkinter import*

screen=Tk()
screen.geometry("500x500")

screen.title("Degree Convert")
screen.config(background="pink")

def convert():
    c_temp=c_entry.get()

    if c_temp.isdigit():
        error.place_forget()
        c_temp=int(c_temp)
        f_temp=(c_temp*9/5)+32
        f_label.config(text="Temperature in Farenheit: "+str(f_temp))

    else:
        error.place(x=200, y=340)

cf_label=Label(screen, text="Celsius >>> Farenheit", font=("Comic Sans MS", 15), fg="black")
cf_label.place(x=175, y=60)
entry_label=Label(screen, text="Enter Temperature in Celsius", font=("Comic Sans MS", 15), fg="black")
entry_label.place(x=143, y=110)
validity=Label(screen, text="PLEASE ENTER A VALID INPUT", fg="black")
validity.place(x=200, y=215)

c_entry=Entry(screen, font=("Comic Sans MS", 15))
c_entry.place(x=150, y=170)

f_label=Label(screen, text="Temperature in Farenheit:", font=("Comic Sans MS", 10), fg="black")
f_label.place(x=160, y=300)

error=Label(screen, text="This is an INVALID input.", fg="red")

convert=Button(screen, text="Convert", command=convert)
convert.place(x=250, y=250)

screen.mainloop()