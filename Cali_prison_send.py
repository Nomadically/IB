# import PySimpleGUI as sg
#
# """
#     Demo - Element List
#
#     All 34 elements shown in 1 window as simply as possible.
#
#     Copyright 2022 PySimpleGUI
# """
#
# use_custom_titlebar = False
#
# def make_window(theme=None):
#     NAME_SIZE = 23
#
#     def name(name):
#         dots = NAME_SIZE-len(name)-2
#         return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')
#
#     sg.theme(theme)
#
#     treedata = sg.TreeData()
#
#     treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
#     treedata.Insert("", '_B_', 'B', [])
#     treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )
#
#     layout_l = [[name('Text'), sg.Text('Text')],
#                 [name('Input'), sg.Input(s=15)],
#                 [name('Multiline'), sg.Multiline(s=(15,2))],
#                 [name('Output'), sg.Output(s=(15,2))],
#                 [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
#                 [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
#                 [name('Checkbox'), sg.Checkbox('Checkbox')],
#                 [name('Radio'), sg.Radio('Radio', 1)],
#                 [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
#                 [name('Button'), sg.Button('Button')],
#                 [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
#                 [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
#                 [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
#                 [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
#                 [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]
#
#     layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,50))],
#                 [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
#                 [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
#                 [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
#                 [name('Horizontal Separator'), sg.HSep()],
#                 [name('Vertical Separator'), sg.VSep()],
#                 [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
#                 [name('Column'), sg.Column([[sg.T(s=15)]])],
#                 [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
#                 [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
#                 [name('Push'), sg.Push(), sg.T('Pushed over')],
#                 [name('VPush'), sg.VPush()],
#                 [name('Sizer'), sg.Sizer(1,1)],
#                 [name('StatusBar'), sg.StatusBar('StatusBar')],
#                 [name('Sizegrip'), sg.Sizegrip()]  ]
#
#     layout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
#               [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-')],
#               [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 18', justification='c', expand_x=True)],
#               [sg.Col(layout_l), sg.Col(layout_r)]]
#
#     window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)
#
#     window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
#     window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element
#
#     return window
#
# # Start of the program...
# window = make_window()
#
# while True:
#     event, values = window.read()
#     sg.popup(event, values)                     # show the results of the read in a popup Window
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     if values['-COMBO-'] != sg.theme():
#         sg.theme(values['-COMBO-'])
#         window.close()
#         window = make_window()
#     if event == '-USE CUSTOM TITLEBAR-':
#         use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
#         window.close()
#         window = make_window()
# window.close()


# --------------------------


import csv
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
import PySimpleGUI as sg
import keyboard
import pyperclip
from openpyxl import load_workbook

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.

prisons = {
    'Avenal State Prison': {'manifest': 'ref#', 'nameID': ''},
    'California City Correctional Facility': {'manifest': 'ref#', 'nameID': ''},
    'Calipatria State Prison': {'manifest': 'ref#', 'nameID': ''},
    'California Correctional Center': {'manifest': 'ref#', 'nameID': ''},
    'California Correctional Institution': {'manifest': 'ref#', 'nameID': ''},
    'California Correctional Women’s Facility': {'manifest': 'ref#', 'nameID': ''},
    'California State Prison, Centinela': {'manifest': 'ref#', 'nameID': ''},
    'California Health Care Facility': {'manifest': 'ref#', 'nameID': ''},
    'California Institution for Men': {'manifest': 'ref#', 'nameID': ''},
    'California Institution for Women': {'manifest': 'ref#', 'nameID': ''},
    'California Men’s Colony': {'manifest': 'ref#', 'nameID': ''},
    'California Medical Facility': {'manifest': 'ref#', 'nameID': ''},
    'California State Prison, Corcoran': {'manifest': 'ref#', 'nameID': ''},
    'California Rehabilitation Center': {'manifest': 'ref#', 'nameID': ''},
    'Correctional Training Facility': {'manifest': 'ref#', 'nameID': ''},
    'Chuckawalla Valley State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Folsom State Prison': {'manifest': 'ref#', 'nameID': ''},
    'High Desert State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Ironwood State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Kern Valley State Prison': {'manifest': 'ref#', 'nameID': ''},
    'California State Prison, Los Angeles County': {'manifest': 'ref#', 'nameID': ''},
    'Mule Creek State Prison': {'manifest': 'ref#', 'nameID': ''},
    'North Kern State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Pelican Bay State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Pleasant Valley State Prison': {'manifest': 'ref#', 'nameID': ''},
    'R. J. Donovan Correctional Facility': {'manifest': 'ref#', 'nameID': ''},
    'California State Prison, Sacramento': {'manifest': 'ref#', 'nameID': ''},
    'SATF California State Prison, Corcoran': {'manifest': 'ref#', 'nameID': ''},
    'Sierra Conservation Center': {'manifest': 'ref#', 'nameID': ''},
    'California State Prison, Solano': {'manifest': 'ref#', 'nameID': ''},
    'San Quentin State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Salinas Valley State Prison': {'manifest': 'ref#', 'nameID': ''},
    'Valley State Prison': {'manifest': 'ref#', 'nameID': ''}
}

