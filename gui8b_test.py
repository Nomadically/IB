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
import pyperclip
import win32ui

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
def updating(arg1, **kwargs): # maybe insert a facID column to help id places? going by names always is..not cool
    today = datetime.date.today().strftime("%B %d, %Y")
    filename = 'AllDetails.csv' #put name of csv file here
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
                row = ({'Sno': row['Sno'], 'Registration Number': reg, 'Name': name, 'RollNo': rollno, 'Status': status})
                writer.writerow(row)
                print('Done! Alh')
    shutil.move(tempfile.name, filename)


# this function for updating csv entries
def updatingentry(arg1, **kwargs):
    today = datetime.date.today().strftime("%B %d, %Y")
    filename = 'customers10-Copy.csv'
    tempfile = NamedTemporaryFile(mode='a', delete=False)
    newfile = today + '-' + filename
    fields = ['name', 'street', 'address', 'zip', 'website']
    with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        for row in reader:
            name = row['name']
            street = row['street']
            address = row['address']
            zip = row['zip']
            website = row['website']
            for key, value in kwargs.items():
                if row['name'] == str(arg1) and key == 'street':
                    street = value
                if row['name'] == str(arg1) and key == 'address':
                    address = value
                if row['name'] == str(arg1) and key == 'zip':
                    zip = value
                if row['name'] == str(arg1) and key == 'website':
                    website = value
                if row['name'] == str(arg1) and key == 'name':
                    name = value
                print('updating row', row['name'])
                row = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
                writer.writerow(row)
                print('Done! Alh')
    shutil.move(tempfile.name, filename)

#updating2('Bibb Correctional Facility', street='565 Bibb Lane, Apt. #625')

#updating2('Bibb Correctional Facility', street='565 Bibb Lane')



