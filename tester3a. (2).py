from ahk import AHK, Hotkey
import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import time
import tkinter.messagebox
import keyboard


ahk = AHK()
prisonInfo = {'MD': {'PrisonName':['Street Here', '12345']},
          'NY': {"Prison2Name":['Street2 Here', '67891']}}

people = {'MD': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'NY': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

print(people)
print(prisonInfo['NY']['Prison2Name'])

#val = input("state?")
#val2 = input("prison?")

people1 = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for st, prison in prisonInfo.items():
    print("\nState:", st)
    for key in prison:
        print(key + ':', prison[key])

def tester():
    win = list(ahk.windows())
    print(win)
    for window in ahk.windows():
        print(window.title) #this will list names of open windows
    ahk.run_script('Run Notepad') # Open notepad
    win = ahk.find_window(title=b'Untitled - Notepad')  # Find the opened window
    win.activate()
    #ahk.type("this is a test run")
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    keyboard.write(prisonInfo[state][prison][0]) #this enters street addr
    #keyboard.write(prisonInfo[state][prison][1]) #this enters zip code
    #now entering info into mailware 
    """
    win2 = ahk.find_window(title=b'Mailware 2014 - IslamicBookstore.com - [Customer]')  # Find the opened window
    win2.activate() #this will shift focus to it
    keyboard.send('alt+n')
    keyboard.send('alt+c')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(prison) #prison name
    keyboard.send('tab')
    keyboard.write(prisonInfo[state][prison][0]) #street address
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.send('tab')
    keyboard.write(prisonInfo[state][prison][1]) #zip code
    keyboard.send('tab')
    keyboard.send('tab')
    """
    # keyboard.send('alt+f')
    #keyboard.send('alt+f')
    #ahk.type(prisonInfo[state][prison]) 
    #ahk.key_press('Alt')
    #ahk.key_press('F')
    #win = ahk.find_window(title=b'Gmail - thinkingdrops - Mozilla Thunderbird') # Find the opened window
    #win.activate()           # Give the window focus
    



    
def keys_exists(element, *keys):
    '''
    Check if *keys (nested) exists in `element` (dict).
    '''
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True

state = input("state?")
prison = input("prison?")

#print(keys_exists(prisonInfo, "MD", "Prison2"))

if keys_exists(prisonInfo, state, prison) == True:
    tester()
else:
    print("no bueno")    



    
"""
for p_id, p_info in people1.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])
"""



#if val in States:
    #print("cool")
    #print(States[val][val2])

"""
if val2 in States:
    print("okey coolier")
else:
    print("what is dis")
    """

"""
val = input("Enter your value: ")
print(val)

if val in States:
    print("Excellent")
    val2 = input("enter prison name?")
    if val2 in States[val]:
        print(States[val[val2]])
    else:
        print("sorry not good enough")
else:
    print("sorry dude")
"""