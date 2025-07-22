from tkinter import*

screen=Tk()
screen.geometry("400x300")

screen.config(background="light grey")

title=Label(screen, text="Chocolate and Ice Cream", font="15")
title.pack()

#Top Frame (HORIZONTAL)
top_f=Frame(screen)
top_f.pack()
milk_choc=Button(top_f, text="Milk Chocolate", fg="white", bg="brown")
dark_choc=Button(top_f, text="Dark Chocolate", fg="white", bg="black")
white_choc=Button(top_f, text="White Chocolate", fg="white", bg="orange")

milk_choc.pack(side=LEFT)
dark_choc.pack(side=LEFT)
white_choc.pack(side=LEFT)

#Bottom Frame (VERTICAL)
bottom_f=Frame(screen, bg="light grey")
bottom_f.pack(side=BOTTOM, pady=50)
mint_ice=Button(bottom_f, text="Mint Chocolate Ice", fg="white", bg="green")
strawberry_ice=Button(bottom_f, text="Strawberry Ice", fg="white", bg="pink")
bubblegum_ice=Button(bottom_f, text="Bubblegum Ice", fg="white", bg="blue")

mint_ice.pack(side=BOTTOM, pady=10)
strawberry_ice.pack(side=BOTTOM, pady=10)
bubblegum_ice.pack(side=BOTTOM, pady=10)

screen.mainloop()