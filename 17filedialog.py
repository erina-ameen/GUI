from tkinter import *
from tkinter.filedialog import *

screen=Tk()
screen.geometry("550x450")
screen.config(background="grey")

#Adding items to listbox
def adding():
    lister.insert(END, entry.get())
    entry.delete(0,END)

#Deleting items to listbox
def deleting():
    chosen_item=lister.curselection()
    lister.delete(chosen_item)

#Saving Items
def saving():
    extension=asksaveasfile(defaultextension=".txt")
    if extension is not None:
        for i in lister.get(0, END):
            print(i.strip(),file=extension)
            lister.delete(0,END)

#Opening Items
def opening():
    extension=askopenfile(title="Open File")
    if extension is not None:
        lister.delete(0,END)
        new_item=extension.readlines()
        for i in new_item:
            lister.insert(END, i.strip())

enter_f=Frame(screen, background="grey")
enter_f.pack(pady=20)
save=Button(enter_f, text="SAVE", width=72, command=saving)
entry=Entry(enter_f, width=85)
add=Button(enter_f, text="ADD", width=72, command=adding)

save.pack(side=BOTTOM, pady=5)
entry.pack(side=BOTTOM, pady=5)
add.pack(side=BOTTOM, pady=5)

side_f=Frame(screen, background="grey")
side_f.pack(pady=20)
opener=Button(side_f, text="OPEN", command=opening)
delete=Button(side_f, text="DELETE", command=deleting)

opener.pack(side=LEFT, padx=100)
delete.pack(side=LEFT, padx=100)

item_f=Frame(screen, background="red")
item_f.pack()
scroll=Scrollbar(item_f, orient="vertical")
scroll.pack(side=RIGHT, fill=Y)
lister=Listbox(item_f, width=72, yscrollcommand=scroll.set, bg="red")
for i in range(20):
    lister.insert(END, "LIST"+str(i))
lister.pack(side=LEFT, padx=10, pady=15)
scroll.config(command=lister.yview)

screen.mainloop()
