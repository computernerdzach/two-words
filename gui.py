# Imports
from tkinter import *
from random import randint as r

from words import words as w


# Functions
# generate two random words
def get_words():
    index1 = r(0, (len(w)))
    index2 = r(0, (len(w)))
    while index1 == index2:
        index2 = r(0, (len(w)))
    return [w[index1], w[index2]]


# post randomized words to label boxes
def button_click():
    words = get_words()
    lbl1.configure(text=words[0])
    lbl2.configure(text=words[1])


# GUI
# build and configure the gui
window = Tk()
window.title("Two Words")
window.geometry('560x325')
window.configure(bg="steelblue")

# word 1
lbl1 = Label(window, text="TWO", font='Times 14', width=30, height=15, bg="lightblue", padx=1, pady=1)
lbl1.grid(column=0, row=0)

# spacer
lblSpace = Label(window, width=1, height=17, bg="steelblue")
lblSpace.grid(column=1, row=0)

# word 2
lbl2 = Label(window, text="WORDS", font='Times 14', width=30, height=15, bg="lightblue", padx=1, pady=1)
lbl2.grid(column=2, row=0)

# word randomizer
btn = Button(window, text="TWO WORDS NOW!", command=button_click, width=20, bg="beige")
btn.grid(column=0, row=100, columnspan=3)

# main loop
window.mainloop()
