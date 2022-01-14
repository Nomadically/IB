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
from difflib import SequenceMatcher
import pandas as pd
import collections
import operator

abbr = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}
#url = 'https://www.prisonpro.com/content/north-kern-state-prison'

#url = 'https://www.prisonpro.com/content/tucson-arizona-state-prison-complex'
url = 'https://www.prisonpro.com/content/bullock-correctional-facility'
#url = 'https://www.prisonpro.com/content/california-state-prison-corcoran' # manually update units/sections here
#url = 'https://www.prisonpro.com/content/perryville-arizona-state-prison-complex'
#url = 'https://www.prisonpro.com/content/tucson-arizona-state-prison-complex'
#url = 'https://www.prisonpro.com/content/douglas-arizona-state-prison-complex'
#url = 'https://www.prisonpro.com/content/jester-i-iii-iv-units' # may need to manually correct this one
#url = 'https://www.prisonpro.com/content/eastern-correctional-institution-annex'

html_doc = urllib.request.urlopen(url).read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/bullock-correctional-facility').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/tucson-arizona-state-prison-complex').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/california-state-prison-corcoran').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/perryville-arizona-state-prison-complex').read()
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
    if "Inmate" in h3[i-2] or "Dorm" in h3[i-2] or "Bed" in h3[i-2]:
        a = h3[i-3]
        b = h3[i-1]
        c = h3[i]
        try:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', h3[i]).groupdict()['zipcode']
        except AttributeError:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})', h3[i]).groupdict()['zipcode']
            print("Fixed this zip: "+h3[i])
        h4.append([a, b, c, d])
    else:
        a = h3[i-2]
        b = h3[i-1]
        c = h3[i]
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

h5 = []
for i in indices:
    altnames = ['Inmate', 'Dorm', 'Bed', 'Unit']
    a = h3[i-2]
    c = ''
    for ele in altnames:
        if ele in h3[i-2]:
            c = h0[1]    
            a = h3[i-3]
    b = h3[i-1]
    d = h3[i]
    try:
        e = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', h3[i]).groupdict()['zipcode']
    except AttributeError:
        e = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})', h3[i]).groupdict()['zipcode']
        print("Fixed this zip:"+h3[i])

    h5.append([a, b, c, d]) 
    
    
    with codecs.open("customers11.csv", encoding='utf-8', mode ='a') as f:
        fieldnames = ['name', 'street', 'street2', 'address', 'zip', 'website']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'name': a, 'street': b, 'street2': c, 'address':d, 'zip': e, 'website':url})
        print("done this one")




print(h5)
print('here dudeererererere')

def inmatefind(state):
    url = 'https://www.google.com/search?q=inmate+locator+'
    state = re.search('^[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s(\d{5})', state).groupdict()['state']
    webbrowser.open(url+state, new=0, autoraise=True)
 
# this function will open browser link to google search of state inmate locator   
#inmatefind(c)



df = pd.read_csv('customers11.csv')
names = df.name

prisons = []
for n in names:
    prisons.append(n)



print("why not")
#===============================================================================
# substring_counts={}
# 
# for i in range(0, len(prisons)):
#     for j in range(i+1,len(names)):
#         string1 = names[i]
#         string2 = names[j]
#         match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
#         matching_substring=string1[match.a:match.a+match.size]
#         if(matching_substring not in substring_counts):
#             substring_counts[matching_substring]=1
#         else:
#             substring_counts[matching_substring]+=1
# 
# print(substring_counts) #{'myKey_': 5, 'myKey_apples': 1, 'o': 1, '': 3}
#===============================================================================

#print(names)

#===============================================================================
# result = []
# def phrases(string):
#     words = string.split()
#     for number in range(len(words)):
#         for start in range(len(words)-number):
#              result.append(" ".join(words[start:start+number+1]))
#     return result
# 
# print(phrases(names[0]))
#===============================================================================

#all_phrases = collections.Counter(phrase for subject in subjects for phrase in phrases(subject))


#===============================================================================
# for i in range(0, len(names)):
#     mystring = names[i]
#     min_length = 3
#     substrings = [
#         mystring[i:i+j]
#         for i in range(0, len(mystring) - min_length + 1)
#         for j in range(min_length, len(mystring) - i + 1)
#         ]
#     counts = {}
#     for substring in substrings:
#         try:  # increase count for existing keys, set for new keys
#              counts[substring] += 1
#         except KeyError:
#              counts[substring] = 1
#     
#     print("done: "+names[i])
# counts = collections.Counter(substrings)
# print(counts)
#===============================================================================
#===============================================================================
# for i in range(0, len(names)):
#     for n in names:
#         phrases(names[i])
#===============================================================================
wordlist = []
#===============================================================================
# for i in range(0, len(names)):
#     string = names[i]
#     strr = string.split()
#     wordlist.extend(strr)
#===============================================================================
    

print(wordlist)

#print(result)
print('here')

tr = []
stringies = 'this is a list'
stringiest = 'not quite un listed'
st = stringies.split()
ts = stringiest.split()
#print(st)
tr.append(st)
tr.append(st)

print(tr)
tu = []
tu.extend(st)
tu.extend(ts)

print(tu)




testing = names[0].split()
print(testing)
wl = []
for n in names:
    #print(n.split())
    #wl.extend(n.split())
    print(n)
    print('worked now')
    

holder = []

for i in range(0, len(names)):
    s = names[i].split()
    print(s)
    holder.extend(s)
    
print(holder)

def most_frequent(List):
    counter = 0
    num = List[0]
      
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
  
    return num

print(most_frequent(holder))
print("here now 019201290192")
flat_list = [item for i in holder for item in i.split() ]
count_dict = {i:flat_list.count(i) for i in flat_list}
sorted_dict = sorted(count_dict.items(), reverse=True, key=operator.itemgetter(1))

print(sorted_dict)


for p in prisons:
    string = 'hamilton'
    if string.title() in p:
        print("ok")
        print(prisons.index(p))








#===============================================================================
# 
# def updating(**kwargs):
#         with codecs.open("customers10.csv", encoding='utf-8', mode ='w') as f:
#             fieldnames = ['name', 'street', 'address', 'zip', 'website']
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             #writer.writeheader()
#             #writer.writerow({'name': a, 'street': b, 'address': c, 'zip': d, 'website': row[0]})
#             print("done this one: "+row[0])
#             for key, value in kwargs.items():
#                 if key == row['name']:
#                     writer.writerow({'name': value})
#                     print("done:"+key+value)
#                     #print(row['address'])
#                     #print(row['street'])
#                     #print(row['zip'])
#===============================================================================


#updating(old_name="Test Facility", new_name="Test Facility 2")












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
