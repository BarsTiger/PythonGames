from tkinter import *


def bAaction():
    print('Спасибо!')


def bBaction():
    print('Урмяяяяяуу! Мне больно')


window = Tk()
buttonA = Button(window, text='Нажми!', command=bAaction)
buttonB = Button(window, text='Не нажимай!', command=bBaction)
buttonA.pack()
buttonB.pack()
window.mainloop()
