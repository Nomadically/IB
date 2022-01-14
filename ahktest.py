import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK
from ahk.window import Window
import keyboard
import webbrowser
import time
import pandas as pd
import csv
import pyautogui
import subprocess
import win32ui


ahk = AHK()


#win = ahk.active_window                        # Get the active window
#win = ahk.win_get(title='Untitled - Notepad')  # by title
#win = list(ahk.windows())                      # list of all windows
#print(win)


#win = Window(ahk, ahk_id='0xabc123')           # by ahk_id
#win = Window.from_mouse_position(ahk)          # the window under the mouse cursor
#win = Window.from_pid('20366')                 # by process ID

#for window in ahk.windows():
#print(window.title)

# Some more attributes
#print(window.class)
#print(window.text)
#print(window.rect)   # (x, y, width, height)
#print(window.id)     # ahk_id
#print(window.pid)
#print(window.process)

for window in ahk.windows():
    print(window.title)  # this will list names of open windows
    print("after this:")
    #print(window.class_name)  # this will list names of open class names
    if b'Inmate Account Creation' in window.title:
        ibprog = ahk.find_window(title=window.title)
    if b'Mailware' in window.title:
        mailware = ahk.find_window(title=window.title)
    if b'Notepad' in window.title:
        notepad = ahk.find_window(title=window.title)
    if b'Search for Customer' == window.title:
        custfind = ahk.find_window(title=window.title)
        #custfind.close()
    # if b'TMessageForm' in window.title:
    #     popupclose = ahk.find_window(title=window.title)
    #     popupclose.activate()
    #     keyboard.send('enter')
    #     ibprog.activate()







# try:
#     mailware.activate()
#     # keyboard.send('f4') -->this doesnt work yet
#     # keyboard.send('alt+f')
#     # keyboard.send('ctrl+c')
#     # keyboard.send('tab')
#     # keyboard.send('tab')
#     # keyboard.send('ctrl+v')
# except NameError:
#     print("Mailware is not up, need to fix")


# when running find_inmate, add continue after its called in while loop
def find_inmate(fn, ln, inm):
    try:
        mailware.activate()
    except NameError:
        sg.popup('Mailware not active, now starting program - please wait.')
        subprocess.call([r"C:\Program Files (x86)\Mailware 2014\Mailware.exe"])
    try:
        custfind.activate()
    except NameError:
        keyboard.send('f4')
    keyboard.send('alt+f')  # this puts cursor at first name in mailware
    keyboard.write(fn.title())
    keyboard.send('tab')
    keyboard.write(ln.title())
    keyboard.send('enter')
    keyboard.send('esc')
    return fn, ln, inm
    # after this, need to prompt user if inmate found or not - "No, not found, create account" and "Yes, found"

    # keyboard.send('ctrl+a')
    # keyboard.send('ctrl+a')
# this is name of that shazam print window >>>>

"""
b'Shazam Report Wizard: \\\\paradise\\mailware2013\\data\\Reports\\A - Inmate Standard Letter.srw'

"""


prisonInfo = {'MD': {'PrisonName':['Street Here', '12345']},
          'NY': {"Prison2Name":['Street2 Here', '67891']}}

people = {'MD': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'NY': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#theme_firstname_list = sg.theme_list()
#print(theme_firstname_list)

print("ok here 12121211212")



# 09/13/21: as of now, below works to put first and last names in mailware and search
def terry(fn, ln):
    # for window in ahk.windows():
    #     if b'Search for Customer' == window.title:
    #         custfind = ahk.find_window(title=window.title)
    #         custfind.close()
    #     if b'Mailware' in window.title:
    #         mailware = ahk.find_window(title=window.title)
    #         mailware.activate()
    try:
        custfind.activate()
    except NameError:
        mailware.activate()
    keyboard.send('f4')
    time.sleep(1)
    keyboard.send('alt+f')
    keyboard.write(fn)
    keyboard.send('tab')
    keyboard.write(ln)
    time.sleep(1)
    keyboard.send('enter')

#terry('test', 'dude')

#mailware.activate()
#===============================================================================
# # Create a list of prisons
# df = pd.read_csv('customers9.csv')
# names = df.name
# streets = df.street
# addresses = df.address
# zips = df.zip
# websites = df.website
# prisons = names
#===============================================================================


# Define the window's contents

#===============================================================================
# layout = [  [sg.Text('Enter First Name:'), sg.Input()],
#             [sg.Text('Enter Last Name:'), sg.Input()],
#             [sg.Text('Enter Inmate Number:'), sg.Input()],
#             [sg.Text('Row 3'), sg.Button('Ok')] ]
#===============================================================================



#===============================================================================
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
#===============================================================================

#q = input("what info first?")
#q2 = input("what info second?")
#q3 = input("what inmate num")

#find_inmate(q, q2, q3)

#custfind.activate()
#mailware.activate()
#mailware.maximize()

"""

keyboard.send('f3')

currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
print(currentMouseX, currentMouseY)
pyautogui.moveTo(264, 158)

pyautogui.move(0, 20)
pyautogui.doubleClick()
keyboard.send('escape')
pyautogui.keyDown('Home')
pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down'])
keyboard.press('shift')
pyautogui.typewrite(['left','left','left','left','left'])
keyboard.release('shift')
#keyboard.press('shift')
#keyboard.send('right+right+right+right+right+right')
#keyboard.release('shift')
#pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
keyboard.send('ctrl+c')
#keyboard.send('left')
#keyboard.press('shift')
#notepad.activate()
#keyboard.write('now this is customer number: ')
#pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

"""






#keyboard.send('right')

#keyboard.release('shift')
#keyboard.send('ctrl+c')

#keyboard.send('home')
#keyboard.send('shift+right+right+right')
#keyboard.send('ctrl+c')


def tester(fn, ln, num, fac):
    #win = list(ahk.windows())
    #print(win)
    ahk.run_script('Run Notepad') # Open notepad
    time.sleep(1)
    for window in ahk.windows():
        print(window.title) #this will list names of open windows
        if b'Firefox' in window.title: # >>>> now we can shift focus to this app at any point
            browser = ahk.find_window(title=window.title)  # Find the opened window
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
    keyboard.write('This is the info: '+fn+' '+ln+' '+num+' '+fac)

theme_name_list = sg.theme_list()
print(theme_name_list)