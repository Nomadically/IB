import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import PySimpleGUI as psg

f = open('customers10.csv', 'rt')
csv_reader = csv.DictReader(f, escapechar='\\')
#q = input("what name?")
check = 'bibb'
names = []
addresses = []
zips = []
streets = []
websites = []

for row in csv_reader:
    names.append(row['name'])
    addresses.append(row['address'])
    zips.append(row['zip'])
    streets.append(row['street'])
    websites.append(row['website'])

def find1(check):
    for row in csv_reader:
        #print(row['name'])
        names.append(row['name'])
        addresses.append(row['address'])
        zips.append(row['zip'])
        streets.append(row['street'])
        websites.append(row['website'])
        if check.title() in row['name']:
            print(row)
            print(row['name'])
            print(row['street'])
            print(row['zip'])
            print(row['website'])
            return row['name']

# set the theme for the screen/window
psg.theme('SandyBeach')
# define layout
layout = [[psg.Text('Choose Boarding place', size=(20, 1), font='Lucida', justification='left')],
          [psg.Combo(['New York', 'Chicago', 'Washington', 'Colorado', 'Ohio', 'San Jose', 'Fresno', 'San Fransisco'],
                     default_value='Utah', key='board')],
          [psg.Text('Choose Destination ', size=(30, 1), font='Lucida', justification='left')],
          [psg.Combo(['New York', 'Chicago', 'Washington', 'Colorado', 'Ohio', 'San Jose', 'Fresno', 'San Fransisco'],
                     key='dest')],
          [psg.Text('Choose additional Facilities', size=(30, 1), font='Lucida', justification='left')],
          [psg.Listbox(values=[names],
                       select_mode='extended', key='fac', size=(30, 6))],
          [psg.Button('SAVE', font=('Times New Roman', 12)), psg.Button('CANCEL', font=('Times New Roman', 12))]]
# Define Window
win = psg.Window('Customise your Journey', layout)
# Read  values entered by user
e, v = win.read()
# close first window
win.close()
# access the selected value in the list box and add them to a string
strx = ""
for val in v['fac']:
    strx = strx + " " + val + ","

# display string in a popup
psg.popup('Options Chosen',
          'You will Travel from :' + v['board'] + ' to ' + v['dest'] + ' \nYour additional facilities are:' + strx[
                                                                                                              1:len(
                                                                                                                  strx) - 1])

df = pd.read_csv('customers10.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = names


print(names)

#print(names[0])
print("we are here")

test = 'bibb'
teststr = test.title()

for name in names:
    if teststr in name:
        print(name)
        #index = names.index(name)
        #print(index)

def finder(input):
    input = input.title()
    status = False
    for name in names:
        if input in name:
            try:
                print(name)
                print("found!")
                #print(locate)
                #print(names[locate])
                #print(streets[locate])
                #print(addresses[locate])
                #print(zips[locate])
                status = True
                return name
            except ValueError:
                print("not found")

#print(zips)

"""

with open('../yc startup programs/testable.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        #keep going
        if (userinput in row[0] and userinput2 in row[2]):
            print("here!")
            #print(row[0]) #corresponds to facility name
            #print(row[1]) # " to street
            #print(row[2]) # " to zip code
            win2 = ahk.find_window(title=b'Mailware 2014 - IslamicBookstore.com - [Customer]')  # Find the opened window
            win2.activate()  # this will shift focus to it
            keyboard.send('alt+n')
            keyboard.send('alt+c')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(row[0])  # prison name
            keyboard.send('tab')
            keyboard.write(row[1])  # street address
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.send('tab')
            keyboard.write(row[2])  # zip code
            keyboard.send('tab')
            keyboard.send('tab')


    for window in ahk.windows():
        #print(window.title) #this will list names of open windows
        if b'Mailware' in window.title:
            mailware = ahk.find_window(title=window.title)
        mailware.activate()


"""