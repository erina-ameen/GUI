from tkinter import *

screen=Tk()
screen.geometry("500x500")

#bg colour
screen.config(background="purple")

def state():
    entry_ans=entrybox.get()
    print(entry_ans)

#label
label=Label(screen, text="This is a Label", font=("Comic Sans MS" , 20), fg="pink", bg="purple")
label.place(x=150, y=100)

#button
button=Button(screen, text="You can click me", command=state)
button.place(x=200, y=160)

#entry box
entrybox=Entry(screen)
entrybox.place(x=170, y=200)


screen.mainloop()