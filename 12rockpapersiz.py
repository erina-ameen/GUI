from tkinter import*
import random

screen=Tk()
screen.geometry("700x350")

screen.config(background="pink")

you_score=0
comp_score=0
options=[('rock',0,),('paper',1),('scissors',2)]

#Computer WIN Function
def comp_win():
    global comp_score, you_score
    comp_score+=1
    winner.config(text="Computer wins!")
    comp_score_l.config(text="Computer Scored: "+str(comp_score))
    you_score_l.config(text="You Scored: "+str(you_score))

#Player(you) WIN Function
def you_win():
    global comp_score, you_score
    you_score+=1
    winner.config(text="You win!")
    comp_score_l.config(text="Computer Scored: "+str(comp_score))
    you_score_l.config(text="You Scored: "+str(you_score))

    if comp_score==5:
        winner.config(text="Computer wins Game!")
        resetting()
    if you_score==5:
        winner.config(text="Player wins Game!")
        resetting()

#TIE Function
def tied():
    global comp_score, you_score
    winner.config(text="IT'S A TIE!")
    comp_score_l.config(text="Computer Scored: "+str(comp_score))
    you_score_l.config(text="You Scored: "+str(you_score))

#Computer SELECTION
def comp_select_return():
    return random.choice(options)

def you_select(opt):
    global you_score, comp_score
    comp_select=comp_select_return()
    you_select_l.config(text="You Selected: "+opt[0])
    comp_select_l.config(text="Computer Selected: "+comp_select[0])
    print(opt)
    print(comp_select)

    if comp_select==opt:
        tied()

    #Player Chooses Rock
    if opt[1]==0:
        if comp_select[1]==1:
            comp_win()
        elif comp_select[1]==2:
            you_win()
    
    #Player Chooses Paper
    if opt[1]==1:
        if comp_select[1]==2:
            comp_win()
        elif comp_select[1]==0:
            you_win()

    #Player Chooses Scissors
    if opt[1]==2:
        if comp_select[1]==1:
            you_win()
        elif comp_select[1]==0:
            comp_win()


def resetting():
    global you_select_l, you_score_l, comp_select_l, comp_score_l, comp_score, you_score
    you_select_l.config(text="You Selected: ")
    you_score_l.config(text="You Scored: ")
    comp_select_l.config(text="Computer Selected: ")
    comp_score_l.config(text="Computer Scored: ")
    comp_score=0
    you_score=0

rps_label=Label(screen, text="Rock Paper Scissors")
rps_label.place(x=70, y=30)
sub_label=Label(screen, text="Let's Start the Game")
sub_label.place(x=70, y=55)
winner=Label(screen, text="Winning", bg="green", fg="white")
winner.place(x=200, y=55)

#Buttons
opts_label=Label(screen, text="Your Options:")
opts_label.place(x=70, y=100)

r=Button(screen, text="Rock", command=lambda: you_select(options[0]))
r.place(x=190, y=100)
p=Button(screen, text="Paper", command=lambda: you_select(options[1]))
p.place(x=280, y=100)
s=Button(screen, text="Scissors", command=lambda: you_select(options[2]))
s.place(x=370, y=100)

#Outputs
score_label=Label(screen, text="Score")
score_label.place(x=70, y=150)

you_select_l=Label(screen, text="You Selected: ")
you_select_l.place(x=190, y=150)
you_score_l=Label(screen, text="You Scored: ")
you_score_l.place(x=190, y=170)
comp_select_l=Label(screen, text="Computer Selected: ")
comp_select_l.place(x=190, y=210)
comp_score_l=Label(screen, text="Computer Scored: ")
comp_score_l.place(x=190, y=230)

reset=Button(screen, text="Reset", command=resetting)
reset.place(x=190, y=250)

screen.mainloop()
