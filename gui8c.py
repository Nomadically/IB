import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import re
from tempfile import NamedTemporaryFile
import shutil
import csv
import codecs
import datetime
import subprocess

# maybe devise ahk script that starts the python program?
ahk = AHK()
sg.theme('DarkAmber')

for window in ahk.windows():
    if b'Mailware' in window.title:
        mailware = ahk.find_window(title=window.title)
    if b'ibProject' in window.title:
        ib = ahk.find_window(title=window.title)
    if b'Search for Customer' == window.title:
        custfind = ahk.find_window(title=window.title)
        custfind.close()


# --- 07/1/21: now writes properly to file ----> need to transpose this into current csv settings
def updating(arg1, **kwargs):  # maybe insert a facID column to help id places? going by names always is..not cool
    today = datetime.date.today().strftime("%B %d, %Y")
    filename = 'AllDetails.csv'  # put name of csv file here
    tempfile = NamedTemporaryFile(mode='a', delete=False)
    newfile = today + '-' + filename
    fields = ['Sno', 'Registration Number', 'Name', 'RollNo', 'Status']
    with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        for row in reader:
            reg = row['Registration Number']
            name = row['Name']
            rollno = row['RollNo']
            status = row['Status']
            for key, value in kwargs.items():
                if row['Sno'] == str(arg1) and key == 'regNum':
                    reg = value
                if row['Sno'] == str(arg1) and key == 'name':
                    name = value
                if row['Sno'] == str(arg1) and key == 'rollno':
                    rollno = value
                if row['Sno'] == str(arg1) and key == 'status':
                    status = value
                print('updating row', row['Sno'])
                row = (
                {'Sno': row['Sno'], 'Registration Number': reg, 'Name': name, 'RollNo': rollno, 'Status': status})
                writer.writerow(row)
                print('Done! Alh')
    shutil.move(tempfile.name, filename)

# below functions take inputs and puts them into mailware, after some stuff checked
def fieldentry(facility):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    for row in csv_reader:
        if facility in row['name']:
            n = row['name']
            str = row['street']
            zpp = row['zip']
            break
    f.close
    print(row)
    results = [n, str, zpp]
    return results


def lencheck(fac, fn, ln, inm):
    # print(len(fn))
    for ele in fac:
        assert (len(ele) <= 40), "Facility name is too long; 40 char limit."
    assert (len(fn) <= 15), "Check inmate's first name: will be truncated if longer than 15 characters."
    assert (
                len(ln + ' #' + inm) <= 20), "Check inmate's last name + number: will be truncated if longer than 20 characters."
    return fac, fn, ln, inm


"""
>>> this is how to handle lencheck results, let user know if length too long

try:
    lencheck('joe', 'ok', '123')
except AssertionError:
    print("Careful with inmate information - some part may be too long and thus shorted by Mailware.")


"""


def mailwarefocus(fac, fn, ln, inm):
    mailware.activate()
    keyboard.send('f4')
    keyboard.send('esc')
    keyboard.send('alt+n')  # this entry puts cursor at first name of new customer form
    # keyboard.send('alt+c') #this entry takes program to current customer
    keyboard.write(fn)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(ln + ' ' + '#' + inm)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[0])  # prison name
    keyboard.send('tab')
    keyboard.write(fac[1])  # street address
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[2])  # zip code
    # time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')
    # ib.activate() # this if want to refocus back to pycharm


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
    'Northern Mariana Islands': 'MP',
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
        # addr.append(saved)
        if s in abbrev_us_state:
            j = abbrev_us_state[s]
            # print(abbrev_us_state[i])
            st = re.search('[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s([0-9]{5})', saved).groupdict()['state']
            if s == st:
                addr.append(row['name'])  # change this to append also street2 or physicalstreet if h3[i-2] !=h0[1]
            if j == st:
                addr.append(row['name'])
    myDict[s] = addr
    print("done: " + s)

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
fn = sg.Input(key='fn', tooltip='Inmate first name here: ', size=(30, 1), justification='left')
ln = sg.Input(key='ln', tooltip='Inmate last name here: ', size=(30, 1), justification='left')
inm = sg.Input(key='inm', tooltip='Inmate number here: ', size=(30, 1), justification='left')

# these are buttons
x = sg.Button('Create Inmate Account')
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
    [sg.Combo((), **options, key="subproject", tooltip='Select state above first, then facility.')],
    # [fin],
    [x],
    [y],
    [z]
]

window = sg.Window('Inmate Account Creation', layout, use_ttk_buttons=True, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Quit'):
        break
    elif event == "mainproject":
        lst = myDict[values[event]]
        window['subproject'].Update(value=lst[0], values=lst)
    elif event == 'Create Inmate Account':
        try:
            lencheck(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
        except AssertionError:
            sg.popup("Length of one or more fields is too long, will be truncated by Mailware - verify account info!")
            mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            continue
        if values['fn'] == '' or values['ln'] == '' or values['inm'] == '' or values['subproject'] == '':
            sg.popup("Please select state and enter complete info for all fields.", title="Error")
            continue
        try:
            mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            # sg.Popup('Ok clicked', keep_on_top=True) >>> maybe use keep on top?
            continue
        except NameError:
            sg.popup("Mailware needs to be turned on!")
            continue
    if event == 'Clear All Data':
        window['fn'].update('')
        window['ln'].update('')
        window['inm'].update('')
        window['mainproject'].update('')
        window['subproject'].update('')
window.close()


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