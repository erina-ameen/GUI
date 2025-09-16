from tkinter import*
from googletrans import Translator
from gtts import gTTS
import os

screen=Tk()
screen.geometry("300x240")

def convert():
    language="fr"
    t=entry.get()
    translator=Translator()
    translated_text=translator.translate(t, dest="fr")
    converter=gTTS(text=translated_text.text, lang=language, slow=False)
    converter.save("record.wav")
    os.system("record.wav")

top_f=Frame(screen, background="pink", height="100")
title=Label(top_f, text="Text to Speech", background="pink")
title.place(x=120, y=40)
top_f.pack(fill=X)

bottom_f=Frame(screen, background="light green", height="200")
entry=Entry(bottom_f)
entry.place(x=100, y=20)
submit=Button(bottom_f, text="Submit", command=convert)
submit.place(x=140, y=50)
bottom_f.pack(fill=X)

screen.mainloop()