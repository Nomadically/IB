import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import re

# maybe devise ahk script that starts the python program?
ahk = AHK()
sg.theme('DarkAmber')

for window in ahk.windows():
    if b'Mailware' in window.title:
        mailware = ahk.find_window(title=window.title)
    if b'ibProject' in window.title:
        ib = ahk.find_window(title=window.title)
    if b'Search for Customer' in window.title:
        custfind = ahk.find_window(title=window.title)


def update(ov):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    for row in csv_reader:
        if ov in row['name']:
            row['name']
            # need to use csv dictwriter object, see preproto6


# below function takes inputs and puts them into mailware
def fieldentry(input, fn, ln, inm):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    for row in csv_reader:
        if input in row['name']:
            print(row['name'])
            print(row['street'])
            print(row['address'])
            print(row['zip'])
            n = row['name']
            s = row['street']
            a = row['address']
            z = row['zip']
            try: #now solved in case the f4 search window is already open in mailware when program starts
                custfind.close()
            except NameError:
                pass
            mailware.activate()
            keyboard.send('f4')
            keyboard.send('esc')
            keyboard.send('alt+n') #this entry puts cursor at first name of new customer form
            #keyboard.send('alt+c') #this entry takes program to current customer
            keyboard.write(fn) # this puts first name
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(ln+' '+'#'+inm) # this puts last name + inmate number
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(n)  # prison name
            keyboard.send('tab')
            keyboard.write(s)  # street address
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(z)  # zip code
            #time.sleep(1)
            keyboard.send('tab')
            keyboard.send('tab')
            #ib.activate() # this if want to refocus back to pycharm
            break
    f.close
    return row



states0 = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
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

# below will create dictionary that to populate two combo boxes 
myDict = {}

for s in states0:
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    addr = []
    for row in csv_reader:
        saved = row['address']
        #addr.append(saved)
        if s in abbrev_us_state:
            j = abbrev_us_state[s]
            # print(abbrev_us_state[i])
            st = re.search('[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s([0-9]{5})', saved).groupdict()['state']
            if s == st:
                addr.append(row['name']) #change this to append also street2 or physicalstreet if h3[i-2] !=h0[1]
            if j == st:
                addr.append(row['name'])
    myDict[s] = addr
    print("done: "+s)

print(myDict['AZ'])

options = {
    "font": ('Helvetica', 16),
    "size": (35, 5),
    "readonly": True,
    "enable_events": True,
}

# below is labels 
firstname = sg.Text("Inmate First Name:", justification='center')
lastname = sg.Text("Inmate Last Name:", justification='left')
inmnumber = sg.Text("Inmate Number:   ", justification='left')
stateselectlabel = sg.Text("First, select state:   ", justification='left')
facilityselected = sg.Text("Then, choose facility:   ", justification='left')

# below is input areas
fn = sg.Input(key='fn', tooltip='Inmate first name here: ', size=(30,1), justification='right')
ln = sg.Input(key='ln', tooltip='Inmate last name here: ', size=(30,1), justification='right')
inm = sg.Input(key='inm', tooltip='Inmate number here: ', size=(30,1), justification='right')

# these are buttons
x = sg.Button('Submit')
y = sg.Button('Quit')
z = sg.Button('Clear All Data')

layout = [
    [firstname],
    [fn],
    [lastname],
    [ln],
    [inmnumber],
    [inm],
    [stateselectlabel],
    [sg.Combo(list(myDict.keys()), **options, key="mainproject", tooltip='Select state first, then facility below.')],
    [facilityselected],
    [sg.Combo((),                 **options, key="subproject", tooltip='Select state above first, then facility.')],
    [x],
    [y],
    [z]
]


window = sg.Window('Inmate Account Creation', layout, use_ttk_buttons=True, finalize=True)

while True:
 
    event, values = window.read()
    ready = False
    if event in (sg.WINDOW_CLOSED, 'Quit'):
        break
    elif event == "mainproject":
        lst = myDict[values[event]]
        window['subproject'].Update(value=lst[0], values=lst)
        ready = True
    if event == 'Submit':
        if values['fn'] == '' or values['ln'] == '' or values['inm'] == '' or values['subproject'] == '':
            sg.popup("Please select state and enter complete info for all fields.", title="Error")
            #window['fn'].update('')
            #window['ln'].update('')
            #window['inm'].update('')
            continue
        fieldentry(values['subproject'], values['fn'], values['ln'], values['inm'])
            #sg.Popup('Ok clicked', keep_on_top=True)
    if event == 'Clear All Data':
        window['fn'].update('')
        window['ln'].update('')
        window['inm'].update('')
        window['mainproject'].update('')
        window['subproject'].update('')
 
window.close()

"""
layout = [
    [firstname],
    [fn],
    [lastname],
    [ln],
    [inmnumber],
    [inm],
    [stateselectlabel],
    [sg.Combo(list(myDict.keys()), **options, key="mainproject", tooltip='Select state first, then facility below.')],
    [facilityselected],
    [sg.Combo((),                 **options, key="subproject", tooltip='Select state above first, then facility.')],
    [x],
    [y]
]



"""

"""
[ sg.Frame('Labelled Group',[[
            a, a1, b, b1, c, c1]])]

[ sg.Frame('Inmate Information',[[
            [firstname, fn],
            [lastname, ln],
            [inmnumber, inm]]])]

# this is name of that shazam print window >>>>


b'Shazam Report Wizard: \\\\paradise\\mailware2013\\data\\Reports\\A - Inmate Standard Letter.srw'

for mailware entry fields:
99999999999999999999 = last name max length is 20 chars
999999999999999 = first name max length is 15 chars

99999999999999999999999999999999999999999999999999999999999999999999 = 69

9999999999999999999999999999999999999999
9999999999999999999999999999999999999999
9999999999999999999999999999999999999999 = max length of addr and company name fields is 40 chars

"""