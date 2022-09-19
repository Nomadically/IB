import unicodedata
import html5lib
import keyboard
import requests
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

#
html_doc = requests.get('https://www.bop.gov/locations/institutions/tha/#send_things')
soup = BeautifulSoup(html_doc.content, 'html.parser')

holding = []
tag = soup.br
#f = codecs.open('temptext.txt', encoding='utf-8',mode='w+')
for string in tag.strings:
    print(string)

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