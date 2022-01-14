import pandas as pd
import csv
from timeit import timeit
import PySimpleGUI as sg
import re

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
          'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
          'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

def wru(selected):
    state = re.search('^[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s(\d{5})', addresses).groupdict()['state']
    responses = []
    if selected == state:
        responses.append(names[addresses.index(state)])
    

f = open('customers10.csv', 'rt')
csv_reader = csv.DictReader(f, escapechar='\\')
#q = input("what name?")
q = 'bibb'

names = []
addresses = []
zips = []
streets = []
websites = []

for row in csv_reader:
    #print(row['name'])
    names.append(row['name'])
    addresses.append(row['address'])
    zips.append(row['zip'])
    streets.append(row['street'])
    websites.append(row['website'])
    #print(row['name'])
    #if q.title() in row['name']:
        #print(row)
    
    #f.close

"""
this is what needs to do:
1) dropdown list of all states
2) when a state is selected, then regex match occurs checking the address column where search = selected state
3) 

"""


for e in names:
    print(e)



sg.theme("DarkBlue")

items = ['USA', 'Mexico', 'Japan', 'Korea', 'UK', 'China', 'France']
asia_index = (2 ,3, 5)





layout = [
    [sg.Listbox(states, size=(10, 5), key='-LISTBOX1-', enable_events=True)],
    [sg.Listbox(names, size=(50, 20), key='-LISTBOX-', enable_events=True)]
]

# Create a binding on the listbox onclick
#facility_list.bind("<<ListboxSelect>>", fillout)

window = sg.Window('Title', layout, finalize=True)
listbox = window['-LISTBOX-'].Widget
listbox2 = window['-LISTBOX1-'].Widget
for index in asia_index:
    listbox.itemconfigure(index, bg='green', fg='white')    # set options for item in listbox
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == '-LISTBOX-':
        print(values['-LISTBOX-'])
    #print(event, values)
    #sg.popup_get_text('This is {}'.format(values['-LISTBOX-'][0]))
    if event == '-LISTBOX1-':
        print(values['-LISTBOX1-'])
        
        

        

window.close()

#t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
#t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
#t.timeit()


"""
stt = 'Maryland'

if stt in states:
    print(states[stt])

keys = [k for k, v in states.items() if v == 'Maryland']
print(keys)

keyer = states.get('MD')
print(keyer)

"""

























