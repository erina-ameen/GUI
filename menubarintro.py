from tkinter import*

screen=Tk()
screen.geometry("400x300")

screen.title("Menu Bar Intro")

menu_bar=Menu(screen)

#Adding file menu
file=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="Open File", command=None)
file.add_separator()
file.add_command(label="Open Folder", command=None)
file.add_separator()
file.add_command(label="New Window", command=None)

#Adding edit menu
edit=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo", command=None)
edit.add_command(label="Redo", command=None)
edit.add_separator()
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)

#Displaying Menu
screen.config(menu=menu_bar)

screen.mainloop()