options = {
    "font": ('Helvetica', 16),
    "size": (45, 5),
    "readonly": True,
    "enable_events": True,
    # "element_justification": 'center'
}

dat1 = sg.CalendarButton(button_text='Select From date:', target='date1', format='%m-%d-%Y', key='d1')
dat2 = sg.CalendarButton(button_text='Select To date:', target='date2', format='%m-%d-%Y', key='d2')

layout = [[sg.Text('Program to auto-compile/send California Manifests')],
          [sg.Text('Enter inmate names and IDs:')],
          [sg.Multiline(s=(25, 2))],
          [sg.Text('Enter manifest reference number:')],
          [sg.Multiline(s=(25, 2))],
          [dat1, sg.InputText('   ', key='date1', size=(10, 1), tooltip='<- Click button to choose first date.')],
          [dat2, sg.InputText('   ', key='date2', size=(10, 1), tooltip='<- Click button to choose second date.')],
          [sg.Combo(sorted(list(prisons.keys())), **options, key="mainproject",
                    tooltip='<-Choose facility, state prisons of California CDCR->')],
          [sg.Button('Process Prison')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Process Prison':
        with open('CAprisonsCSV.csv') as csv_file:
            # reading the csv file using1 DictReader
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if values['mainproject'] in row['prison']:
                    print(row['acronym'])
                    # myDict["niche"] = "programming"
                    inm_info = {values[0]: values[1]}
                    date1 = values['date1']
                    date2 = values['date2']
                    print('this is what this created dict looks like:')
                    print(inm_info)
                    print(date1)
                    print(date2)
                    wb = load_workbook(filename='Manifest-EmailTemplate.xlsx')
                    # worksheet = wb.get_sheet_by_name('Sheet1')
                    sheet1 = wb['Sheet1']
                    # worksheet['D3']='Whatever you want to put in D3'
                    sheet1['A2'] = values['mainproject']  # <<<--- facility name goes in here
                    sheet1['B5'] = 'From ' + date1 + ' to ' + date2  # <<<--- date ranges go in here
                    sheet1['B6'] = row['email']  # <<<--- email goes in here
                    sheet1['A11'] = values[1]  # <<<--- manifest #s goes in here
                    sheet1['B11'] = values[0]  # <<<--- inmates name/ID go in here
                    filename = 'Manifest-Email-' + row['acronym']
                    wb.save(filename + '.xlsx')
                    time.sleep(1)
                    date = date1 + '-' + date2
                    tbirdPath = r'E:\Program Files\Mozilla Thunderbird\thunderbird.exe'
                    to = 'ykchaudry@gmail.com'
                    cc = 'ykchaudry@gmail.com, ykchaudry@gmail.com'
                    p = Path(filename + ".xlsx").resolve()
                    print(p)
                    # attachment = r'C:\Users\think\Documents\progressQuestion.png'
                    attachment = p
                    subject = """Manifest Master List-IslamicBookstore.com,""" + date
                    body = ''
                    message = """asalaamu'alaikum (Peace be with you),

                    Greetings,

                    Please find attached the manifest master list for the package(s) being shipped this week.
                    
                    It is expected to arrive within 10 to 14 business days via USPS or FedEx.
                                       
                    IF YOU DO NOT RECEIVE THESE PACKAGES, PLEASE NOTIFY US AS SOON AS POSSIBLE.


                    If you have any questions or concerns, please let us know.

                    Thank you, 
                    """
                    pyperclip.copy(message)
                    composeCommand = 'format=html,to={}, cc={},subject={},body={},attachment={}'.format(to, cc, subject,
                                                                                                        body,
                                                                                                        attachment)
                    subprocess.Popen([tbirdPath, '-compose', composeCommand])
                    time.sleep(1)
                    keyboard.send('ctrl+v')
                    # keyboard.write(message) -- this also works but not needed, faster to paste

                    keyboard.send('ctrl+enter') # 3/4/22: get this to work!--works
                    break
    print('You entered ', values[0], values[1])

window.close()
