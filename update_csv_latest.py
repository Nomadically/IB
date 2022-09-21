import codecs
import csv

"""
flow of program: 

1) need to find a facility by name, 
2) see if facility_name is present in both, and if so, then check if row['street_1'] is same
3) if it is same, then only billing address file used to write/pass info to channergy program

"""



def update_entry(arg1, arg2, **kwargs):
    file_billing = 'Prison-Addresses-Billing.csv'
    file_shipping = 'Prison-Addresses-Shipping.csv'
    fields_billing = ['facility_name', 'billing_name', 'street_1', 'street_2', 'address', 'zip_code', 'website']
    fields_shipping = ['facility_name', 'shipping_name', 'street_1', 'street_2', 'address', 'zip_code', 'website']
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