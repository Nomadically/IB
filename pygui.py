import PySimpleGUI as sg
from tkinter import ttk
from ahk import AHK, Hotkey
import keyboard
import webbrowser
import time
import pandas as pd
import csv



ahk = AHK()
sg.theme('DarkAmber')

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

# Create a list of prisons
df = pd.read_csv('customers9.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = names



def finder(input):
    for name in names:
        if input in name:
            try:
                locate = name.index(name)
                print("found!")
                print(locate)
                print(names[locate])
                print(streets[locate])
                print(addresses[locate])
                print(zips[locate])
            except ValueError:
                print("not found")

print(names)        