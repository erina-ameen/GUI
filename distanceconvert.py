from tkinter import*
screen=Tk()

m_entry_label=Label(screen, text="Enter distance in Meters:")
km_output_label=Label(screen, text="Kilometer")
cm_output_label=Label(screen, text="Centimeter ")
mm_output_label=Label(screen, text="Millimeter ")

m_entry=Entry(screen)

def convert():
    m_convert=m_entry.get()

    if m_convert.isdigit():
        m_convert=int(m_convert)
        km_con=m_convert/1000
        cm_con=m_convert*100
        mm_con=m_convert*1000
        km_text.delete("1.0", END)
        km_text.insert(END, km_con)
        cm_text.delete("1.0", END)
        cm_text.insert(END, cm_con)
        mm_text.delete("1.0", END)
        mm_text.insert(END, mm_con)

submit=Button(screen, text="Submit", command=convert)

km_text=Text(screen, height=1, width=20)
cm_text=Text(screen, height=1, width=20)
mm_text=Text(screen, height=1, width=20)

#Gridding
m_entry_label.grid(row=0, column=0)
m_entry.grid(row=0, column=1)
submit.grid(row=0, column=2)

km_output_label.grid(row=1, column=0)
cm_output_label.grid(row=1, column=1)
mm_output_label.grid(row=1, column=2)

km_text.grid(row=2, column=0)
cm_text.grid(row=2, column=1)
mm_text.grid(row=2, column=2)

screen.mainloop()