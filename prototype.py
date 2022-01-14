from bs4 import BeautifulSoup
import urllib
import requests
import soupsieve as sv
import codecs
import csv
import io
import re
import numpy as np
import pandas as pd


f1 = open('out5.csv', 'rt')
csv_reader = csv.reader(f1, escapechar='\\')
#q = input("what name?")

for row in csv_reader:
    html_doc = urllib.request.urlopen(row[0]).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    holding = []
    for string in soup.strings:
        holding.append(string)
    try:
        index1 = holding.index('Inmate Mailing Address:')
    except ValueError:
        print(row[0]+" Can't find inmate mailing address. Check me!")
        break
    index2 = index1 + 2 #this should refer to facility name
    index3 = index2 + 1 #this should refer to street address
    index4 = index3 + 1 #this should refer to city state and zip
    address = holding[index4]
    encoded_zip = address.encode("ascii", "ignore")
    decoded_zip = encoded_zip.decode()
    try:
        actual_zip = re.match('^.*(?P<zipcode>\d{5}).*$', decoded_zip).groupdict()['zipcode'] #now we have zip code extracted from address
    except AttributeError:
        actual_zip = 'FIND ME'
        print(row[0]+" Zipcode issue, check me.")
        continue
    actual_name = holding[index2]
    encoded_name = actual_name.encode("ascii", "ignore")
    decoded_name = encoded_name.decode()
    actual_address = holding[index3]
    encoded_address = actual_address.encode("ascii", "ignore")
    decoded_address = encoded_address.decode()
    #below 3 statements are for trying to put names of facilities in easy to checkk list
    column_names = ["name", "address", "zip"]
    df = pd.read_csv("customers4.csv", names=column_names)
    namings = df.name.to_list()
    
    if holding[index2] not in namings: #remove this in next iteration, writing list just once should stop dupe entries
        with open("customers5.csv", "a", newline="") as f:
            fieldnames = ['name', 'address', 'zip']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({'name': decoded_name, 'address': decoded_address, 'zip': actual_zip})
    else:
        continue
        
        
        

#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/eastern-correctional-institution-annex').read()
#soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
#head_tag = soup.head
#print(head_tag.contents)
#title_tag = head_tag.contents[0]
#print(title_tag)
#for child in head_tag.descendants:
    #print(child)

#holding = []

#f = codecs.open('temptext.txt', encoding='utf-8',mode='w+')
#for string in soup.strings:
    #holding.append(string)
    
#print(holding)
#print(len(holding))
#index1 = holding.index('Inmate Mailing Address:')
#print(index1)

#index2 = index1 + 2 #this should refer to facility name
#index3 = index2 + 1 #this should refer to street address
#index4 = index3 + 1 #this should refer to city state and zip


#print(holding[57]) #this is index above of reference point in each website
#print(holding[58])

#print(holding[59]) #this is the facility name
#print(index2)

#print(holding[60]) #this is street address
#print(index3)

#print(holding[61]) #this is city state and zip
#print(index4)

print("ok nearly")

#below is so that zip code can be extracted from city state zip entry
#address = holding[index4]
#address = holding[61]
#actual_zip = re.match('^.*(?P<zipcode>\d{5}).*$', address).groupdict()['zipcode']
#print(actual_zip) #now we have zip code extracted from address

#actual_name = holding[59]
#actual_name = holding[index2]
#below is in case string from fac name needs to be stripped of non-ACSII
#encoded_name = actual_name.encode("ascii", "ignore")
#decoded_name = encoded_name.decode()
#print(decoded_name)


#THE BELOW APPENDS TO CSV WOOOOOOT, now also writes to every line with no blank in between
#file = open('customers3.csv', 'a', newline='')
#fieldnames = ['name', 'address', 'zip']
#writer = csv.DictWriter(file, fieldnames=fieldnames)
#writer.writeheader()
#writer.writerow({'name': decoded_name, 'address': holding[index3], 'zip': actual_zip})

#with open("out4.csv", "a", newline="") as f:

