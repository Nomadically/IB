import os
from time import perf_counter
# import psutil
# # import traceback
# import signal
from pywinauto import Application
#
import subprocess
# #
import psutil
# import win32gui
import win32gui
import win32con
import win32api
# # import wmi
#
# # from ahk import AHK, Hotkey
# import os
# # import subprocess
# # import UpdateCSV
# from fpdf import FPDF

t1_start = perf_counter()



# hwndMain = win32gui.FindWindow("Notepad", None)
# print(hwndMain)
# hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
# win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x5b, 0)




# listOfProcessNames = list()
# # Iterate over all running processes
# for proc in psutil.process_iter():
#    # Get process detail as dictionary
#    pInfoDict = proc.as_dict(attrs=['pid', 'name'])
#    # Append dict of process detail in list
#    listOfProcessNames.append(pInfoDict)
#
# target = 'Channergy'
# # ---- 8/30/22: this WORKS to terminate a process by ID
# # for e in listOfProcessNames:
# #     if target in e['name']:
# #         print(e['name'])
# #         os.kill(e['pid'], signal.SIGINT)
#
# print(listOfProcessNames)


# win2find = input('enter name of window to find')

# 09/06/22:
# win2find = 'Notepad++'
# whnd = win32gui.FindWindowEx(None, None, None, win2find)
# if not (whnd == 0):
#   print('FOUND!')

# pdf = FPDF()
#
# pdf.add_page()
#
# pdf.set_font("Arial", size=15)
#
# pdf.cell(200,10,txt="GeeksforGeeks",
#          ln =1, align='C')
#
# pdf.cell(200, 10, txt="A Computer Science portal for geeks.",
#          ln=2, align='C')
#
# pdf.cell(200, 10, txt="Where will we end up?",
#          ln=2, align='L')
# pdf.cell(100, 10, txt="Where will we end up?",
#          ln=2, align='L')
#
# pdf.output("GFG-2.pdf")
# here below
# listOfProcessNames = list()
# # Iterate over all running processes
# for proc in psutil.process_iter():
#    # Get process detail as dictionary
#    pInfoDict = proc.as_dict(attrs=['pid', 'name'])
#    # Append dict of process detail in list
#    listOfProcessNames.append(pInfoDict)
#
# target = 'Channergy'
# # ---- 8/30/22: this WORKS to terminate a process by ID
# # for e in listOfProcessNames:
# #     if target in e['name']:
# #         print(e['name'])
# #         os.kill(e['pid'], signal.SIGINT)


#
openProcesses = {}
target = "Notepad"
#
def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hex(hwnd), win32gui.GetWindowText(hwnd))
        adding = {win32gui.GetWindowText(hwnd): hex(hwnd)}
        openProcesses.update(adding)
#
win32gui.EnumWindows(winEnumHandler, None)

window_id = openProcesses.get('Search for Customer')
print(window_id)

os.system("taskkill /im ")
# app = Application().connect(process=window_id)
# app.top_window().set_focus()





# #
# for key in openProcesses:
#     if key.find(target) > -1:
#         print(openProcesses[key])
#         for e in listOfProcessNames:
#             if target in e['name']:
#                 pid = e['pid']
#                 subprocess.call('taskkill', '/f', '/pid', pid)

# s = 'Notepad'
# count = 0
# if any(s in i for i in openProcesses):
#     print(f'{s} is present in the list')
#     count += 1
# else:
#     print(f'{s} is not present in the list')
# print(count)

# UpdateCSV.Modify.new_entry('Sullivan Correctional Facility',
#          street='P.O. Box 116',
#          street2='',
#          address='Fallsburg, NY 12733-0116',
#          zip='12733-0116',
#          website='https://doccs.ny.gov/location/sullivan-correctional-facility')
# ahk = AHK()
#
# for window in ahk.windows():
#     print(window.title)
#
# Running the aforementioned command and saving its output
# output = os.popen('wmic process get description, processid').read()
#
# # Displaying the output
# print(output)
#
# if 'svchost.exe' in output:
#     print('here')

# open_windows = win32gui.EnumWindows()
# print(open_windows)


# traverse the software list
# Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
# a = str(Data)
# # try block
# #  arrange the string
# try:
#     for i in range(len(a)):
#         print(a.split("\\r\\r\\n")[i])
# except IndexError as e:
#     print("All Done")

# import wmi library

# This variable ti would be used
# as a parity and counter for the
# terminating processes
ti = 0

# This variable stores the name
# of the process we are terminating
# The extension should also be
# included in the name


t1_stop = perf_counter()

print("Elapsed time during the whole program in seconds:",
      t1_stop - t1_start)

import UpdateCSV

