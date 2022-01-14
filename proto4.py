from bs4 import BeautifulSoup
import urllib
import requests
import soupsieve as sv
import codecs
import csv
import io
import re
import numpy as np
from numpy import indices

f1 = open('out5.csv', 'rt')
csv_reader = csv.reader(f1, escapechar='\\')

for row in csv_reader:
    html_doc = urllib.request.urlopen(row[0]).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    holding = []
    for string in soup.strings:
        holding.append(string)
        if 'Inmate Mailing Address' in string:
            indexA = holding.index(string)
        if 'Search for a Facility' in string:
            indexB = holding.index(string)
    h2 = holding[indexA:indexB+1]
    h3 = []
    for h in h2:
        i = h.encode("ascii", "ignore")
        j = i.decode()
        h3.append(j)
    regex = r"^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?"     
    indices = [i for i, x in enumerate(h3) if re.search(regex, x)]
    #print(indices)
    h4 = []
    for i in indices:
        if "Inmate" in h3[i-2]:
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
        with codecs.open("customers10.csv", encoding='utf-8', mode ='a') as f:
            fieldnames = ['name', 'street', 'address', 'zip', 'website']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            #writer.writeheader()
            writer.writerow({'name': a, 'street': b, 'address': c, 'zip': d, 'website': row[0]})
            print("done this one: "+row[0])
    