from ahk import AHK, Hotkey
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import time
import tkinter.messagebox

ahk = AHK()

#ahk.run_script('Run Notepad') # Open notepad

#ahk.send_input('Hello`, World{!}')
#ahk.key_press('a')
#ahk.key_press('Tab')

def tester():
    win = list(ahk.windows())
    print(win)
    for window in ahk.windows():
        print(window.title) #this will list names of open windows
    ahk.run_script('Run Notepad') # Open notepad
    ahk.key_press('Alt')
    ahk.key_press('F')
    win = ahk.find_window(title=b'Work-IB - Gmail - thinkingdrops - Mozilla Thunderbird') # Find the opened window
    win.activate()           # Give the window focus


#below is one
"""
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def showMsg():  
    tkinter.messagebox.showinfo('Message', 'You clicked the Submit button!')

button = Button(tkWindow,
    text = 'Submit',
    command = showMsg)  
button.pack()  
  
tkWindow.mainloop()
"""
#above is one thing


# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Maryland - ECI",
    "California - SVSP",
    "Nevada - DOC",
    "New York - ECF"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Maryland - ECI" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "click Me" , command = tester ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()


"""
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

----

key_combo = '#n' # Define an AutoHotkey key combonation
script = 'Run Notepad' # Define an ahk script
hotkey = Hotkey(ahk, key_combo, script) # Create Hotkey
hotkey.start()  #  Start listening for hotkey
"""