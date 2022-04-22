from tempfile import NamedTemporaryFile
import shutil
import csv
import codecs
import datetime



# 09/29/21: need to update few places, one is Wabash valley CF in IN
# also, seems like ZIp codes from PrisonPro are incorrect for Arizona ASPC lumley, may need
# to verify against AZ DOC later

# --- 07/1/21: now writes properly to file
def updating(arg1, **kwargs):
    today = datetime.date.today().strftime("%B %d, %Y")
    filename = 'AllDetails.csv'
    tempfile = NamedTemporaryFile(mode='a', delete=False)
    newfile = today + '-' + filename
    fields = ['Sno', 'Registration Number', 'Name', 'RollNo', 'Status']
    with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        for row in reader:
            reg = row['Registration Number']
            name = row['Name']
            rollno = row['RollNo']
            status = row['Status']
            for key, value in kwargs.items():
                if row['Sno'] == str(arg1) and key == 'regNum':
                    reg = value
                if row['Sno'] == str(arg1) and key == 'name':
                    name = value
                if row['Sno'] == str(arg1) and key == 'rollno':
                    rollno = value
                if row['Sno'] == str(arg1) and key == 'status':
                    status = value
                print('updating row', row['Sno'])
                row = ({'Sno': row['Sno'], 'Registration Number': reg, 'Name': name, 'RollNo': rollno, 'Status': status})
                writer.writerow(row)
                print('Done! Alh')
    shutil.move(tempfile.name, filename)

#updating('6', regNum='45453535')
#updating('5', status='Unknown', regNum='1010101')
#updating('4', rollno='why not workdude')
#updating('3', name='Rehamy B')
#updating('2', name='Komally Me')
#updating('4', Name='John Snow', RollNo='0101010', Status='Awesome')
#updating(4, name='Dude99 tHereHere')



# this function for updating csv entries --- 09/30/21: now added 2nd argument, State in capital abbrev.
# def updatingentry(arg1, arg2, **kwargs):
#     today = datetime.date.today().strftime("%B %d, %Y")
#     filename = 'customers10-Copy.csv'
#     tempfile = NamedTemporaryFile(mode='a', delete=False)
#     newfile = today + '-' + filename
#     fields = ['name', 'street', 'street2', 'address', 'zip', 'website']
#     #fields = ['name', 'street', 'address', 'zip', 'website']
#     with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
#         reader = csv.DictReader(csvfile, fieldnames=fields)
#         writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
#         for row in reader:
#             if arg1 == row['name'] and arg2 in row['address']:
#                 name = row['name']
#                 street = row['street']
#                 street2 = row['street2']
#                 address = row['address']
#                 zip = row['zip']
#                 website = row['website']
#                 for key, value in kwargs.items():
#                     if row['name'] == str(arg1) and key == 'street':
#                         street = value
#                     if row['name'] == str(arg1) and key == 'street2':
#                         street2 = value
#                     if row['name'] == str(arg1) and key == 'address':
#                         address = value
#                     if row['name'] == str(arg1) and key == 'zip':
#                         zip = value
#                     if row['name'] == str(arg1) and key == 'website':
#                         website = value
#                     # if row['name'] == str(arg1) and key == 'name':
#                     #     name = value
#                 print('updating row', row['name'])
#                 row = ({'name': name, 'street': street, 'street2': street2, 'address': address, 'zip': zip, 'website': website})
#                 writer.writerow(row)
#                 print('Done! Alh')
#     shutil.move(tempfile.name, filename)

# 09/30/21: still not working on update
#updatingentry('Bibb Correctional Facility', 'AL', street='565 Bibb Lane, Apt. #625')
#updating2('Bibb Correctional Facility', street='565 Bibb Lane, Apt. #625')

#updating2('Bibb Correctional Facility', street='565 Bibb Lane')



# this function for updating csv entries --- 09/30/21: now added 2nd argument, State in capital abbrev.
# def updatingentry2(arg1, arg2, **kwargs):
#     today = datetime.date.today().strftime("%B %d, %Y")
#     filename = 'customers10-Copy.csv'
#     tempfile = NamedTemporaryFile(mode='a', delete=False)
#     newfile = today + '-' + filename
#     fields = ['name', 'street', 'address', 'zip', 'website']
#     with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
#         reader = csv.DictReader(csvfile, fieldnames=fields)
#         writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
#         rows = []
#         for row in reader:
#             rows.append(row)
#         #csvfile.seek(0)
#         writer.writeheader()
#         writer.writerows(rows)
#         #csvfile.truncate()
#         for row in reader:
#             if arg1 == row['name'] and arg2 in row['address']:
#                 name = row['name']
#                 street = row['street']
#                 address = row['address']
#                 zip = row['zip']
#                 website = row['website']
#                 for key, value in kwargs.items():
#                     if row['name'] == str(arg1) and key == 'street':
#                         street = value
#                     if row['name'] == str(arg1) and key == 'address':
#                         address = value
#                     if row['name'] == str(arg1) and key == 'zip':
#                         zip = value
#                     if row['name'] == str(arg1) and key == 'website':
#                         website = value
#                     # if row['name'] == str(arg1) and key == 'name':
#                     #     name = value
#                 print('updating row', row['name'])
#                 row_updated = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
#                 writer.writerow(row_updated)
#                 print('Done! Alh')
#             else:
#                 print("not found!")
#     shutil.move(tempfile.name, filename)

