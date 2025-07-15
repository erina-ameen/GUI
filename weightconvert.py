from tkinter import*
screen=Tk()

kg_entry_label=Label(screen, text="Enter weight in kg:")
g_output_label=Label(screen, text="Grams")
pounds_output_label=Label(screen, text="Pounds")
ounces_output_label=Label(screen, text="Ounces")

kg_entry=Entry(screen)

def convert():
    kg_convert=kg_entry.get()

    if kg_convert.isdigit():
        kg_convert=int(kg_convert)
        g_con=kg_convert*1000
        pounds_con=kg_convert*2.2
        ounces_con=kg_convert*35.274
        g_text.delete("1.0", END)
        g_text.insert(END, g_con)
        pounds_text.delete("1.0", END)
        pounds_text.insert(END, pounds_con)
        ounces_text.delete("1.0", END)
        ounces_text.insert(END, ounces_con)

submit=Button(screen, text="Submit", command=convert)

g_text=Text(screen, height=1, width=20)
pounds_text=Text(screen, height=1, width=20)
ounces_text=Text(screen, height=1, width=20)

#Gridding
kg_entry_label.grid(row=0, column=0)
kg_entry.grid(row=0, column=1)
submit.grid(row=0, column=2)

g_output_label.grid(row=1, column=0)
pounds_output_label.grid(row=1, column=1)
ounces_output_label.grid(row=1, column=2)

g_text.grid(row=2, column=0)
pounds_text.grid(row=2, column=1)
ounces_text.grid(row=2, column=2)

screen.mainloop()
