from ahk import AHK, Hotkey
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import time
import tkinter.messagebox
import keyboard
import sys
import pandas as pd
import csv
import re

#from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


#keyboard.send('alt+f, a')


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


"""
with open('testable.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Prison Name'], row['Zip'])
"""
ahk = AHK()
userinput = input("Name of prison?")
userinput2 = input("Zip of prison?")

with open('../yc startup programs/testable.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        #keep going
        if (userinput in row[0] and userinput2 in row[2]):
            print("here!")
            #print(row[0]) #corresponds to facility name
            #print(row[1]) # " to street
            #print(row[2]) # " to zip code
            win2 = ahk.find_window(title=b'Mailware 2014 - IslamicBookstore.com - [Customer]')  # Find the opened window
            win2.activate()  # this will shift focus to it
            keyboard.send('alt+n')
            keyboard.send('alt+c')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(row[0])  # prison name
            keyboard.send('tab')
            keyboard.write(row[1])  # street address
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(row[2])  # zip code
            keyboard.send('tab')
            keyboard.send('tab')


        #if userinput == row[0]: # if the username shall be on column 3 (-> index 2)
            #print("is in file")
            #print(row[1]+row[2])



#df = pd.read_csv('data.csv')

#print(df.to_string())  



#below makes a popup with dropdown menu of states above

"""
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
"""








