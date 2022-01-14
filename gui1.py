from tkinter import *
import pandas as pd
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import PySimpleGUI as sg
from ttkthemes import ThemedTk
import csv
from ahk import AHK, Hotkey
import keyboard

ahk = AHK()
root = Tk()
#root = ThemedTk(theme="black")
root.title('Inmate Name and Data Entry')
#root.iconbitmap('c:/gui/codemy.ico')
#root.geometry("400x400")
root.geometry("")


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#window = ThemedTk(theme="arc")

def finding(input):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    #check = 'bibb'
    for row in csv_reader:
        #print(row['name'])
        #names.append(row['name'])
        #addresses.append(row['address'])
        #zips.append(row['zip'])
        #streets.append(row['street'])
        #websites.append(row['website'])
        if input == row['name']:
            print(row['name'])
            print(row['address'])
            print(row['street'])
            print(row['zip'])
            return row 
    f.close

def tester(inputlist):
    #win = list(ahk.windows())
    #print(win)
    ahk.run_script('Run Notepad') # Open notepad
    #time.sleep(1)
    for window in ahk.windows():
        #print(window.title) #this will list names of open windows
        #if b'Firefox' in window.title: # >>>> now we can shift focus to this app at any point
            #browser = ahk.find_window(title=window.title)  # Find the opened window
        #if b'WordPad' in window.title:
            #wordpad = ahk.find_window(title=window.title)
        if b'Notepad' in window.title:
            notepad = ahk.find_window(title=window.title)
    #time.sleep(1)
    notepad.activate()
    #ahk.type("this is a test run")
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    keyboard.write('\nok dude street here') #this enters street addr
    #browser.activate()
    #time.sleep(3)
    #notepad.activate()
    keyboard.write('This is the info: '+str(inputlist))

# Update the listbox
def update(data):
    # Clear the listbox
    facility_list.delete(0, END)
    # Add prisons to listbox
    for item in data:
        facility_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
    # Delete whatever is in the entry box
    entry_facility.delete(0, END)
    # Add clicked list item to entry box
    entry_facility.insert(0, facility_list.get(ANCHOR))


# Create function to check entry vs listbox
def check(e):
    # grab what was typed
    typed = entry_facility.get()
    if typed == '':
        data = prisons
    else:
        data = []
        for item in prisons:
            if typed.lower() in item.lower():
                data.append(item)
    # update our listbox with selected items
    update(data)

# Button to press
def helloCallBack():
   messagebox.showinfo(title="Ok here", message = entry_firstname.get()+" "+entry_lastname.get()+" "+entry_inmatenum.get()+
                       " "+entry_facility.get())
   print((entry_firstname.get()+" "+entry_lastname.get()+" "+entry_inmatenum.get()+
                       entry_facility.get()))
   finding(facility_list.get(ANCHOR))
   tester(finding(facility_list.get(ANCHOR)))           

# First name's box's label + entry field + binding
label_firstname = ttk.Label(root, text="Enter First Name:",
    font=("Helvetica", 12))
label_firstname.pack()
entry_firstname = Entry(root, font=("Helvetica", 12))
entry_firstname.pack()
entry_firstname.bind("<KeyRelease>", check)


# Last name's box's label + entry field + binding
label_lastname = ttk.Label(root, text="Enter Last Name:",
    font=("Helvetica", 12))
label_lastname.pack()
entry_lastname = Entry(root, font=("Helvetica", 12))
entry_lastname.pack()
entry_lastname.bind("<KeyRelease>", check)

# Inmate number' box's label + entry field + binding
label_inmatenum = ttk.Label(root, text="Enter Inmate Number:",
    font=("Helvetica", 12))
label_inmatenum.pack()
entry_inmatenum = Entry(root, font=("Helvetica", 12))
entry_inmatenum.pack()
entry_inmatenum.bind("<KeyRelease>", check)



# Facility box's label + entry field + binding
label_facility = ttk.Label(root, text="Begin typing Facility name:",
    font=("Helvetica", 12))
label_facility.pack(pady=0)
entry_facility = Entry(root, font=("Helvetica", 12))
entry_facility.pack(pady=0)
entry_facility.bind("<KeyRelease>", check)


# Create a listbox
label_listbox = ttk.Label(root, text="Click on desired facility, then press Submit",
    font=("Helvetica", 12))
label_listbox.pack(pady=0)
facility_list = Listbox(root, width=40)
facility_list.pack(pady=0)

B = ttk.Button(root, text ="Submit", command = helloCallBack)
B.pack()


# Create a list of prisons
df = pd.read_csv('customers10.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = names



# Add the prisons to our list
# update(prisons)
update(names)


# Create a binding on the listbox onclick
facility_list.bind("<<ListboxSelect>>", fillout)



root.resizable(True, True)
root.mainloop()