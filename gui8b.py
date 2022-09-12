import time

import PySimpleGUI as sg
from ahk import AHK, Hotkey
import keyboard
import webbrowser
# import time
# import pandas as pd
# import csv
import re
from tempfile import NamedTemporaryFile
import shutil
import csv
import codecs
import datetime
# import subprocess
import pyperclip
# import win32ui
# import os
# import sys


# 4/22/22: can implement running python within a python script, see below
# https://stackoverflow.com/questions/3316961/call-program-with-arguments

# 2/22/22: can now find inmate info straight from vinelink without entering any info>
#https://vinelink.vineapps.com/search/persons;limit=20;offset=0;showPhotos=false;isPartialSearch=false;siteRefId=CASWVINE;personContextRefId=k13758;stateServed=CA
# need to modify these parts of URL = 1) "(state by 2 letter Abbrev)SWVINE", 2) personContextRefId="(inmate number here)", and 3) stateServed="(state by 2 letter abbrev)"


# 2/25/22: maybe same as vine URL works for FL state:
# http://www.dc.state.fl.us/OffenderSearch/list.aspx?Page=List&TypeSearch=AI&DataAction=Filter&dcnumber=E31995&photosonly=0&nophotos=1&matches=20

#http://www.dc.state.fl.us/OffenderSearch/list.aspx?Page=List&TypeSearch=AI&DataAction=Filter&dcnumber=[dc number]&photosonly=0&nophotos=1&matches=20

#http://www.dc.state.fl.us/OffenderSearch/list.aspx?Page=List&TypeSearch=AI&DataAction=Filter&dcnumber=l39407&photosonly=0&nophotos=1&matches=20

#https://www.dpscs.state.md.us/inmate/search.do?searchType=name&firstnm=Delonte&lastnm=norwood
# 3/14/22: so florida has this, Maryland, maybe other states as well

# 3/24/22:seems Texas has a way too:
# https://inmate.tdcj.texas.gov/InmateSearch/viewDetail.action?sid=02734683

# maybe devise ahk script that starts the python program?
ahk = AHK()
#sg.theme('DarkAmber')
sg.theme('DarkTeal6')


def Channergy():
    win_customer = ahk.win_get(title='Search for Customer')
    win_customer.close()
    win_report = ahk.win_get(title='Shazam Report Wizard')
    win_report.close()
    win_main = ahk.win_get(title='Channergy 2021 Client/Server')
    win_main.activate()


Channergy()


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
# def updatingentry(arg1, **kwargs):
#     today = datetime.date.today().strftime("%B %d, %Y")
#     filename = 'customers10-Copy.csv'
#     tempfile = NamedTemporaryFile(mode='a', delete=False)
#     newfile = today + '-' + filename
#     fields = ['name', 'street', 'address', 'zip', 'website']
#     with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
#         reader = csv.DictReader(csvfile, fieldnames=fields)
#         writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
#         for row in reader:
#             name = row['name']
#             street = row['street']
#             address = row['address']
#             zip = row['zip']
#             website = row['website']
#             for key, value in kwargs.items():
#                 if row['name'] == str(arg1) and key == 'street':
#                     street = value
#                 if row['name'] == str(arg1) and key == 'address':
#                     address = value
#                 if row['name'] == str(arg1) and key == 'zip':
#                     zip = value
#                 if row['name'] == str(arg1) and key == 'website':
#                     website = value
#                 if row['name'] == str(arg1) and key == 'name':
#                     name = value
#                 print('updating row', row['name'])
#                 row = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
#                 writer.writerow(row)
#                 print('Done! Alh')
#     shutil.move(tempfile.name, filename)

#updating2('Bibb Correctional Facility', street='565 Bibb Lane, Apt. #625')

#updating2('Bibb Correctional Facility', street='565 Bibb Lane')



