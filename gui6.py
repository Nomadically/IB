import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import re




import PySimpleGUI as sg

items = {
    "ProjectA": ["subproject1a", "subproject2a"],
    "ProjectB": ["subproject1b", "subproject2b"],
    "ProjectC": ["subproject1c", "subproject2c"],
}

options = {
    "font": ('Helvetica', 16),
    "size": (15, 1),
    "readonly": True,
    "enable_events": True,
}

layout = [
    [sg.Combo(list(items.keys()), **options, key="mainproject")],
    [sg.Combo((),                 **options, key="subproject")],
]

window = sg.Window('COMBO', layout)

#===============================================================================
# while True:
# 
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     elif event == "mainproject":
#         lst = items[values[event]]
#         window['subproject'].Update(value=lst[0], values=lst)
# 
# window.close()
#===============================================================================



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

# need to create dict of state:facilities, done



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








states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado",
"CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois",
"IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":
"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska",
"NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina",
"ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina",
"SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington",
"WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}




if 'AL' in list(states.keys()):
    #print(states.keys())
    print("im here")



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
                addr.append(row['name'])
            if j == st:
                addr.append(row['name'])
    myDict[s] = addr
    print("done: "+s)

print(myDict['CA'])








"""
ahk = AHK()
sg.theme('DarkAmber')

# Create a list of prisons
df = pd.read_csv('customers9.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = []
for n in names:
    prisons.append(n)


prisonInfo = {'MD': {'PrisonName':['Street Here', '12345']},
          'NY': {"Prison2Name":['Street2 Here', '67891']}}

people = {'MD': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'NY': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def finding(input):
    f = open('customers9.csv', 'rt')
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

def tester(*inputlist):
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






            
# below is labels 
a = sg.Text("inmate's first name =")
b = sg.Text("inmate's last name =")
c = sg.Text("inmate's number =")
z1 = sg.Text("name of facility =")

f = sg.Combo(prisons, default_value=names[0], key='fac1', size=(30, 6))
d = sg.Text(size=(40,1), key='OUTPUT')

# below is input areas
a1 = sg.Input(key='firstname', tooltip='< Inmate first name here >')
b1 = sg.Input(key='lastname', tooltip='< Inmate last name here >')
c1 = sg.Input(key='inmatenum', tooltip='< Inmate number here >')
z = sg.Input(key='fac', tooltip='< Facility name here >') # this is the input area that will need to be updated

# these are buttons
x = sg.Button('Submit')
y = sg.Button('Quit')



# this is layout of how each of above will be arranged  
layout = [[a, a1],
          [b, b1],
          [c, c1],
          [z1, z],
          [f],
          [d],
          [x, y]]

# Create the window
window = sg.Window('Inmate Account Search and Creation', layout, use_ttk_buttons = True, finalize=True)

# Display and interact with the Window using an Event Loop
while True:
    e, v = window.read()
    # this will close app
    if e == sg.WINDOW_CLOSED or e == 'Quit':
        break
    if e == 'Submit':
       
        if finding(v['fac']) != None or v['fac1'] != None:
            finding(v['fac'])
        else:
            sg.popup('Please enter facility name again, '+v['fac']+' not found in database.')
            continue
    # Output a message to the window
    window['OUTPUT'].update('Hello ' + v['firstname'] +v['lastname']+v['inmatenum']+ "! Thanks for trying PySimpleGUI",
                              text_color='yellow')

# Finish up by removing from the screen
window.close()

"""
