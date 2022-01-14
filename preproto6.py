from bs4 import BeautifulSoup
import urllib
import requests
import soupsieve as sv
import codecs
import csv
import io
import webbrowser
import re
import numpy as np
from numpy import indices

abbr = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

# will have to manually correct Arizona ASPC facilities to match properly
# also manually correct/verify csp corcoran in Cali

#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/north-kern-state-prison').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/bullock-correctional-facility').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/tucson-arizona-state-prison-complex').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/california-state-prison-corcoran').read()
html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/perryville-arizona-state-prison-complex').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/douglas-arizona-state-prison-complex').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/jester-i-iii-iv-units').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/eastern-correctional-institution-annex').read()
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

holding = []

for string in soup.strings:
    holding.append(string)
    if 'Inmate Mailing Address' in string:
        indexA = holding.index(string)
    if 'Physical Address' in string:
        index0 = holding.index(string)
    if 'Search for a Facility' in string:
        indexB = holding.index(string)
    #print(string)
# bound of indexes now incorporated into if statements above

# below are bounds for sublist of main strings, where inmate addresses will be stored
# indexA = holding.index('Inmate Mailing Address:')
# indexB = holding.index('Search for a Facility')

print(indexB)

h0 = holding[index0:indexA]

h2 = holding[indexA:indexB+1]
print(h2)


# data = {key.encode("ascii"): value for key, value in data.items()}
h3 = []
for h in h2:
    i = h.encode("ascii", "ignore")
    j = i.decode()
    h3.append(j) #h3 is now list holding proper text strings always
print("here i am")
print(h0)
#===============================================================================
# for string in h2:
#     pattern = re.compile(r'^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?')
#     regex = r"^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?"
#     #results = pattern.findall(string)
#     #match = re.search(regex, string)    
#     #print(results)
#     #if match != None:
#         #print(string)
#         #print(h2.index(string))
#===============================================================================

# OK so below indices is list of indexes in h2 where zip code match occurs
# now i need to set each index/element of indices as a base index for writing/capturing
# to save to csv
regex = r"^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?"    
pattern = re.compile(r'^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?')   
indices = [i for i, x in enumerate(h3) if re.search(regex, x)]
print(indices) 
#print(h2[4])
#print(h2[8])
#print(h2[12])
h4 = []
#z = re.search('[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', string).groupdict()['zipcode']
for i in indices:
    #print(h2[i])
    b = h3[i - 1]  # this will always be street address
    c = h3[i]  # this will always be city/state/zip
    #if "Inmate" in h3[i-2] or "Dorm" in h3[i-2] or "Bed" in h3[i-2]:
    if h3[i-2] != h0[1]:
        a = h3[i-3]
        #a = h0[1]
        e = h3[i-2]
        faclist = ['Dorm', 'Bed', 'Facility', 'Yard', 'Unit']
        #if any(faclist) in h3[i-2]:
        #f = h0[]
        try:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', h3[i]).groupdict()['zipcode']
        except AttributeError:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})', h3[i]).groupdict()['zipcode']
            print("Fixed this zip: "+h3[i])
        h4.append([a+', '+e, b, c, d])
    else:
        a = h3[i-2]
        try:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', h3[i]).groupdict()['zipcode']
        except AttributeError:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})', h3[i]).groupdict()['zipcode']
            print("Fixed this zip:"+h3[i])
        h4.append([a, b, c, d])
    #===========================================================================
    # with codecs.open("customers8.csv", encoding='utf-8', mode ='a') as f:
    #     fieldnames = ['name', 'street', 'address', 'zip']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     #writer.writeheader()
    #     writer.writerow({'name': a, 'street': b, 'address': c, 'zip': d})
    #     print("done this one")
    #===========================================================================
    
print(h4) # this is final list of decoded strings turned into addresses, saved as dict of addresses
print("above me is final list of stuff")
print(len(indices))



def inmatefind(state):
    url = 'https://www.google.com/search?q=inmate+locator+'
    state = re.search('^[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s(\d{5})', state).groupdict()['state']
    webbrowser.open(url+state, new=0, autoraise=True)
 
# this function will open browser link to google search of state inmate locator   
#inmatefind(c)


"""

            #below for zip
            encoded_zip = src_zip.encode("ascii", "ignore")
            decoded_zip = encoded_zip.decode()




"""

#print({k: v for k, v in globals().items() if not k.startswith("__")})

#===============================================================================
# for i in range(1, 11):
#     globals()[f"my_variable_{i}"] = i
# 
# 
# print(my_variable_1)
# print(my_variable_2)
#===============================================================================




#if len(indices) == 1:

#===============================================================================
# firstaddr = h2.index(h2[4]) #these are city state zips of different addresses in h2 list
# secaddr = h2.index(h2[8])
# thiraddr = h2.index(h2[12])
# 
# firststr = firstaddr -1
# secstreet = secaddr -1
# thirstreet = thiraddr -1
# 
# if "Inmate Name" in h2[firststr-1]:
#     firstname = firststr -2
# else:
#     firstname = firststr -1
# 
# secname = secstreet -1
# thirname = thirstreet -1
# 
# 
# print(h2[firstname]+", "+h2[firststr]+", "+h2[firstaddr])
#===============================================================================
    
    #===========================================================================
    # y = [x.group() for x in re.finditer(regex, string)]
    # print(y)
    # s = re.finditer(regex, string)
    # print(s[0])
    #===========================================================================

#===============================================================================
# 
#     for r in results:
#         if r != None:
#             indexprime = h2.index(string)
#             indexstreet = indexprime - 1
#             indexname = indexstreet - 1
#             print(h2[indexprime])
#             print(h2[indexstreet])
#             print(h2[indexname])
#===============================================================================


#===============================================================================
# print("testeree here")
# d = {}
# for x in range(1, len(indices)):
#     d["string{0}".format(x)] = "Hello"
# 
# print(d)
# print(d["string5"])
#===============================================================================
