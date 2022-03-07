import csv
import subprocess
from ahk import AHK
import keyboard

from openpyxl import load_workbook

prisons = {}

with open('CAprisonsCSV.csv') as csv_file:
    # reading the csv file using DictReader
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if 'Valley' in row['prison']:
            print(row)
            # break


tbirdPath = r'C:\Program Files\Mozilla Thunderbird\thunderbird.exe'
to = 'yousaf@islamicbookstore.com'
subject = 'Hello'
body = '<html><body><h1>Header</h1>This is the body. TEST EMAIL TO SELF<br></body></html>'
composeCommand = 'format=html,to={},subject={},body={}'.format(to, subject, body)
subprocess.Popen([tbirdPath, '-compose', composeCommand])
keyboard.send('ctrl+enter') # 3/4/22: get this to work!
print('worked till here')


# f = open('CAprisonsCSV.csv', 'rt')
# csv_reader = csv.DictReader(f, escapechar='\\')
# for row in csv_reader:
#     prisons.append(row)

# dicted = dict(list(csv_reader[0]))

# print(dicted)


# opening the csv file
# with open('CAprisonsCSV.csv') as csv_file:
#     # reading the csv file using DictReader
#     csv_reader = csv.DictReader(csv_file)
#
#     # converting the file to dictionary
#     # by first converting to list
#     # and then converting the list to dict
#     dict_from_csv = dict(list(csv_reader)[1])
#
#     # making a list from the keys of the dict
#     list_of_column_names = list(dict_from_csv.keys())
#
#     # displaying the list of column names
#     print("List of column names : ",
#           list_of_column_names)
#     print(dict_from_csv)



# with open('CAprisonsCSV.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('CAprisonsCSV-new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1] for rows in reader}

# opening the csv file by specifying
# the location
# with the variable name as csv_file
# with open('CAprisonsCSV.csv') as csv_file:
#     # creating an object of csv reader
#     # with the delimiter as ,
#     csv_reader = csv.reader(csv_file, delimiter=',')
#
#     # list to store the names of columns
#     list_of_column_names = []
#
#     # loop to iterate through the rows of csv
#     for row in csv_reader:
#         # adding the first row
#         list_of_column_names.append(row)
#
#         # breaking the loop after the
#         # first iteration itself
#         break
#
# # printing the result
# print("List of column names : ",
#       list_of_column_names[0])







# wb = load_workbook(filename = 'Test-Export-CAprisons.xlsx')
# sheet_ranges = wb['Customer #']
# print(sheet_ranges['A9'].value)

#this function finds data from CSV based on facility, so facility's address info
def fieldentry2(prison):
    #f = open('customers10.csv', 'rt')
    f = open('CAprisonsCSV.csv', 'rt')
    csv_reader = csv.DictReader(f, escapechar='\\')
    for row in csv_reader:
        if prison in row['prison']: # >>>>>>>>>>>>>>>>> need to update this logic, add 2nd check
            n = row['prison']         # like matching  as well as prison !! <<<<--- 09/10/21
            email = row['email']
            # if row['street2'] is not None:
            #     strt2 = row['street2'], #need to add this also, 12/01/21, done on 12/09/21
            # zpp = row['zip']
            break
    f.close
    print(row)
    if row['prison'] is not None and len(row['email']) > 1:
        # 01/28/22: fix the below, the str casting of str2, looks like a tuple inside mailware
        results = [n.strip(), email.strip()] #add str2 to this array <<< 12/01/21, then continue tracing where else code needs to be updated
    else:
        results = [n.strip(), email.strip()]
    return results

#fieldentry2('Salinas')

# class HashTable:
#
#     # Create empty bucket list of given size
#     def __init__(self, size):
#         self.size = size
#         self.hash_table = self.create_buckets()
#
#     def create_buckets(self):
#         return [[] for _ in range(self.size)]
#
#     # Insert values into hash map
#     def set_val(self, key, val):
#
#         # Get the index from the key
#         # using hash function
#         hashed_key = hash(key) % self.size
#
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
#
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
#
#             # check if the bucket has same key as
#             # the key to be inserted
#             if record_key == key:
#                 found_key = True
#                 break
#
#         # If the bucket has same key as the key to be inserted,
#         # Update the key value
#         # Otherwise append the new key-value pair to the bucket
#         if found_key:
#             bucket[index] = (key, val)
#         else:
#             bucket.append((key, val))
#
#     # Return searched value with specific key
#     def get_val(self, key):
#
#         # Get the index from the key using
#         # hash function
#         hashed_key = hash(key) % self.size
#
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
#
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
#
#             # check if the bucket has same key as
#             # the key being searched
#             if record_key == key:
#                 found_key = True
#                 break
#
#         # If the bucket has same key as the key being searched,
#         # Return the value found
#         # Otherwise indicate there was no record found
#         if found_key:
#             return record_val
#         else:
#             return "No record found"
#
#     # Remove a value with specific key
#     def delete_val(self, key):
#
#         # Get the index from the key using
#         # hash function
#         hashed_key = hash(key) % self.size
#
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
#
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
#
#             # check if the bucket has same key as
#             # the key to be deleted
#             if record_key == key:
#                 found_key = True
#                 break
#         if found_key:
#             bucket.pop(index)
#         return
#
#     # To print the items of hash map
#     def __str__(self):
#         return "".join(str(item) for item in self.hash_table)
#
#
# hash_table = HashTable(50)
#
# # insert some values
# hash_table.set_val('gfg@example.com', 'some value')
# print(hash_table)
# print()
#
# hash_table.set_val('portal@example.com', 'some other value')
# print(hash_table)
# print()
#
# # search/access a record with key
# print(hash_table.get_val('portal@example.com'))
# print()
#
# # delete or remove a value
# hash_table.delete_val('portal@example.com')
# print(hash_table)