# this function for making new entries to csv
# def newentry(arg1, **kwargs):
#     filename = 'customers10-Copy.csv'
#     #filename = 'customers10.csv'
#     fields = ['name', 'street', 'address', 'zip', 'website']
#     with codecs.open(filename, 'a', encoding='utf8') as csvfile:
#         writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
#         name = str(arg1)
#         street = ''
#         address = ''
#         zip = ''
#         website = ''
#         for key, value in kwargs.items():
#             if key == 'street':
#                 street = value
#             if key == 'address':
#                 address = value
#             if key == 'zip':
#                 zip = value
#             if key == 'website':
#                 website = value
#         row = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
#         writer.writerow(row)
#         print('Done! Alh')


def finding(input):
    f = open('customers10.csv', 'rt') #also #filename = 'customers10-Copy.csv'
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

# def WindowExists(classname):
#     try:
#         win32ui.FindWindow(classname, None)
#     except win32ui.error:
#         return False
#     else:
#         return True


# def finding(fn, ln):
#     for window in ahk.windows():
#         if b'Search for Customer' == window.title:
#             custfind = ahk.find_window(title=window.title)
#             custfind.close()
#         if b'Mailware' in window.title:
#             mailware = ahk.find_window(title=window.title)
#             mailware.activate()
#     # try:
#     #     custfind.activate()
#     # except NameError:
#     #     mailware.activate()
#     # mailware.activate()
#     # keyboard.send('esc')
#     keyboard.send('f4')
#     time.sleep(1)
#     keyboard.send('alt+f')
#     keyboard.write(fn.strip())
#     keyboard.send('tab')
#     keyboard.write(ln.strip())
#     time.sleep(1)
#     keyboard.send('enter')


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
# this function finds data from CSV based on facility, so facility's address info
# def fieldentry(facility):
#     #f = open('customers10.csv', 'rt')
#     f = open('customers10-Copy.csv', 'rt')
#     csv_reader = csv.DictReader(f, escapechar='\\')
#     for row in csv_reader:
#         if facility in row['name']: # >>>>>>>>>>>>>>>>> need to update this logic, add 2nd check
#             n = row['name']         # like matching state as well as facility !! <<<<--- 09/10/21
#             str = row['street']
#             str2 = row['street2']
#             zpp = row['zip']
#             break
#     f.close
#     print(row)
#     results = [n, str, str2, zpp]
#     return results

