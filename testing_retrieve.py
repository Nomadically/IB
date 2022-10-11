import pandas as pd
from math import nan, isnan


def retrieval(**kwargs):
    """This function will match up facility name across 2 different CSV databases, confirming correct facility
        by matching up state with input. Also filtering out NaN and empty values from results."""
    facility_name = kwargs.get('facility_name', None)
    state = kwargs.get('state', None)
    names_df = ['facility_name',  'name', 'street_1', 'street_2', 'address', 'zip_code', 'website']
    df_shipping = pd.read_csv('Prison-Addresses-Shipping.csv', names=names_df)
    df_billing = pd.read_csv('Prison-Addresses-Billing.csv', names=names_df)
    billing_name = df_billing[df_billing['facility_name'].str.contains(facility_name)]
    shipping_name = df_shipping[df_shipping['facility_name'].str.contains(facility_name)]
    if billing_name.equals(shipping_name) and billing_name['address'].str.contains(state).any():
        ship_to_name = billing_name.iloc[0][1]
        ship_to_street_1 = billing_name.iloc[0][2]
        ship_to_street_2 = billing_name.iloc[0][3]
        ship_to_zip_code = billing_name.iloc[0][5]
        results_pre = [ship_to_name, ship_to_street_1, ship_to_street_2, ship_to_zip_code]
        results_actual = [x for x in results_pre if pd.isnull(x) is False and x != 'nan' and x != '']
        print(results_actual)
        return results_actual
    else:

        print('not there yet, here goes logic if billing + shipping are different')

retrieval(facility_name='Bibb', state='AL')

def random_func():
    dict_1 = {'val': 1, 'val2':2}
    dict_2 = {'val3': 3, 'val4': 4}
    # print(len(dict_1, dict_2))
    return dict_1, dict_2

print(len(random_func()))

def random_func2(trying: dict):
    print(len(trying))
    return trying

newest = random_func2(random_func())

print(newest[0]['val'])

# if newest[0]['val4'] in newest[0].keys:
#     print('its here!@')
# else:
#     print('nope')

try:
    newest[0]['val4']
except KeyError:
    print('it aint here')
else:
    print('its here bro')