#updatingentry2("Bibb Correctional Facility", 'AL', street='625 Bibb St.')


def updatingentry3(arg1, arg2, **kwargs):
    filename = 'customers10-Copy.csv'
    fields = ['name', 'street', 'street2', 'address', 'zip', 'website']
    with codecs.open(filename, 'r+', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        #writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        rows = []
        for row in reader:
            if arg1 == row['name'] and arg2 in row['address']:
                for key, value in kwargs.items():
                    if row['name'] == str(arg1) and key == 'street':
                        row['street'] = value
                    if row['name'] == str(arg1) and key == 'street2':
                        row['street2'] = value
                    if row['name'] == str(arg1) and key == 'address':
                        row['address'] = value
                    if row['name'] == str(arg1) and key == 'zip':
                        row['zip'] = value
                    if row['name'] == str(arg1) and key == 'website':
                        row['website'] = value
                    # if row['name'] == str(arg1) and key == 'name':
                    #     name = value
                    print('updating row element: ', row[key])
            rows.append(row)
        csvfile.seek(0)
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        #writer.writeheader()
        writer.writerows(rows)
        csvfile.truncate()
# &*(*&^&%%$&^%$&^%$&^%$&^%$&^%$>>>>>> 09/30/21: WORKS BELOW ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Done:

#12/09/21:
#updatingentry3('Tester CF', 'AL', street='P.O. Box 10001001010') --confirm this works with new field street2


#updatingentry3('Union Correctional Institution', 'FL', street='P.O. Box 1000')
#updatingentry3('Bibb Correctional Facility', 'AL', street='625 Booby Ave.')
#updatingentry3('Bibb Correctional Facility', 'AL', street='565 Bibb Lane')

#updatingentry3('', '', street='', address='', zip=, website='') #first 2 args mandatory, rest optional








# this function for making new entries to csv
def newentry(arg1, **kwargs):
    filename = 'customers10-Copy.csv'
    #filename = 'customers10.csv'
    fields = ['name', 'street', 'street2', 'address', 'zip', 'website']
    with codecs.open(filename, 'a', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        name = str(arg1)
        street = ''
        address = ''
        zip = ''
        website = ''
        for key, value in kwargs.items():
            if key == 'street':
                street = value
            if key == 'street2':
                street2 = value
            if key == 'address':
                address = value
            if key == 'zip':
                zip = value
            if key == 'website':
                website = value
        row = ({'name': name, 'street': street.title(), 'street2': street2.title(), 'address': address.upper(), 'zip': zip, 'website': website})
        writer.writerow(row)
        print('Done! Alh')

# use these as templates to add/update entries to csv >>>>>>>>>>>>>>>>>>
#newentry('', street='', street2='', address='', zip=, website='')

# newentry('',
#          street='',
#          street2='',
#          address='',
#          zip='',
#          website='')


#done =

print("check 1")

# newentry('Little Sandy Correctional Complex',
#          street='505 Prison Connector',
#          street2='',
#          address='Sandy Hook, KY 41171',
#          zip='41171',
#          website='https://corrections.ky.gov/Facilities/AI/lscc/Pages/default.aspx')




# newentry('Clinton Correctional Facility',
#          street='P.O. Box 2000',
#          street2='',
#          address='Dannemora, NY 12929',
#          zip='12929',
#          website='https://doccs.ny.gov/location/clinton-correctional-facility')




# newentry('Mid-State Correctional Facility',
#          street='P.O. Box 866',
#          street2='',
#          address='Wrightstown, NJ 08562',
#          zip='08562',
#          website='https://www.prisonpro.com/content/mid-state-correctional-facility')

# newentry('RIVERBEND CORRECTIONAL FACILITY',
#          street='196 LAYING FARM RD',
#          street2='',
#          address='MILLEDGEVILLE, GA 31061',
#          zip='31061',
#          website='http://www.dcor.state.ga.us/Facilities/riverbend-corr-facility')


# newentry('Northern State Prison',
#          street='P.O. Box 2300',
#          street2='',
#          address='Newark, NJ 07114',
#          zip='07114',
#          website='https://www.prisonpro.com/content/northern-state-prison')




# newentry('Plane State Jail',
#          street='904 FM 686',
#          street2='',
#          address='Dayton, TX 77535',
#          zip='77535',
#          website='https://www.tdcj.texas.gov/unit_directory/unit_information.html')




# newentry('Edna Mahan CF for Women',
#          street='P.O. Box 4004',
#          street2='',
#          address='Clinton, NJ 08809',
#          zip='08809',
#          website='https://www.prisonpro.com/content/edna-mahan-correctional-facility-women')

# newentry('Southern State Correctional Facility',
#          street='4295 Route 47',
#          street2='',
#          address='Delmont, NJ 08314',
#          zip='08314',
#          website='https://www.prisonpro.com/content/southern-state-correctional-facility')




# newentry('Marcy Correctional Facility',
#          street='P.O. Box 3600',
#          street2='',
#          address='Marcy, NY 13403-3600',
#          zip='13403',
#          website='https://doccs.ny.gov/location/marcy-correctional-facility')





# newentry('Limon Correctional Facility',
#          street='49030 State Hwy 71 South',
#          street2='',
#          address='Limon, CO 80826',
#          zip='80826',
#          website='https://cdoc.colorado.gov/facilities/limon-correctional-facility')



# newentry('Wyoming State Penitentiary ',
#          street='P.O. Box 400',
#          street2='',
#          address='Rawlins,WY 82301',
#          zip='82301',
#          website='https://www.prisonpro.com/content/wyoming-state-penitentiary')



#01/14/22:
# newentry('Northeast Ohio CC',
#          street='2240 Hubbard Road',
#          street2='',
#          address='Youngstown, OH 44505',
#          zip='44505',
#          website='https://drc.ohio.gov/northeastocc')

print("check 2")

#01/14/22:
# newentry('Dorsey Run Correctional Facility',
#          street='2020 Toulson Road',
#          street2='',
#          address='Jessup, MD 20794',
#          zip='20794',
#          website='https://www.dpscs.state.md.us/locations/drc.shtml')


#01/12/22:
# newentry('Gwinnett County Jail',
#          street='2900 University Pkwy',
#          street2='',
#          address='Lawrenceville, GA 30043',
#          zip='30043',
#          website='Google Search')



# 01/04/22: need to add dorsey run corr fac in MD=>done on 01/14/22


# 01/06/22:
# newentry('Upstate Correctional Facility',
#          street='P.O. Box 2000',
#          street2='',
#          address='Malone, NY 12953',
#          zip='12953',
#          website='https://doccs.ny.gov/location/upstate-correctional-facility')

# newentry('Elmira Correctional Facility',
#          street='1879 Davis St.',
#          street2='P.O. Box 500',
#          address='Collins, NY 14034',
#          zip='14901-0500',
#          website='https://doccs.ny.gov/location/elmira-correctional-facility')

# newentry('Collins Correctional Facility',
#          street='P.O. Box 340',
#          street2='',
#          address='Collins, NY 14034',
#          zip='14034-0340',
#          website='https://doccs.ny.gov/location/collins-correctional-facility')


# newentry('Bare Hill Correctional Facility',
#          street='181 Brand Rd',
#          street2='Caller Box #20',
#          address='Malone, NY 12953-0020',
#          zip='12953-0020',
#          website='https://doccs.ny.gov/location/bare-hill-correctional-facility')

# newentry('Auburn Correctional Facility',
#          street='135 State Street',
#          street2='P.O. Box 618',
#          address='Auburn, NY 13021',
#          zip='13021',
#          website='https://doccs.ny.gov/location/auburn-correctional-facility')

# newentry('Mid-State Correctional Facility',
#          street='P. O. Box 2500',
#          street2='',
#          address='Marcy, NY 13403',
#          zip='13403',
#          website='https://doccs.ny.gov/location/mid-state-correctional-facility')

print("check 2")

# testing = works below, 12/09/21:
# newentry('Tester CF',
#          street='1212 Ok st',
#          street2='po box 00101',
#          address='Homer, AL 76664',
#          zip='76664',
#          website='www.google.com')

#12/08/21:
# newentry('Coxsackie Correctional Facility',
#          street='P.O. Box 999',
#          address='Coxsackie, NY 12051-0200',
#          zip='12051-0200',
#          website='https://doccs.ny.gov/location/coxsackie-correctional-facility')


#12/01/21: done
#newentry('Green Haven Correctional Facility', street='594 Rt. 216', address='Stormville, NY 12582-0010', zip='12582-0010', website='https://doccs.ny.gov/location/green-haven-correctional-facility')

# 10/25/21: add ordnance road cc here >>> done, on 12/01/21
#newentry('', street='', address='', zip=, website='')
# newentry('Ordnance Road Correctional Center',
#          street='600 East Ordnance Road',
#          address='Glen Burnie, MD 21060',
#          zip='21060',
#          website='https://www.aacounty.org/locations-and-directions/ordnance-road-correctional-center')


# added below as of 11/02/21
#newentry('Five Points Correctional Facility', street='Caller Box 119', address='Romulus, NY 14541', zip='14541', website='https://www.prisonpro.com/content/five-points-correctional-facility')

#newentry('new jersey state prison', street='po box 861', address='trenton, nj 08625', zip='08625', website='')




#updatingentry('', street='', address='', zip=, website='')

# 09/28/21: below not yet executed, need to add street2 field in csv + above functions
#newentry('Five Points Correctional Facility', street='6600 State Route 96', address='', zip=, website='')

# 10/12/21: need to add riverbend corr rehab fac in GA, 196 laying farm rd, 31061 <<<<<<<<<<<<<<<

#newentry('Sing Sing Correctional Facility', street='354 Hunter Street', address='Ossining, New York 10562-5442', zip=10562-5442, website='https://www.prisonpro.com/content/sing-sing-correctional-facility')
# newentry('Wyoming Correctional Facility', street='P.O. Box 501', address='Attica, NY 14011', zip=14011, website='https://doccs.ny.gov/location/wyoming-correctional-facility')
# newentry('ASPC Florence - East Unit', street='PO Box 5000', address='Florence, AZ 85132', zip=85132, website='https://corrections.az.gov/')
# newentry('Wynne Unit', street='810 FM 2821', address='Huntsville, TX 77349', zip=77349, website='https://www.tdcj.texas.gov/unit_directory/unit_information.html')
# newentry('Great Meadow Correctional Facility', street='P.O. Box 51', address='Comstock, NY 12821-0051', zip=12821-0o0051, website='https://doccs.ny.gov/location/great-meadow-correctional-facility')
# newentry('Southport Correctional Facility', street='P.O. Box 2000', address='Pine City, NY 14871-2000', zip=14871-2000, website='https://doccs.ny.gov/location/southport-correctional-facility')
# newentry('Lee Adjustment Center', street='168 Lee County Adjustment Center', address='Beattyville, KY 41311', zip=41311, website='https://corrections.ky.gov/Facilities/AI/LAC/Pages/default.aspx')
#updatingentry(q_name, street=q_street, address=q_address, zip=q_zip, website=q_website)




# 08/18/21: this doesn't work yet...----08/24/21:alhamdulillah works!! now appends to csv with new entries
#updating3('New Place Facility', address = 'You cant find me 123 street')

# q1 = input("do you need to update anything?")
# if q1 == 'yes':
#     q_name = input("name?")
#     q_street = input("street?")
#     #q_address = input("address?")
#     q_a1 = input("city?")
#     q_a2 = input("state?")
#     q_zip = input("zip?")
#     q_website = input("website?")
#     q_address = q_a1+", "+q_a2+" "+q_zip
#     #newentry(q_name, street=q_street, address=q_address, zip=q_zip, website=q_website)
#     updatingentry(q_name, street=q_street, address=q_address, zip=q_zip, website=q_website)
# else:
#     print("goodbye!")

dct = {'one': 1, 'two': 2, 'five':5, 'three':3}

dci = sorted(dct)
print(dci)
"""

add this part to a new function to create/append an entry to csv file, will need to change mode to 'a' (append),
rest should be same


                if row['name'] != str(arg1):
                    name = str(arg1)
                    if key == 'street':
                        street = value
                    if key == 'address':
                        address = value
                    if key == 'zip':
                        zip = value
                    if key == 'website':
                        website = value

"""









"""


# --- 07/1/21: now writes properly to file

08/18/21: transposed for customer10.csv, starting testing = ALHAMDULILLAH transpose confirmed works

def updating2(arg1, **kwargs):
    today = datetime.date.today().strftime("%B %d, %Y")
    filename = 'customers10-Copy.csv'
    tempfile = NamedTemporaryFile(mode='a', delete=False)
    newfile = today + '-' + filename
    fields = ['name', 'street', 'address', 'zip', 'website']
    with codecs.open(filename, 'r', encoding='utf8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        for row in reader:
            name = row['name']
            street = row['street']
            address = row['address']
            zip = row['zip']
            website = row['website']
            for key, value in kwargs.items():
                if row['name'] == str(arg1) and key == 'street':
                    street = value
                if row['name'] == str(arg1) and key == 'address':
                    address = value
                if row['name'] == str(arg1) and key == 'zip':
                    zip = value
                if row['name'] == str(arg1) and key == 'website':
                    website = value
                if row['name'] == str(arg1) and key == 'name':
                    name = value
                print('updating row', row['name'])
                row = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
                writer.writerow(row)
                print('Done! Alh')
    shutil.move(tempfile.name, filename)









"""