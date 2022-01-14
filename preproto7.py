import pandas as pd
import csv
from timeit import timeit
import re


names = []
addresses = []
zips = []
streets = []
websites = []

f = open('customers10.csv', 'rt')
csv_reader = csv.DictReader(f, escapechar='\\')
#q = input("what name?")
check = 'bibb'

for row in csv_reader:
    #print(row['name'])
    names.append(row['name'])
    addresses.append(row['address'])
    zips.append(row['zip'])
    streets.append(row['street'])
    websites.append(row['website'])
    if check.title() in row['name']:
        print(row)
    f.close
"""

df = pd.read_csv('customers9.csv')
names = df.name
streets = df.street
addresses = df.address
zips = df.zip
websites = df.website
prisons = names
"""


def wru(selected):
    state = re.search('^[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s(\d{5})', addresses).groupdict()['state']
    responses = []
    if state == selected:
        responses.append(names[addresses.index(state)])
    return responses

wru('Florida')


#the below checks created list of elements inside csv to see if input matches
#q2 = input("what anything to find?")

def test1():
    q2 = 'bibb'
    for name in names:
        try:
            if q2.title() in name:
                locate = names.index(name)
                print("found!")
                print(locate)
                print(names[locate])
                print(addresses[locate])
                print(zips[locate])
        except ValueError:
            print("not found")