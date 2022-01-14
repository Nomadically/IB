from bs4 import BeautifulSoup
import urllib
import requests
import soupsieve as sv
import codecs
import csv
import io
import re
import numpy as np

#below was testing for confirm that inmate mailing addr exists as reference point, done
#===============================================================================
# f1 = open('out5.csv', 'rt')
# csv_reader = csv.reader(f1, escapechar='\\')
# #q = input("what name?")
# 
# for row in csv_reader:
#     html_doc = urllib.request.urlopen(row[0]).read()
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     holding = []
#     for string in soup.strings:
#         holding.append(string)
#     try:
#         index1 = holding.index('Inmate Mailing Address:')
#         print(index1)
#     except ValueError:
#         print(row[0])
#         continue
#===============================================================================

# 
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/roxbury-correctional-institution').read()
html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/chittenden-regional-correctional-facility').read()
#https://www.prisonpro.com/content/correctional-alternative-placement-program-capp
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/san-quentin-state-prison').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/easterling-correctional-institution').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/correctional-alternative-placement-program-capp').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/gulf-correctional-institution').read()
#html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/donaldson-correctional-facility').read()
soup = BeautifulSoup(html_doc, 'html.parser')
holding = []
for string in soup.strings:
    holding.append(string)
    if "Inmate Mailing Address" in string:
        index1 = holding.index(string)
        

h2 = holding[index1:index1+9] #this is list of useful info strings

fac_id_str = ['prison', 'institution', 'facility', 'center', 'correctional']
add_info_str = ['dorm', 'housing', 'bed']

#===============================================================================
# for ele in h2:
#     z = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}){1}\s(?P<zipcode>\d{5})(?:[-]\d{4})?', ele).groupdict()['zipcode']
#     if z != None:
#         print(z)
#         index2 = h2.index(ele)
#         print(index2)
#===============================================================================
        
#print(h2)
        
#print(holding[index1+5])    
#address = holding[index1+5]
#encoded_zip = address.encode("ascii", "ignore")
#decoded_zip = encoded_zip.decode()

for string in h2:
    #pattern = re.compile('^[^0-9]+(\,\s){1}([A-Z]{2}){1}\s(\d{5})(?:[-]\d{4})?')
    regex = r"^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?"
    #result = pattern.findall(string)
    match = re.search(regex, string)
    if match != None:
        print(string) #city state zip string, with zip being extracted in below statement
        z = re.search('[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', string).groupdict()['zipcode']
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
        src_name = h2[index4]
        encoded_name = src_name.encode("ascii", "ignore")
        decoded_name = encoded_name.decode()
        with codecs.open("customers8.csv", encoding='utf-8', mode ='a') as f:
            fieldnames = ['name', 'address', 'zip']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': decoded_name, 'address': h2[index3], 'zip': z})






    #===========================================================================
    # if result != None:
    #     index2 = h2.index(string)
    #     #print(result)
    #     print(h2[index2])
    #     #z = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}){1}\s(?P<zipcode>\d{5})(?:[-]\d{4})?', result).groupdict()['zipcode']
    #     #print(z)
    #===========================================================================


print(h2[index4])      
print("below here")
print(h2[0])
print(h2)
print(h2[3])
#print(h2[index2])

#method of stripping non ascii from stuff
h3 = []
for a in h2:
    encoded_h = a.encode("ascii", "ignore")
    decoded_h = encoded_h.decode()
    h3.append(a)
    print(a)
    


#print(result)
#print(h2[index2])
#print(h2[index2])

#z = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}){1}\s(?P<zipcode>\d{5})(?:[-]\d{4})?', holding[index1+5]).groupdict()['zipcode']

#print(z)
#actual_zip = re.match('^(\d{5})(?:[-]\d{4})?$', decoded_zip).groupdict()['zipcode'] #now we have zip code extracted from address
#act_zip = re.search('^\d{5}$', address)
#print(act_zip)
#===============================================================================
# address = holding[index4]
# encoded_zip = address.encode("ascii", "ignore")
# decoded_zip = encoded_zip.decode()
# 
# actual_zip = re.match('^\d{5}(?:[-]\d{4})?$', decoded_zip).groupdict()['zipcode'] #now we have zip code extracted from address
#===============================================================================


# this is regex for zip code and +4 matching > ^\d{5}(?:[-]\d{4})?$

#not quite finished here ^^^

#if "Dorm" in string or "housing" in string or "bed" in string:
        




#print(index1)
#print(h2)






#===============================================================================
# t2 = holding[47:55]
# print(t2)
# t3 = holding[index1:index1+9]
# print(t3[1])
#===============================================================================




#print(holding[index1+5]+" should be zip field")
#print(holding[y])
#check = holding.index('Inmate Mailing Address')

#===============================================================================
# test = holding[[i for i, item in enumerate(holding) if re.search('(inmate)\s(name)', item)]]
#print(test) ----- ^(inmate)\s(name)$
#
# #if "Dorm" in holding[index1+1]:
#     #index2 = index1 + 2
#     #print("place needs Housing info")
# #else:
# index2 = index1 + 2 #this should refer to facility name
# index3 = index2 + 1 #this should refer to street address
# index4 = index3 + 1 #this should refer to city state and zip
# address = holding[index4]
# try:
#     actual_zip = re.match('^.*(?P<zipcode>\d{5}).*$', address).groupdict()['zipcode'] #now we have zip code extracted from address
# except AttributeError:
#     actual_zip = 'FIND ME'
# actual_name = holding[index2]
# encoded_name = actual_name.encode("ascii", "ignore")
# decoded_name = encoded_name.decode()
#  
# print(index1)
# #===============================================================================
# # print(holding[index1])
# # print(holding[index2]+" this should be name of facility")
# # print(holding[index3]+" this should be street?")
# # print(holding[index4]+" this should be city state zip")
# # print(actual_zip)
# # print(decoded_name)
# #===============================================================================
#  
# fruit_list = ['raspberry', 'apple', 'strawberry']
# berry_idx = [i for i, item in enumerate(fruit_list) if re.search('berry$', item)]
# print(berry_idx)
# # (inmate)\s(name)
# 
# 
#  
# 
# print("ok")
# print(address)
# print(actual_zip)
# print(holding[index2])
# print(holding[index3])
#===============================================================================


#===============================================================================
# for string in soup.strings:
#     holding.append(string)
#     if "Inmate Mailing Address" in string:
#         print(holding.index(string))
#         index1 = holding.index(string)
#     if "Inmate" in string and "Name" in string:
#         
#         y = holding.index(string)
#         print(y)
#===============================================================================



#===============================================================================
# fruit_list = ['raspberry', 'apple', 'strawberry']
# berry_idx = [i for i, item in enumerate(fruit_list) if re.search('berry$', item)]
# print(berry_idx)
#===============================================================================


    #===========================================================================
    #     index1 = holding.index(string)
    #     index2 = index1 + 2 #this should refer to facility name
    #     index3 = index2 + 1 #this should refer to street address
    #     index4 = index3 + 1 #this should refer to city state and zip
    #     if "bed" in string or "housing" in string or "dorm" in string:
    #         temp2_index = holding.index(string)
    #         index1 = temp2_index + 1
    #         index2 = index1 + 1 #this should refer to facility name
    #         index3 = index2 + 1 #this should refer to street address
    #         index4 = index3 + 1 #this should refer to city state and zip
    # if "Inmate" in string and "Name" in string:
    #     y = holding.index(string)
    #     print(y)
    #===========================================================================