# UpdateCSV.Modify.update_entry('Bibb Correctional Facility', 'AL', street='565 Bibb Lane')
# UpdateCSV.Modify.new_entry('Bibbby Correctional Facility',
#                            street='927 chill court',
#                            street2='',
#                            address='Baltimore, MD 21223',
#                            zip='21223',
#                            website='http://google.com')

# new_entry('',
#          street='',
#          street2='',
#          address='',
#          zip='',
#          website='')

# update_entry('Bibb Correctional Facility', 'AL', street='565 Bibb Lane')

# import smtplib
#
# # 8/11/22: api key created for raztraders1, =
# #AIzaSyClTJWUqfRKkkz6VAbrvOGDObXm-5wx3xU
#
# gmail_user = 'raztraders1@gmail.com'
# gmail_password = '01ufLwLAL51u4I'
#
# sent_from = gmail_user
# to = ['yousaf@islamicbookstore.com']
# subject = 'Lorem ipsum dolor sit amet'
# body = 'consectetur adipiscing elit'
#
# email_text = """\
# From: %s
# To: %s
# Subject: %s
#
# %s
# """ % (sent_from, ", ".join(to), subject, body)
#
# try:
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     smtp_server.ehlo()
#     smtp_server.login(gmail_user, gmail_password)
#     smtp_server.sendmail(sent_from, to, email_text)
#     smtp_server.close()
#     print ("Email sent successfully!")
# except Exception as ex:
#     print ("Something went wrong….",ex)


# import PySimpleGUI as sg
#
# sg.theme('DarkAmber') # Add a touch of color
#
# # All the stuff inside your window.
# layout = [ [sg.Text('Some text on Row 1')],
# [sg.Text('Enter something on Row 2'), sg.InputText()],
# [sg.Button('Ok'), sg.Button('Cancel')],
#            [sg.Button('test')]]
#
# # Create the Window
# window = sg.Window('Window Title', layout)
#
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     if event == "test":
#         sg.popup_timed('popup_timed')
#     if event == "Ok":
#
#         # what we want to do: when process prison is clicked,
#         # then first thing is to create directory while making sure
#         inmates_test = values[0]
#         if ';' in inmates_test: #indicates at least 2 people in input
#             new_dict = inmates_test.split(';')
#             count = 0
#             for n in new_dict:
#                 inmate = new_dict[count].split(',')
#                 inmate_name = inmate[0]
#                 inmate_id = inmate[1]
#                 manifest_ref = inmate[2]
#                 print(inmate_name)
#                 count = count+1
#                 # print(new_dict[0])
#                 # print(new_dict[1])
#         else:
#             single = inmates_test.split(',')
#             print(single[0].title()) #name
#             print(single[1]) #id
#             print(single[2]) #manifest ref
#             print('You entered this here=', single[0])
#
#             window.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # from openpyxl import load_workbook
# #
# # wb = load_workbook(filename='Manifest-Weekly.xlsx')
# #
# # sheet = wb['Sheet3']
# # # worksheet['D3']='Whatever you want to put in D3'
# # #sheet['A2'] = values['mainproject']
# #
# # #print(sheet['C2'].value)
# #
# # names = sheet['C2'].value
# # current = 'Avenal State Prison'
# # #as of 8/5/22 = these can access any rows and columns in an excel file xlsx
# #
# #
# #
# # # first need to match facility in mainproject = to prison in manifest-weekly file
# # # then need to go to inmates row, access values and str.split them according to ;
# #
# # #inmates_test = 'john doe, A123456, 433112; johny doey, A1245453456, 4335112; johnee doeee, A123456766, 43315512 '
# # #inmates_test = 'john doe,A123456,433112'
# #
# # inmates_test = names
# # if ';' in inmates_test:
# #     new_dict = inmates_test.split(';')
# #     print(new_dict[0])
# #     print(new_dict[1])
# # else:
# #     single = inmates_test.split(',')
# #     print(single[0].title())
# #     print(single[1])
# #     print(single[2])
# #
# # stored = {1: names}
# #
# # #print(stored)
# #
# # test = {'fname last name', '123455', 445311}
# # test2 =['fname last name', '123455', 445311]
# #
# # for col in sheet['A']:
# #     print(col.value)
# #     if col.value == current:
# #         print('this is where we found it')
# #
# # for row in sheet[1]:
# #     print(row.value)
# #
# #
# # prisons = []
# # for col in sheet['A']:
# #     prisons.append(col.value)
# #     #print('test')
# #
# # t = 0
# #
# # if current in prisons:
# #     print('finally?')
# #     t = prisons.index(current)
# # print(t)
# # # ws.cell(row, column)
# # print(sheet[('C'+str(t))].value)
