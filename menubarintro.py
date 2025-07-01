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

#Adding selection menu
select=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Selection", menu=select)
select.add_command(label="Select All", command=None)
select.add_command(label="Expand Selection", command=None)
select.add_command(label="Shrink Selection", command=None)
select.add_separator()
select.add_command(label="Copy Line Up", command=None)
select.add_command(label="Copy Line Down", command=None)
select.add_command(label="Move Line Up", command=None)
select.add_command(label="Move Line Down", command=None)
select.add_command(label="Duplicate Selection", command=None)

#Adding view menu
view=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view)
view.add_command(label="Command Palette", command=None)
view.add_command(label="Open View", command=None)
view.add_separator()
view.add_command(label="Zoom In", command=None)
view.add_command(label="Zoom Out", command=None)

#Adding go menu
go=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Go", menu=go)
go.add_command(label="Back", command=None)
go.add_command(label="Forward", command=None)
go.add_command(label="Last Edit Selection", command=None)
go.add_separator()
go.add_command(label="Switch Editor", command=None)
go.add_command(label="Switch Group", command=None)

#Adding run menu
run=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Run", menu=view)
run.add_command(label="Start Debugguing", command=None)
run.add_command(label="Run without Debugging", command=None)
run.add_command(label="Stop without Debugging", command=None)
run.add_command(label="Restart Debugging", command=None)
run.add_separator()
run.add_command(label="Open Configurations", command=None)
run.add_command(label="Add Configuration", command=None)

#Displaying Menu
screen.config(menu=menu_bar)

screen.mainloop()