# this function for making new entries to csv
def newentry(arg1, **kwargs):
    #filename = 'customers10-Copy.csv'
    filename = 'customers10.csv'
    fields = ['name', 'street', 'address', 'zip', 'website']
    with codecs.open(filename, 'a', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        name = str(arg1)
        street = ''
        address = ''
        zip = ''
        website = ''
        for key, value in kwargs.items():
            if key == 'street':
                street = value
            if key == 'address':
                address = value
            if key == 'zip':
                zip = value
            if key == 'website':
                website = value
        row = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
        writer.writerow(row)
        print('Done! Alh')


def finding(input):
    f = open('customers10.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    # check = 'bibb'
    for row in csv_reader:
        if input.title() in row['name']:
            print(row['name'])
            print(row['address'])
            print(row['street'])
            print(row['zip'])
            return row['name']
        else:
            return "Not found! Please contact admin."
    f.close

def WindowExists(classname):
    try:
        win32ui.FindWindow(classname, None)
    except win32ui.error:
        return False
    else:
        return True


def finding(fn, ln):
    for window in ahk.windows():
        if b'Search for Customer' == window.title:
            custfind = ahk.find_window(title=window.title)
            custfind.close()
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
            mailware.activate()
    keyboard.send('f4')
    time.sleep(1)
    keyboard.send('alt+f')
    keyboard.write(fn)
    keyboard.send('tab')
    keyboard.write(ln)
    time.sleep(1)
    keyboard.send('enter')


# don't bother with find inmate aspect, just keep program to creating account with info given
# when running find_inmate, add continue after its called in while loop
# def find_inmate(fn, ln, inm):
#     try:
#         mailware.activate()
#     except NameError:
#         sg.popup('Mailware not active, now starting program - please wait.')
#         subprocess.call([r"C:\Program Files (x86)\Mailware 2014\Mailware.exe"])
#     try:
#         custfind.activate()
#     except NameError:
#         keyboard.send('f4')
#     keyboard.send('esc')
#     keyboard.send('f4')
#     keyboard.send('alt+f')  # this puts cursor at first name in mailware
#     keyboard.write(fn.title())
#     keyboard.send('tab')
#     keyboard.write(ln.title())
#     keyboard.send('enter')
#     return fn, ln, inm

"""
def my_popup():
    for window in ahk.windows():
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
        if b'ibProject' in window.title:
            ib = ahk.find_window(title=window.title)
        if b'Search for Customer' in window.title:
            custfind = ahk.find_window(title=window.title)
        if b'Inmate Account' in window.title:
            prog = ahk.find_window(title=window.title)

    layout1 = [
        [sg.Text("Does inmate customer account exist?")],
        [sg.Button("Yes, done for now."), sg.Button("No, proceed to click on 'Create Account'.")]
    ]
    win = sg.Window("My Popup", layout1, modal=True,
        grab_anywhere=True, enable_close_attempted_event=True)
    ev, val = win.read()
    if ev in (sg.WINDOW_CLOSED, 'Yes, done for now.', sg.WINDOW_CLOSE_ATTEMPTED_EVENT, 'CANCEL'):
        custfind.activate()
        win.close()
    if ev == "No, proceed to click on 'Create Account'.":
        #prog.activate() >>>> need to fix here (how to revert focus back to main program)
        win.close()
    win.close()
    #window.write_event_value(event, None)

"""


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
    #print(len(fn))
    for ele in fac:
        assert (len(ele) <= 40), "Facility name is too long; 40 char limit."
    assert (len(fn) <= 15), "Check inmate's first name: will be truncated if longer than 15 characters."
    assert (len(ln+' #'+inm) <= 20), "Check inmate's last name + number: will be truncated if longer than 20 characters."
    return fac, fn, ln, inm
    
"""
>>> this is how to handle lencheck results, let user know if length too long

try:
    lencheck('joe', 'ok', '123')
except AssertionError:
    print("Careful with inmate information - some part may be too long and thus shorted by Mailware.")


"""
# this function updates the address in mailware
def mailwareupdate(fac):
    for window in ahk.windows():
        if b'Search for Customer' == window.title:
            custfind = ahk.find_window(title=window.title)
            custfind.close()
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
            mailware.activate()
    keyboard.send('f4')
    keyboard.send('esc')
    keyboard.send('alt+n') #this entry puts cursor at first name of new customer form
    keyboard.send('alt+c') #this entry takes program to current customer
    keyboard.send('esc') #this ensures that no popup gets in the way
    #keyboard.send('alt+p') #this entry puts cursor at first name of ship-to address
    #keyboard.write(fn)
    keyboard.send('tab')
    keyboard.send('tab')
    #keyboard.write(ln+' '+'#'+inm)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[0])  # prison name
    keyboard.send('tab')
    keyboard.write(fac[1])  # street address
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[2])  # zip code
    #time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')
    #ib.activate() # this if want to refocus back to pycharm







def mailwarefocus(fac, fn, ln, inm):
    for window in ahk.windows():
        if b'Search for Customer' == window.title:
            custfind = ahk.find_window(title=window.title)
            custfind.close()
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
            mailware.activate()
    keyboard.send('f4')
    keyboard.send('esc')
    keyboard.send('alt+n') #this entry puts cursor at first name of new customer form
    #keyboard.send('alt+c') #this entry takes program to current customer
    keyboard.write(fn)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(ln+' '+'#'+inm)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[0])  # prison name
    keyboard.send('tab')
    keyboard.write(fac[1])  # street address
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[2])  # zip code
    #time.sleep(1)
    keyboard.send('tab')
    keyboard.send('tab')
    #ib.activate() # this if want to refocus back to pycharm



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

"""
q1 = input("do you need to update anything?")
if q1 == 'yes':
    q_name = input("name?")
    q_street = input("street?")
    q_address = input("address?")
    q_zip = input("zip?")
    q_website = input("website?")
    newentry(q_name, street=q_street, address=q_address, zip=q_zip, website=q_website)

"""




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
fn = sg.Input(key='fn', tooltip='Inmate first name here: ', size=(30,1), justification='left')
ln = sg.Input(key='ln', tooltip='Inmate last name here: ', size=(30,1), justification='left')
inm = sg.Input(key='inm', tooltip='Inmate number here: ', size=(30,1), justification='left')

# these are buttons
x = sg.Button('Create Inmate Account')
y = sg.Button('Quit')
z = sg.Button('Clear All Data')
xyz = sg.Button('Need to create or update facility info?')
search = sg.Button('Check Online Info')
updateinfo = sg.Button('Update Address')
newfac = sg.Button('Add New Facility to CSV - Admin Only')
find = sg.Button('Find in Mailware')


#fin = sg.Button('Find Inmate')

