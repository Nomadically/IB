import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import re



states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# thank you to @kinghelix and @trevormarburger for this idea
abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

ahk = AHK()
sg.theme('DarkAmber')

def finding(input):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    #check = 'bibb'
    for window in ahk.windows():
        # print(window.title) #this will list names of open windows
        # if b'Firefox' in window.title: # >>>> now we can shift focus to this app at any point
        # browser = ahk.find_window(title=window.title)  # Find the opened window
        # if b'WordPad' in window.title:
        # wordpad = ahk.find_window(title=window.title)
        #if b'Notepad' in window.title:
            #notepad = ahk.find_window(title=window.title)
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
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
            n = row['name']
            s = row['street']
            a = row['address']
            z = row['zip']
            break
            # time.sleep(1)
            # notepad.activate()
    mailware.activate()
    # ahk.type("this is a test run")
    keyboard.send('f4')
    keyboard.send('esc')
    # keyboard.write('The quick brown fox jumps over the lazy dog.')
    # keyboard.write('\nok dude street here') #this enters street addr
    # browser.activate()
    # time.sleep(3)
    # notepad.activate()
    # keyboard.write('This is the info: '+str(inputlist))
    keyboard.send('alt+n')
    keyboard.send('alt+c')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(n)  # prison name
    #time.sleep(1)
    keyboard.send('tab')
    keyboard.write(s)  # street address
    time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(z)  # zip code
    #time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')
    return row
            #return row['name']+'\n'+row['street']+'\n'+row['zip']+'\n'+row['address']
            #results.append(row['name'])
    #return results
    f.close

def tester(**inputlist):
    finding(v['fac1'])
    #win = list(ahk.windows())
    #print(win)
    #ahk.run_script('Run Notepad') # Open notepad
    #time.sleep(1)
    for window in ahk.windows():
        #print(window.title) #this will list names of open windows
        #if b'Firefox' in window.title: # >>>> now we can shift focus to this app at any point
            #browser = ahk.find_window(title=window.title)  # Find the opened window
        #if b'WordPad' in window.title:
            #wordpad = ahk.find_window(title=window.title)
        if b'Notepad' in window.title:
            notepad = ahk.find_window(title=window.title)
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
    #time.sleep(1)
    #notepad.activate()
    mailware.activate()
    #ahk.type("this is a test run")
    keyboard.send('f4')
    keyboard.send('esc')
    #keyboard.write('The quick brown fox jumps over the lazy dog.')
    #keyboard.write('\nok dude street here') #this enters street addr
    #browser.activate()
    #time.sleep(3)
    #notepad.activate()
    #keyboard.write('This is the info: '+str(inputlist))
    keyboard.send('alt+n')
    keyboard.send('alt+c')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(inputlist["name"])  # prison name
    time.sleep(1)
    keyboard.send('tab')
    keyboard.write(inputlist["street"])  # street address
    time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(inputlist["zip"])  # zip code
    time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')

def stfind(i):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    addr = []
    for row in csv_reader:
        saved = row['address']
        #addr.append(saved)
        if i in abbrev_us_state:
            j = abbrev_us_state[i]
            # print(abbrev_us_state[i])
            st = re.search('[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s([0-9]{5})', saved).groupdict()['state']
            if i == st or j == st:
                addr.append(row['name'])
    #print(addr)
    facilities = []
    for p in addr:
        facilities.append(p)
    print(facilities)
    return facilities

# Create a list of prisons
df = pd.read_csv('customers10.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = []
for n in names:
    prisons.append(n)
    
    
    
print(prisons)
pulladdr =[]
for r in addresses:
    pulladdr.append(r)
    

blank = []

# below is labels 
firstname = sg.Text("Inmate First Name:", justification='center')
lastname = sg.Text("Inmate Last Name:", justification='left')
inmnumber = sg.Text("Inmate Number:   ", justification='left')
stateselectlabel = sg.Text("Select state first:   ", justification='left')
facilityselected = sg.Text("Then choose facility:   ", justification='left')

f = sg.Combo(prisons, default_value=prisons[0], key='fac1', size=(50, 15))

h = sg.Combo(states, default_value=states[0], key='fac2', size=(30, 15))
#h = sg.Listbox(v=['Search results will be shown here.'], select_mode='extended', key='facresults', size=(30, 6))
d = sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 10), key='OUTPUT')

# below is input areas
fn = sg.Input(key='fn', tooltip='< Inmate first name here >', size=(30,1), justification='right')
ln = sg.Input(key='ln', tooltip='< Inmate last name here >', size=(30,1), justification='right')
inm = sg.Input(key='inum', tooltip='< Inmate number here >', size=(30,1), justification='right')

# these are buttons
x = sg.Button('Submit')
y = sg.Button('Quit')



# this is layout of how each of above will be arranged  
layout = [ [sg.Frame('Labelled Group',[[
            a, a1, b, b1, c, c1]])     ],
          [h1],
          [h],
          [z1],
          [f],
          [d],
          [x],  [y]]

# Create the window
window = sg.Window('Inmate Account Search and Creation', layout, use_ttk_buttons = True, finalize=True)

# Display and interact with the Window using an Event Loop
while True:
    e, v = window.read()
    # this will close app
    if e == sg.WINDOW_CLOSED or e == 'Quit':
        break
    if e == 'Submit':
        
        if v['fn'] == '' or v['ln'] == '' or v['inum'] == '':
            sg.popup("Please enter complete info for all fields.", title="Error")
            window['fn'].update('')
            window['ln'].update('')
            window['inum'].update('')
            continue
        x = stfind(v['fac2'])
        resulted = []
        for x in x:
            resulted.append(x)
        window['OUTPUT'].update(resulted)
        window['fac1'].update(resulted[2])
        #finding(v['fac1'])
        #tester()
        #else:
            #sg.popup('Please enter facility name again, '+v['fac']+' not found in database.')
            #continue
    # Output a message to the Multiline element
        #window['OUTPUT'].update('First name: ' + v['fn'] +'\n'
        #                        +'Last name: '+v['ln']+'\n'+
        #                        'Inmate number: '+v['inum']+

         #                       "Thanks for trying PySimpleGUI",
          #                    text_color='yellow')

# Finish up by removing from the screen
window.close()

# str(finding(v['fac1']))+
# 'Hello ' + v['fn'] +v['ln']+v['inum']+ "! 