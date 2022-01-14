import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import codecs

ahk = AHK()
sg.theme('DarkAmber')

prisonInfo = {'MD': {'PrisonName': ['Street Here', '12345']},
              'NY': {"Prison2Name": ['Street2 Here', '67891']}}

people = {'MD': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'NY': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


# theme_firstname_list = sg.theme_list()
# print(theme_firstname_list)

# ===============================================================================
# # Create a list of prisons
# df = pd.read_csv('customers9.csv')
# names = df.name
# streets = df.street
# addresses = df.address
# zips = df.zip
# websites = df.website
# prisons = names
# ===============================================================================


# Define the window's contents

# ===============================================================================
# layout = [  [sg.Text('Enter First Name:'), sg.Input()],
#             [sg.Text('Enter Last Name:'), sg.Input()],
#             [sg.Text('Enter Inmate Number:'), sg.Input()],
#             [sg.Text('Row 3'), sg.Button('Ok')] ]
# ===============================================================================


# ===============================================================================
# def finder(input):
#     for name in names:
#         if input.title() in name:
#             try:
#                 #locate = names.index(name)
#                 print(name)
#                 print("found!")
#                 #print(locate)
#                 #print(names[locate])
#                 #print(streets[locate])
#                 #print(addresses[locate])
#                 #print(zips[locate])
#                 #return locate
#                 return name
#             except ValueError:
#                 print("not found")
#                 return None
# ===============================================================================

def finding(input):
    f = open('customers11.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    # check = 'bibb'
    for row in csv_reader:
        # print(row['name'])
        # names.append(row['name'])
        # addresses.append(row['address'])
        # zips.append(row['zip'])
        # streets.append(row['street'])
        # websites.append(row['website'])
        if input.title() in row['name']:
            print(row['name'])
            print(row['address'])
            print(row['street'])
            print(row['zip'])
            return row['name']
    f.close


def tester(fn, ln, num, fac):
    # win = list(ahk.windows())
    # print(win)
    ahk.run_script('Run Notepad')  # Open notepad
    # time.sleep(1)
    for window in ahk.windows():
        # print(window.title) #this will list names of open windows
        if b'Firefox' in window.title:  # >>>> now we can shift focus to this app at any point
            browser = ahk.find_window(title=window.title)  # Find the opened window
        if b'WordPad' in window.title:
            wordpad = ahk.find_window(title=window.title)
        if b'Notepad' in window.title:
            notepad = ahk.find_window(title=window.title)
    # time.sleep(1)
    notepad.activate()
    # ahk.type("this is a test run")
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    keyboard.write('\nok dude street here')  # this enters street addr
    # browser.activate()
    # time.sleep(3)
    # notepad.activate()
    keyboard.write('This is the info: ' + fn + ' ' + ln + ' ' + num + ' ' + fac)


a = sg.Text("inmate's first name =")
b = sg.Text("inmate's last name =")
c = sg.Text("inmate's number =")
z1 = sg.Text("name of facility =")
d = sg.Text(size=(40, 1), key='OUTPUT')

a1 = sg.Input(key='firstname', tooltip='< Inmate first name here >')
b1 = sg.Input(key='lastname', tooltip='< Inmate last name here >')
c1 = sg.Input(key='inmatenum', tooltip='< Inmate number here >')
z = sg.Input(key='fac', tooltip='< Facility name here >')

x = sg.Button('Submit')
y = sg.Button('Quit')

z = sg.Input(key='fac', tooltip='< Facility name here >')

layout = [[a, a1],
          [b, b1],
          [c, c1],
          [z1, z],
          [d],
          [x, y]]

# Create the window
window = sg.Window('Inmate Account Search and Creation', layout, use_ttk_buttons=True)


# ===============================================================================
# 
# # Display and interact with the Window using an Event Loop
# while True:
#     event, values = window.read()
#     # See if user wants to quit or window was closed
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     if event == 'Submit':
#         #printering('pressed this: '+values['firstname']+" "+values['lastname']+" "+values['inmatenum']+".")
#         if finding(values['fac']) != None:
#                    tester(values['firstname'], values['lastname'], values['inmatenum'], finding(values['fac']))
#                    finding(values['fac'])
#         else:
#             sg.popup('Please enter facility name again, '+values['fac']+' not found in database.')
#             continue
#     # Output a message to the window
#     window['OUTPUT'].update('Hello ' + values['firstname'] +values['lastname']+values['inmatenum']+ "! Thanks for trying PySimpleGUI",
#                               text_color='yellow')
# 
# # Finish up by removing from the screen
# window.close()
# ===============================================================================


# below function takes inputs and puts them into mailware
def fieldentry(fac):
    f = open('customers11.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    for row in csv_reader:
        if fac in row['name']:
            print(row)
            break
    return row


y = fieldentry('Bibb')

print(y['name'])


# def lencheck(fn):
# print(len(fn))

# lencheck('joe #3')


def lencheck(fn, ln, inm):
    # print(len(fn))
    assert (len(fn) <= 15), "Check inmate's first name: will be truncated if longer than 15 characters."
    assert (
                len(ln + ' #' + inm) <= 20), "Check inmate's last name + number: will be truncated if longer than 20 characters."
    print(fn, ln, inm)
    return fn, ln, inm


# ===============================================================================
# try:
#     lencheck('joe', 'ok', '1233333333333333333333333333333333333333')
# except Exception:
#     print("sorry this doesn't work")
# ===============================================================================
try:
    lencheck('joe', 'ok', '123')
except AssertionError:
    print("Careful with inmate information - some part may be too long and thus shorted by Mailware.")

# this function has to be able to accept any number of arguments, we need to 
# know what old data/location is, and what is to replace it


"""
def updating(**kwargs):
        with codecs.open("customers15.csv", encoding='utf-8', mode='w') as f:
            fieldnames = ['name', 'street', 'address', 'zip', 'website']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            #writer.writerow({'name': a, 'street': b, 'address': c, 'zip': d, 'website': row[0]})
            #print("done this one: "+row[0])
            for key, value in kwargs.items():
                if 'name' == row[key]:
                    writer.writerow({'name': value})
                    print("done:"+key+value)
                if 'street' == row[key]:
                    writer.writerow({'street': value})
                    print("done: "+key+value)
                    #print(row['address'])
                    #print(row['street'])
                    #print(row['zip'])
"""

# updating(old_name="Test Facility", new_name="Test Facility 2")
# updating(name="Bibb CF", street="121212 test st.")
