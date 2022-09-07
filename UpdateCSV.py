from tempfile import NamedTemporaryFile
import shutil
import csv
import codecs
import datetime


class Modify:
    # this function for making new entries to csv
    def new_entry(arg1, **kwargs):
        filename = 'customers10-Copy.csv'
        # filename = 'customers10.csv'
        fields = ['name', 'street', 'street2', 'address', 'zip', 'website']
        with codecs.open(filename, 'a', encoding='utf8') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames=fields)
            name = str(arg1)
            street = ''
            address = ''
            zip_code = ''
            website = ''
            for key, value in kwargs.items():
                if key == 'street':
                    street = value
                if key == 'street2':
                    street2 = value
                if key == 'address':
                    address = value
                if key == 'zip':
                    zip_code = value
                if key == 'website':
                    website = value
            row = ({'name': name, 'street': street.title(), 'street2': street2.title(), 'address': address.upper(),
                    'zip': zip_code, 'website': website})
            writer.writerow(row)
            print(f'Done, added new entry for:{name}.')

    def update_entry(arg1, arg2, **kwargs):
        filename = 'customers10-Copy.csv'
        fields = ['name', 'street', 'street2', 'address', 'zip', 'website']
        with codecs.open(filename, 'r+', encoding='utf8') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=fields)
            # writer = csv.DictWriter(tempfile, delimiter=',', lineterminator='\n', fieldnames=fields)
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
                        print('Done, updated row element: ', row[key], f' for: {arg1}.')
                rows.append(row)
            csv_file.seek(0)
            writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames=fields)
            # writer.writeheader()
            writer.writerows(rows)
            csv_file.truncate()



# Examples:
# update_entry('Union Correctional Institution', 'FL', street='P.O. Box 1000')
# update_entry('Bibb Correctional Facility', 'AL', street='625 Booby Ave.')
# update_entry('Bibb Correctional Facility', 'AL', street='565 Bibb Lane')

# update_entry('', '', street='', address='', zip=, website='') #first 2 args mandatory, rest optional

# done 8/17/22
# new_entry('Centennial Correctional Facility',
#          street='PO BOX 600',
#          street2='',
#          address='Canon City, CO 81215-0600',
#          zip='81215-0600',
#          website='https://cdoc.colorado.gov/facilities/canon-city/centennial-correctional-facility')
# new_entry('',
#          street='',
#          street2='',
#          address='',
#          zip='',
#          website='')
