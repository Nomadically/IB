import unicodedata
import html5lib
import keyboard
import requests
import json, re
from bs4 import BeautifulSoup
from urllib.request import urlopen

import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 12))

layout = [
             [sg.Text(f"Line {i: >2d}:"), sg.Input("")] for i in range(10)] + [
             [sg.Button("Submit")],
             [sg.StatusBar("", size=(20, 1), key='Status')]
         ]

window = sg.Window('Title', layout, finalize=True)
prompt = window['Status'].update
input_key_list = [key for key, value in window.key_dict.items()
                  if isinstance(value, sg.Input)]



# print(window.key_dict)
while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Submit":
        if all(map(str.strip, [values[key] for key in input_key_list])):
            prompt("All inputs are OK !")
        else:
            prompt("Some inputs missed !")

window.close()

#
# text = urllib3.urlopen('http://dcsd.nutrislice.com/menu/meadow-view/lunch/').read()
# menu = json.loads(re.search(r"bootstrapData\['menuMonthWeeks'\]\s*=\s*(.*);", text).group(1))
#
# print(menu)
#


#


#     holding.append(unicodedata.normalize("NFKD", string))
#
# index = holding.index('INMATE NAME & REGISTER NUMBER')
#
# print(holding)
#
# print(len(holding))
# print(index)
#
# print(holding[366])
#


# from ahk import AHK
# ahk = AHK()
#
# win_main = ahk.win_get(title='Channergy 2021 Client/Server')
#
# win_main.activate()
# keyboard.send('f4, esc, alt+n')
# # keyboard.send('esc')
# # keyboard.send('alt+n')
#


# def main():
#     '''Process kill function'''
#     for proc in psutil.process_iter():
#         # check whether the process name matches
#         print(proc.name())
#         if any(procstr in proc.name() for procstr in ['notepad']):
#             print(f'Killing {proc.name()}')
#             proc.kill()
#
#
# if __name__ == "__main__":
#     main()


"""

url = "https://www.bop.gov/locations/institutions/tha/"
page = urlopen(url).read()
soup = bs(page, 'html.parser')

for item in soup.find_all('div'):
    if 'For inmates at the ' in item.text:
        data = item.text.split('var productDetail =')[-1].split('};')[0] + "}"
        datajson = json.loads(data.strip())
        print('Product Code :' + datajson['ProductCode'])
        for item in datajson['ProductSpecification']:
            print(item['SpecificationName'] + " : " + item['SpecificationValue'])

"""

"""
older iteration attempt:

html_doc = requests.get('https://www.bop.gov/locations/institutions/tha/#send_things')
soup = BeautifulSoup(html_doc.content, 'html.parser')

holding = []

#f = codecs.open('temptext.txt', encoding='utf-8',mode='w+')
# for string in soup.strings:
#     print(string)

for span in soup.find_all('span'):
    print(span.text)

"""
