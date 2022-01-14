from ahk import AHK, Hotkey
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import time
import tkinter.messagebox
import keyboard
import sys

#from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


#keyboard.send('alt+f, a')


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

root = Tk()
root.title('chillin bro testin')
#root.iconbitmap(bitmap, default)
root.geometry("400x400")

def selected(event):
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set(states[0])

drop = OptionMenu(root, clicked, *states, command=selected)
drop.pack()

root.mainloop()









