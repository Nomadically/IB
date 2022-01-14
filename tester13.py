from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import codecs
import csv
import numpy as np

req = Request("https://www.prisonpro.com/correctional-facilities-by-state")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

#print(links)

print(links.index('https://www.prisonpro.com/content/alabama-prisons-jails')) # = 8
print(links.index('https://www.prisonpro.com/content/wyoming-prisons-jails')) # = 58

statePrisons = []
for state in links[8:59]:
    statePrisons.append(state)
    
print(statePrisons[0])

#done, list of prison websites saved
#np.savetxt("StatePrisonWebsites.csv", statePrisons, delimiter =", ", fmt ='% s')

print("ok till here")


req2 = Request("https://www.bop.gov/locations/list.jsp")
html_page2 = urlopen(req2)
soup2 = BeautifulSoup(html_page2, "lxml")

links2 = []
for link in soup2.findAll('a'):
    links2.append(link.get('href'))
    
#print(links2)
print(soup2.prettify())


















"""

f = codecs.open('StatePrisonList.csv', encoding='utf-8',mode='w+')
for prison in statePrisons:
    f.write(prison)

f.close()



with f:
    write = csv.writer(f, quoting=csv.QUOTE_ALL)
    for state in statePrisons:
        write.writerow(state)



for link in links:
    print(link)
    print(link.attrs['href'])
    linked = link.attrs['href']
    x = soup.find_all(string="Search")
    #print(x)



def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)




"""