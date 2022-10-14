from tkinter import *
from random import randint as r

from words import words as w


def get_words(words):
    index1 = r(0, (len(words) - 1))
    index2 = r(0, (len(words) - 1))
    while index1 == index2:
        index2 = r(0, (len(words)))
    return [words[index1], words[index2]]


def button_click():
    words = get_words(w)
    processed = f'{words[0].upper()}    ~~AND~~    {words[1].upper()}'
    lbl.configure(text=processed)


window = Tk()
window.title("Two Words")
window.geometry('600x400')

lbl = Label(window, text="Ready?", font='Times 14', width=60, height=15)
lbl.grid(column=0, row=0)

btn = Button(window, text="TWO WORDS NOW!", command=button_click)
btn.grid(column=0, row=100)

window.mainloop()
