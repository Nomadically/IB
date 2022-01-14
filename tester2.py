from ahk import AHK, Hotkey
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import time
import tkinter.messagebox

ahk = AHK()
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def tester():
    #win = list(ahk.windows())
    #print(win)
    for window in ahk.windows():
        print(window.title) #this will list names of open windows
    ahk.run_script('Run Notepad') # Open notepad
    ahk.key_press('Alt')
    ahk.key_press('F')
    win = ahk.find_window(title=b'Gmail - thinkingdrops - Mozilla Thunderbird') # Find the opened window
    win.activate()           # Give the window focus


def showMsg():  
    tkinter.messagebox.showinfo('Message', 'You clicked the Submit button!')
    tester()

button = Button(tkWindow,
    text = 'Submit',
    command = showMsg)  
button.pack()  
  
tkWindow.mainloop()