layout = [
    [firstname],
    [fn],
    [lastname],
    [ln],
    [inmnumber],
    [inm],
    [stateselectlabel],
    [sg.Combo(sorted(list(myDict.keys())), **options, key="mainproject", tooltip='Select state first, then facility below.')],
    [facilityselected],
    [sg.Combo((),                 **options, key="subproject", tooltip='Select state above first, then facility.')],
    #[fin],
    [find],
    [x],
    [search],
    [updateinfo],
    [y],
    [z]
]


window = sg.Window('Inmate Account Creation', layout, use_ttk_buttons=True, finalize=True)

#window2 = sg.Window('Updating/Creating New Facility', layout2, use_ttk_buttons=True, finalize=True)

while True:
    event, values = window.read()
    ready = False
    if event in (sg.WINDOW_CLOSED, 'Quit'):
        break
    elif event == "mainproject":
        lst = sorted(myDict[values[event]])
        window['subproject'].Update(value=lst[0], values=lst)
        ready = True
    #elif event == 'Find Inmate': # here, just have inmate info pulled from custfind, which should already be open
        # 08/03/21: no, don't pull custfind or any cust searching info, just do acc creation with this program
        #find_inmate(values['fn'], values['ln'], values['inm'])
        #time.sleep(2)
        #sg.popup("Was inmate found?")
        # from here, take values entered into name first and last, then close cust find window (via escape)
        #my_popup() # <<< change here
        #continue
    elif event == 'Find in Mailware':
        if values['fn'] == '' or values['ln'] == '':
            sg.popup("Please input first and last name.", title="Error")
            continue
        try:
            finding(values['fn'], values['ln'])
        except NameError:
            sg.popup("Something not running, contact Admin.", title="Error")
            continue
    elif event == 'Create Inmate Account':
        try:
            lencheck(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
        except AssertionError:
            sg.popup("Length of one or more fields is too long, will be truncated by Mailware - verify account info!")
            mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            continue
        #mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
        if values['fn'] == '' or values['ln'] == '' or values['inm'] == '' or values['subproject'] == '':
            sg.popup("Please select state and enter complete info for all fields.", title="Error")
            #window['fn'].update('')
            #window['ln'].update('')
            #window['inm'].update('')
            continue
        try:
            mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            #sg.Popup('Ok clicked', keep_on_top=True)
            continue
        except NameError:
            sg.popup("Mailware needs to be turned on!")
            continue
    #if event == 'Add New Facility to CSV - Admin Only':
        #newentry()
    if event == 'Clear All Data':
        window['fn'].update('')
        window['ln'].update('')
        window['inm'].update('')
        window['mainproject'].update('')
        window['subproject'].update('')
    if event == 'Check Online Info':
        pyperclip.copy(values['inm'])
        url = 'https://www.google.com/search?q='+values['mainproject']+' inmate locator'
        webbrowser.open(url, new=0, autoraise=True)
    if event == 'Update Address':
        mailwareupdate(fieldentry(values['subproject']))
    # elif event == 'Need to create or update facility info?':
    #     break
    #     q1 = input("Create or Update?")
    #     if q1 == 'Create':
    #         facname = input("What is new facility's name?")
    #         facstreet = input("What is new facility's street?")
    #         facaddr = input("What is new facility's address?")
    #         faczip = input("What is new facility's zip?")
    #         facwebsite = input("What is new facility's street?")
    #         newentry(facname, street=facstreet, address=facaddr, zip=faczip, website=facwebsite)
    #         print("Added "+facname+" to CSV!")
    #     if q1 == 'Update':
    #         facname = input("What is facility's name?")
    #         # check logic here! not ready yet
    #         print(finding(facname))
    #         facstreet = input("What is new facility's street?")
    #         facaddr = input("What is new facility's address?")
    #         faczip = input("What is new facility's zip?")
    #         facwebsite = input("What is new facility's street?")
    #         updatingentry(facname, street=facstreet, address=facaddr, zip=faczip, website=facwebsite)
    #         print("Added "+facname+" to CSV!")

window.close()

"""

    elif event == 'Create New Inmate Acc from Search Fields':
        for window in ahk.windows():
            if b'Search for Customer' == window.title:
                custfind = ahk.find_window(title=window.title)
                custfind.activate()
            else:
                sg.popup("No search field open in Mailware.")
                continue
            keyboard.send('alt+f')  # this moves cursor to first name area
            keyboard.send('ctrl+c')
            texty = pyperclip.paste()
            window['fn'].update(texty)
            #keyboard.send('alt+l')  # this moves cursor to last name area




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