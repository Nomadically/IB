import re


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



address = 'sdfds, MD 82332-212'
#so far, it means " " then 5 digits, followed by non-capture group of zip+4 numbers
act_zip = re.search('(:[A-Z]{2})?\s\d{5}(?:[-]\d{4})?', address)

act2_zip = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}){1}\s(?P<zipcode>\d{5})(?:[-]\d{4})?', address).groupdict()['zipcode']

print(act_zip)
print(act2_zip)