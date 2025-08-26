from tkinter import *
import random

screen=Tk()
screen.geometry("400x400")
screen.title("Math Quiz")
screen.config(background="light grey")

questions=["5+3", "9-4", "6x2", "15÷3", "7+6"]
answers=["8", "5", "12", "5", "13"]
selected_question=random.choice(questions)
question_index=questions.index(selected_question)

def start_game():
    global selected_question_entry
    screen.config(background="light blue")
    start.destroy()
    title.place(x=20, y=20)

    selected_question_label.place(x=20, y=60)

    selected_question_entry=Entry(screen)
    selected_question_entry.place(x=20, y=90)

    submit=Button(screen, text="Submit", command=checking)
    submit.place(x=20, y=120)

selected_question_label=Label(screen, text=str(selected_question))

def next_question():
        global questions, selected_question_label, selected_question, question_index
        selected_question=random.choice(questions)
        selected_question_label.config(screen, text=selected_question)
        question_index=questions.index(selected_question)


def checking():
    global answers, questions, question_index, selected_question_entry
    correct_answer=answers[question_index]
    guess=selected_question_entry.get()
    if guess==correct_answer:
        status.config(text="Correct!", fg="white", bg="green")
        questions.remove(selected_question)
    else:
        status.config(text="Wrong!", fg="white", bg="red")
    status.place(x=20, y=200)
    next_question()

status=Label(screen, text="")

title=Label(screen, text="Math Quiz")
title.place(x=180, y=160)
start=Button(screen, text="Start Quiz", command=start_game)
start.place(x=180, y=190)

screen.mainloop()