#this function finds data from CSV based on facility, so facility's address info
def fieldentry2(facility, state):
    #f = open('customers10.csv', 'rt')
    f = open('customers10-Copy.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    for row in csv_reader:
        if facility in row['name'] and state in row['address']: # >>>>>>>>>>>>>>>>> need to update this logic, add 2nd check
            n = row['name']         # like matching state as well as facility !! <<<<--- 09/10/21
            strt = row['street']
            zpp = row['zip']
            if row['street2'] is not None and len(row['street2']) > 1:
                strt2 = row['street2'], #need to add this also, 12/01/21, done on 12/09/21
                results = [n.strip(), strt.strip(), str(strt2).strip(), zpp.strip()]
            else:
                results = [n.strip(), strt.strip(), zpp.strip()]
            break
    f.close
    print(row)
    # if row['street2'] is not None and len(row['street2']) > 1:
    #     # 01/28/22: fix the below, the str casting of str2, looks like a tuple inside mailware
    #     results = [n.strip(), strt.strip(), str(strt2).strip(), zpp.strip()] #add str2 to this array <<< 12/01/21, then continue tracing where else code needs to be updated
    # else:
    #     results = [n.strip(), strt.strip(), zpp.strip()]
    return results

# finish here!!!


def lencheck(fac, fn, ln, inm):
    #print(len(fn))
    for ele in fac:
        assert (len(ele) <= 40), "Facility name is too long; 40 char limit."
    assert (len(fn) <= 15), "Check inmate's first name: will be truncated if longer than 15 characters."
    assert (len(ln+' #'+str(inm)) <= 20), "Check inmate's last name + number: will be truncated if longer than 20 characters."
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
    Channergy()
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
    #if isinstance(fac[2], str):
    if len(fac) == 4:
        keyboard.write(fac[2])  # street address 2
        keyboard.send('tab')
        keyboard.send('tab')
        str_zip = str(fac[3])
        zip_zero = str_zip.zfill(5)
        keyboard.write(zip_zero)  # zip code
        # time.sleep(1)
        keyboard.send('tab')
        keyboard.send('tab')
    else:
        keyboard.send('tab')
        keyboard.send('tab')
        str_zip = str(fac[2])
        zip_zero = str_zip.zfill(5)
        keyboard.write(zip_zero)  # zip code
        # time.sleep(1)
        keyboard.send('tab')
        keyboard.send('tab')
    # if fac[3] == 85132:
    #     keyboard.write(fac[3])  # zip code
    #     keyboard.send('tab')
    #     #time.sleep(2)
    #     #keyboard.write('Florence') # because this ZIP is bugged in mailware, adding "Florence" and AZ manually
    #     keyboard.write('Florence', 1) # 09/30/21: still doesn't work, mailware wont let auto add in this case..stupid zip
    #     keyboard.send('tab')
    #     keyboard.write('AZ')
    #else:


        #ib.activate() # this if want to refocus back to pycharm
    # str_zip = str(fac[2])
    # zip_zero = str_zip.zfill(5)
    # keyboard.write(zip_zero)  # zip code
    # # time.sleep(1)
    # keyboard.send('tab')
    # keyboard.send('tab')
    # # 10/08/21: updated above, now also picks up on 0's in updating addr zip
    # # keyboard.write(fac[2])  # zip code
    # # #time.sleep(1)
    # # keyboard.send('tab')
    # # keyboard.send('tab')
    # # #ib.activate() # this if want to refocus back to pycharm



# 10/26/21: solution for PA state facilities>> keep two entries for all PA facs, one for bill-to
# and other for ship-to, when input request comes for any PA state fac, then take all info
# from those two entries (need to correlate positioning of cursor with respect to ship-to too



def mailwarefocus(fac, fn, ln, inm):
    Channergy()
    keyboard.send('f4')
    keyboard.send('esc')
    keyboard.send('alt+n') #this entry puts cursor at first name of new customer form
    #keyboard.send('alt+c') #this entry takes program to current customer
    keyboard.write(fn.capitalize())
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(ln.capitalize()+' '+'#'+inm)
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(fac[0])  # prison name
    keyboard.send('tab')
    keyboard.write(fac[1])  # street address
    keyboard.send('tab')
    #if isinstance(fac[2], str):
    if len(fac) == 4:
        keyboard.write(fac[2])  # street address 2
        keyboard.send('tab')
        keyboard.send('tab')
        str_zip = str(fac[3])
        zip_zero = str_zip.zfill(5)
        keyboard.write(zip_zero)  # zip code
        # time.sleep(1)
        keyboard.send('tab')
        keyboard.send('tab')
    else:
        keyboard.send('tab')
        keyboard.send('tab')
        str_zip = str(fac[2])
        zip_zero = str_zip.zfill(5)
        keyboard.write(zip_zero)  # zip code
        # time.sleep(1)
        keyboard.send('tab')
        keyboard.send('tab')


    # if len(fac[2]) > 0:
    #     keyboard.write(fac[2])  # street address, line 2, needs to be added everywhere required, 12/01/21, done 12/09/21
    # keyboard.send('tab')
    # keyboard.send('tab')
    # if fac[3] == 85132:
    #     keyboard.write(fac[3])  # zip code
    #     keyboard.send('tab')
    #     time.sleep(2)
    #     #keyboard.write('Florence') # because this ZIP is bugged in mailware, adding "Florence" and AZ manually
    #     keyboard.write('Florence', 2) # 09/30/21: still doesn't work, mailware wont let auto add in this case..stupid zip
    #     keyboard.send('tab')
    #     keyboard.write('AZ')
    # else:
    #     str_zip = str(fac[3]) #12/09/21: edited to fac[3], should now reference zip code
    #     zip_zero = str_zip.zfill(5)
    #     keyboard.write(zip_zero)  # zip code
    #     #time.sleep(1)
    #     keyboard.send('tab')
    #     keyboard.send('tab')
    #     #ib.activate() # this if want to refocus back to pycharm

# now zipcodes will always have 5 digits minimum (problem when dealing with states beginning with 0
# str_inm_num = str(values['inm'])
# tx_zerofilled = str_inm_num.zfill(8)
# pyperclip.copy(tx_zerofilled)



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
myDict = {}
def statesfac():
    # below will create dictionary that to populate two combo boxes
    for s in states0:
        #f = open('customers10.csv', 'rt')
        f = open('customers10-Copy.csv', 'rt')
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
        # print("done: "+s)

    # print(myDict['AZ'])
# now run first instance of this func to populate combo boxes, can run again later if it csv updated within program
statesfac()
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
# def testeree():
#     print("ok here is good")



options = {
    "font": ('Helvetica', 16),
    "size": (25, 5),
    "readonly": True,
    "enable_events": True,
    #"element_justification": 'center'
}

options2 = {
    "font": ('Helvetica', 16),
    "size": (45, 5),
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
fn = sg.Input(key='fn', tooltip='Enter inmate first name here = ', size=(30,1), justification='center')
ln = sg.Input(key='ln', tooltip='Enter inmate last name here = ', size=(30,1), justification='center')
inm = sg.Input(key='inm', tooltip='Enter inmate number here =: ', size=(30,1), justification='center')
# , justification='left'


# arrangement of buttons:
# check info online
# check inmate name in mailware
# update account in mailware
# create inmate account
# quit
# clear all data

"""
search
find
updateinfo
x
y
z
"""


# these are buttons
x = sg.Button('Create Inmate Account', key="Create")
y = sg.Button('Quit')
z = sg.Button('Clear All Data')
xyz = sg.Button('Need to create or update facility info?')
search = sg.Button('Check Info Online')
find_channergy = sg.Button('Locate inmate in Channergy')
updateinfo = sg.Button('Update Address in Channergy')
newfac = sg.Button('Add New Facility to CSV - Admin Only')
find = sg.Button('Find Inmate in JPay')
restart = sg.Button('Restart Program')


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
    [sg.Combo((),                 **options2, key="subproject", tooltip='Select state above first, then facility.')],
    #[fin],
    [search],
    [find_channergy],
    [find],
    [updateinfo],
    [x],
    [y],
    [z],
    #[restart]
]

# 2/16/22: add a 2nd inmate number field, make it optional to add into mailware

window = sg.Window('Inmate Account Creation', layout, use_ttk_buttons=True, finalize=True, resizable=True)

#window2 = sg.Window('Updating/Creating New Facility', layout2, use_ttk_buttons=True, finalize=True)

while True:
    event, values = window.read()
    ready = False
    if event in (sg.WINDOW_CLOSED, 'Quit'):
        break

    # if event and (values['fn'] == '' or values['ln'] == '' or values['inm'] == ''):
    #     print('this may work')
    #     sg.popup("Please input first and last name.", title="Error")
    #     continue # 09/08/22: add logic of what happens if certain buttons pressed and fields missing
    # elif event == 'Restart Program': #---10/20/21: doesnt work yet, trying to restart itself
    #     os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    elif event == "mainproject":
        # testeree()
        lst = sorted(myDict[values[event]])
        window['subproject'].Update(value=lst[0], values=lst)
        ready = True
    elif event == 'Locate inmate in Channergy':
        first_name = (values['fn']).strip()
        last_name = (values['ln']).strip()
        Channergy()
        # (ahk.win_get(title='Channergy 2021 Client/Server')).activate()
        time.sleep(0.25)
        keyboard.send('f4')
        keyboard.send('alt+f')
        keyboard.write(first_name)  # inmate first name
        keyboard.send('tab')
        keyboard.write(last_name)
        time.sleep(0.5)
        keyboard.send('alt+s')
        continue
    elif event == 'Find Inmate in JPay': #need to make sure that this part throws popup if no inmate ID present, 3/9/22
        # inmjpay = (values['inm']).strip --- 3/11/22: doesn't work yet
        #url_jpay = 'https://www.google.com/search?q=' + values['mainproject'] + ' inmate locator'
        inm = values['inm'].strip()
        url_jpay = 'https://www.jpay.com/SearchResult.aspx?searchText='+inm+'&searchState='+values['mainproject']+'&returnUrl=InmateInfo.aspx'
        webbrowser.open(url_jpay, new=0, autoraise=True)

    elif event == 'Create':
        try: #below is where 2 instances of fieldentry being changed for testing fieldentry2
            #lencheck(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            lencheck(fieldentry2(values['subproject'], values['mainproject']), values['fn'], values['ln'], values['inm'])
        except AssertionError:
            sg.popup("Length of one or more fields is too long, will be truncated by Mailware - verify account info!")
            #mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            mailwarefocus(fieldentry2(values['subproject'], values['mainproject']), values['fn'], values['ln'], str(values['inm']).upper())
            continue
        #mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
        if values['fn'] == '' or values['ln'] == '' or values['inm'] == '' or values['subproject'] == '':
            sg.popup("Please select state and enter complete info for all fields.", title="Error")
            #window['fn'].update('')
            #window['ln'].update('')
            #window['inm'].update('')
            continue
        try:
            #mailwarefocus(fieldentry(values['subproject']), values['fn'], values['ln'], values['inm'])
            # if values['mainproject'] == 'TX': ----> 3/21/22: if ever need to have inmate numbers be precise count, then add state/etc here, yc
            #     str_inm_num = str((values['inm']).strip())
            #     tx_zerofilled = str_inm_num.zfill(8)
            #     pyperclip.copy(tx_zerofilled)
            # elif values['mainproject'] == 'AR':
            #     str_inm_num = str((values['inm']).strip())
            #     ar_zerofilled = str_inm_num.zfill(6)
            #     pyperclip.copy(ar_zerofilled)
            #
            # else:
            #     pyperclip.copy(str((values['inm']).upper()).strip())
            mailwarefocus(fieldentry2(values['subproject'], values['mainproject']), values['fn'], values['ln'], str(values['inm']).upper())
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
        keyboard.send('tab')
    if event == 'Check Info Online':
        url = 'https://www.google.com/search?q=' + values['mainproject'] + ' inmate locator'
        # 02/07/22: below now works alh
        vinelinks = ['LA', 'MA', 'AK']
        if (values['mainproject'] in vinelinks):
            url = 'https://www.google.com/search?q=' + values['mainproject'] + ' vinelink inmate'
        if values['inm'] == '' or values['mainproject'] == '':
            sg.popup("Please enter inmate number and state to search that DOC.", title="Error")
            #window['fn'].update('')
            #window['ln'].update('')
            #window['inm'].update('')
            continue
        else:
            if values['mainproject'] == 'TX':
                str_inm_num = str((values['inm']).strip())
                tx_zerofilled = str_inm_num.zfill(8)
                pyperclip.copy(tx_zerofilled)
            elif values['mainproject'] == 'AR':
                str_inm_num = str((values['inm']).strip())
                ar_zerofilled = str_inm_num.zfill(6)
                pyperclip.copy(ar_zerofilled)

            else:
                pyperclip.copy(str((values['inm']).upper()).strip())
            # original location of url value, 02/07/22, ---- now done alh
        webbrowser.open(url, new=0, autoraise=True)
    if event == 'Update Address in Channergy':
        #mailwareupdate(fieldentry(values['subproject']))
        mailwareupdate(fieldentry2(values['subproject'], values['mainproject']))
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