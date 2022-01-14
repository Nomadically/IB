import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import subprocess



ahk = AHK()
sg.theme('DarkAmber')

for window in ahk.windows():
    if b'Mailware' in window.title:
        mailware = ahk.find_window(title=window.title)
    if b'ibProject' in window.title:
        ib = ahk.find_window(title=window.title)
    if b'Search for Customer' in window.title:
        custfind = ahk.find_window(title=window.title)

"""
may need to comment out above if testing at home
"""

def finding(input):
    f = open('customers11.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    #check = 'bibb'
    for row in csv_reader:
        #print(row['name'])
        #names.append(row['name'])
        #addresses.append(row['address'])
        #zips.append(row['zip'])
        #streets.append(row['street'])
        #websites.append(row['website'])
        #results = []
        if input.title() in row['name']:
            print(row['name'])
            print(row['street'])
            print(row['address'])
            print(row['zip'])
            return (row['name']+'\n'+row['street']+'\n'+row['address']+'\n'+ row['zip'])
            #results.append(row['name'])
    #return results
    f.close

def tester(*inputlist):
    #win = list(ahk.windows())
    #print(win)
    ahk.run_script('Run Notepad') # Open notepad
    #time.sleep(1)
    for window in ahk.windows():
        #print(window.title) #this will list names of open windows
        #if b'Firefox' in window.title: # >>>> now we can shift focus to this app at any point
            #browser = ahk.find_window(title=window.title)  # Find the opened window
        if b'WordPad' in window.title:
            wordpad = ahk.find_window(title=window.title)
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
    keyboard.send('ctrl+a') 
    keyboard.send('ctrl+c')
    wordpad.activate()
    keyboard.send('ctrl+v')
    #subprocess.Popen([r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe", '-new-tab'])# set this to open mailware if needed
    #doing the above, opens process without shifting attention to it (has to finish opening before script resumes)
    subprocess.call([r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"])
 
 # when running find_inmate, add continue after its called in while loop
def find_inmate(fn, ln, inm):
    try:
        mailware.activate()
    except NameError:
        sg.popup('Mailware not active, now starting program - please wait.')
        subprocess.call([r"C:\Program Files (x86)\Mailware 2014\Mailware.exe"])
    keyboard.send('f4')
    keyboard.send('alt+f') #this puts cursor at first name in mailware
    keyboard.write(fn.title())
    keyboard.send('tab')
    keyboard.write(ln.title())
    keyboard.send('enter')
    #after this, need to prompt user if inmate found or not - "No, not found, create account" and "Yes, found"
    
    #keyboard.send('ctrl+a')
    #keyboard.send('ctrl+a')
    
    



# Create a list of prisons
df = pd.read_csv('customers11.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = []
for n in names:
    prisons.append(n)
    
# below is labels 
a = sg.Text("Inmate First Name:", justification='center')
b = sg.Text("Inmate Last Name:", justification='left')
c = sg.Text("Inmate Number:   ", justification='left')
z1 = sg.Text("Select facility:   ", justification='left')

f = sg.Combo(prisons, default_value=names[0], key='fac1', size=(50, 15))
#h = sg.Listbox(v=['Search results will be shown here.'], select_mode='extended', key='facresults', size=(30, 6))
d = sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3), key='OUTPUT')

# below is input areas
a1 = sg.Input(key='fn', tooltip='< Inmate first name here >', size=(30,1), justification='right')
b1 = sg.Input(key='ln', tooltip='< Inmate last name here >', size=(30,1), justification='right')
c1 = sg.Input(key='inum', tooltip='< Inmate number here >', size=(30,1), justification='right')

t1 = sg.Input(key='new', size=(20,1))

# these are buttons
x = sg.Button('Submit')
y = sg.Button('Quit')
#op = sg.Button('Test')
#oz = sg.Button('Tested')


# this is layout of how each of above will be arranged  
layout = [[ sg.Frame('Labelled Group',[[
            a, a1, b, b1, c, c1]])],
          [z1],
          [f],
          [d],
          [x],  [y]
          ]

#layout2 = [[oz],
#           [t1]
#    ]

# Create the window
window = sg.Window('Inmate Account Search and Creation', layout, use_ttk_buttons = True, finalize=True)
#window2 = sg.Window('Inmate Account Search and Creation', layout2, use_ttk_buttons = True, finalize=True)

# Display and interact with the Window using an Event Loop
while True:
    e, v = window.read()
    # this will close app
    if e == sg.WINDOW_CLOSED or e == 'Quit':
        break
    #if e == 'Test me':
        #e2, v2 = window2.read()
    if e == 'Submit':
        if v['fn'] == '' or v['ln'] == '' or v['inum'] == '':
            sg.popup("Please enter complete info for all fields.")
            window['fn'].update('')
            window['ln'].update('')
            window['inum'].update('')
            continue
        finding(v['fac1'])
        tested = ['ok', 'almost', 'there']
        tester(tested)
        #else:
            #sg.popup('Please enter facility name again, '+v['fac']+' not found in database.')
            #continue
    # Output a message to the Multiline element
        window['OUTPUT'].update('First name: ' + v['fn'] +'\n'
                                +'Last name: '+v['ln']+'\n'+
                                'Inmate number: '+v['inum']+
                                finding(v['fac1'])+
                                "Thanks for trying PySimpleGUI",
                              text_color='yellow')

# Finish up by removing from the screen
window.close()

# 'Hello ' + v['fn'] +v['ln']+v['inum']+ "! 