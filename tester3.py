from ahk import AHK, Hotkey
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import time
import tkinter.messagebox

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

states = {
    'MD' : 'www.google.com'
}


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.after(3000, lambda: popup.destroy())
    popup.mainloop()
    
#command = lambda: popupmsg("popup message here!"))


def find_state():
    entry = e1.get()
    if entry not in states:
        e1.delete(0, tk.END)
        msg = "Sorry, state not found. Enter abbreviation as 2 letter capitals only."
        popupmsg(msg)
        master.quit()

    else:
        state = e1.get()
        url = states.get(state)
        webbrowser.open(url, new=0, autoraise=True)
        e1.delete(0, tk.END)

master = tk.Tk()
tk.Label(master, 
         text="Which state are you looking for? Enter 2-letter abbreviation, ie MD").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

def process(event=None):
    find_state()
e1.bind('<Return>', process)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Press Enter to Find State Info', command=find_state).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
