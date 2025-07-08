from tkinter import*
screen=Tk()

kg_entry_label=Label(screen, text="Enter weight in kg:")
g_output_label=Label(screen, text="Grams")
pounds_output_label=Label(screen, text="Pounds")
ounces_output_label=Label(screen, text="Ounces")

kg_entry=Entry(screen)

submit=Button(screen, text="Submit")

g_text=Text(screen, height=1, width=20)
pounds_text=Text(screen, height=1, width=20)
ounces_text=Text(screen, height=1, width=20)

#Gridding
