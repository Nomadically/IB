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
        if "Inmate Mailing Address" in string:
            index1 = holding.index(string)            
    h2 = holding[index1:index1+9] #this is list of useful info strings
    fac_id_str = ['prison', 'institution', 'facility', 'center', 'correctional']
    add_info_str = ['dorm', 'housing', 'bed']
    for string in h2:
        regex = r"^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?"
        match = re.search(regex, string)
        if match != None:
            print(string) #city state zip string, with zip being extracted in below statement
            z = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>\d{5})(?:[-]\d{4})?', string).groupdict()['zipcode']
            print(z)
            print("next:")
            print(h2[h2.index(string)])
            index2 = h2.index(string) #this is firm location of string with zip in it
            index3 = index2 - 1 #this should be firm location of street address
            print("now finding always the street address:")
            print(h2[index3])
            print("now making sure dorm or housing info rightly places index for ")
            for a in add_info_str:
                if a in h2[index3-1]:
                    index4 = index3 - 2 #index4 should be facility name, depending on if dorm/bed field there or not
                    print(h2[index4])
                    break
                else:
                    index4 = index3 - 1
                    print(h2[index4])
                    break
            src_zip = z
            src_name = h2[index4]
            src_street = h2[index3]
            #below for zip
            encoded_zip = src_zip.encode("ascii", "ignore")
            decoded_zip = encoded_zip.decode()
            #below for name of facility      
            encoded_name = src_name.encode("ascii", "ignore")
            decoded_name = encoded_name.decode()
            #below for street       
            encoded_street = src_street.encode("ascii", "ignore")
            decoded_street = encoded_street.decode()
            print("Done so far:"+decoded_name+" "+decoded_street+" "+decoded_zip+".")
            with open("customers6.csv", "a", newline="") as f:
                fieldnames = ['name', 'address', 'zip']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow({'name': decoded_name, 'address': decoded_street, 'zip': decoded_zip})
                