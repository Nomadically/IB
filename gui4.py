import PySimpleGUI as psg
import pandas as pd
#set the theme for the screen/window
psg.theme('SandyBeach')

df = pd.read_csv('customers9.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = names

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
print(states[0])
#define layout
layout=[[psg.Text('Choose Boarding place',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(['New York','Chicago','Washington', 'Colorado','Ohio','San Jose','Fresno','San Fransisco'],default_value='Utah',key='board')],
        #[psg.Listbox(values=[states],key='states', size=(30, 6))],
        [psg.Text('Choose Destination ',size=(30, 1), font='Lucida',justification='left')],
        [psg.Combo(['New York','Chicago','Washington', 'Colorado','Ohio','San Jose','Fresno','San Fransisco'],key='dest')],
        [psg.Text('Choose additional Facilities',size=(30, 1), font='Lucida',justification='left')],
        [psg.Listbox(values=['Welcome Drink', 'Extra Cushions', 'Organic Diet','Blanket', 'Neck Rest'], select_mode='extended', key='fac', size=(30, 6))],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
#Define Window
win =psg.Window('Customise your Journey',layout)
#Read  values entered by user
e,v=win.read()
#close first window
win.close()
#access the selected value in the list box and add them to a string
strx=""
for val in v['fac']:
    strx=strx+ " "+ val+","
        
#display string in a popup         
psg.popup('Options Chosen',      
            'You will Travel from :'+ v['board'] + ' to '+v['dest'] +' \nYour additional facilities are:' +strx[1:len(strx)-1] )