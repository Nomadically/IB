import pandas as pd
from math import nan, isnan
from ahk import AHK
from pydantic import BaseModel, validator, ValidationError
from typing import Optional
# from main_gui import stat
from enum import Enum, unique


ahk = AHK()

# win = list(ahk.windows())
win = ahk.win_get(title='Database System Utility')

win.activate()

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


@unique
class States(Enum):
    AL = 'Alabama'
    AK = 'Alaska'
    AS = 'American Samoa'
    AZ = 'Arizona'
    AR = 'Arkansas'
    CA = 'California'
    CO = 'Colorado'
    CT = 'Connecticut'
    DE = 'Delaware'
    DC = 'District of Columbia'
    FL = 'Florida'
    GA = 'Georgia'
    GU = 'Guam'
    HI = 'Hawaii'
    ID = 'Idaho'
    IL = 'Illinois'
    IN = 'Indiana'
    IA = 'Iowa'
    KS = 'Kansas'
    KY = 'Kentucky'
    LA = 'Louisiana'
    ME = 'Maine'
    MD = 'Maryland'
    MA = 'Massachusetts'
    MI = 'Michigan'
    MN = 'Minnesota'
    MS = 'Mississippi'
    MO = 'Missouri'
    MT = 'Montana'
    NE = 'Nebraska'
    NV = 'Nevada'
    NH = 'New Hampshire'
    NJ = 'New Jersey'
    NM = 'New Mexico'
    NY = 'New York'
    NC = 'North Carolina'
    ND = 'North Dakota'
    MP = 'Northern Mariana Islands'
    OH = 'Ohio'
    OK = 'Oklahoma'
    OR = 'Oregon'
    PA = 'Pennsylvania'
    PR = 'Puerto Rico'
    RI = 'Rhode Island'
    SC = 'South Carolina'
    SD = 'South Dakota'
    TN = 'Tennessee'
    TX = 'Texas'
    UT = 'Utah'
    VT = 'Vermont'
    VI = 'Virgin Islands'
    VA = 'Virginia'
    WA = 'Washington'
    WV = 'West Virginia'
    WI = 'Wisconsin'
    WY = 'Wyoming'


class Field(BaseModel):
    """ This class ensures that any included input will fit within Channergy field space constraints. """
    first_name: Optional[str]
    last_name: Optional[str]
    inmate_id: Optional[str]
    inmate_id_second: Optional[str]
    facility_name: Optional[str]
    street_1: Optional[str]
    street_2: Optional[str]
    zip_code: Optional[str]
    state: Optional[str]

    @classmethod
    @validator('first_name')
    def check_first_name(cls, field):
        assert field != '', 'First name field cannot be empty.'
        if len(field) > 15:
            raise ValueError('First name exceeds length allowed by Channergy.')
        return field

    @classmethod
    @validator('last_name', 'inmate_id')
    def check_last_name_and_inmate_id(cls, field):
        max_val = 20
        last_name_id_length = 0
        for f in field:
            assert f != '', 'Last name or inmate ID cannot be empty.'
            last_name_id_length += len(f)
        if last_name_id_length > max_val:
            raise ValueError('Length of last name and inmate ID exceeds Channergy limit; please verify data!')
        return field

    @classmethod
    @validator('inmate_id_second')
    def check_inmate_id_second(cls, field):
        assert field != '', 'Second inmate ID cannot be empty.'
        return field

    @classmethod
    @validator('facility_name')
    def check_facility_name(cls, field):
        if len(field) > 40:
            raise ValueError('Facility name exceeds Channergy limit; please verify data!')
        return field

    @classmethod
    @validator('street_1')
    def check_street_1(cls, field):
        assert field != '', 'Street address cannot be empty.'
        if len(field) > 30:
            raise ValueError('Length of street exceeds Channergy limit; please verify data!')
        return field

    @classmethod
    @validator('street_2')
    def check_street_2(cls, field):
        assert field != '', 'Second line of street address cannot be empty.'
        if len(field) > 30:
            raise ValueError('Length of address line 2 exceeds Channergy limit; please verify data!')
        return field

    @classmethod
    @validator('zip_code')
    def check_zip_code(cls, field):
        assert field != '', 'Zip code cannot be empty.'
        if len(field) < 5:
            field = str(field).zfill(5)
        return field

    @classmethod
    @validator('state')
    def check_state(cls, field):
        states_dict = {s.name: s.value for s in States}
        assert field != '', 'State field cannot be empty.'
        if field not in list(states_dict.keys()):
            raise ValueError('Invalid state abbreviation, please verify data!')
        return field

def required_fields(**kwargs):
    options = ['first_name', 'last_name', 'inmate_id', 'facility_name', 'state', 'zip_code', 'street_1', 'street_2']
    for k, v in kwargs.items():
        if k in options:
            try:
                if k == 'first_name':
                    verified_name = Field(first_name=v)
                    print(verified_name)
                if k == 'last_name':
                    verified_name = Field(last_name=v)
                if k == 'inmate_id':
                    verified_name = Field(inmate_id=v)
                if k == 'facility_name':
                    verified_name = Field(facility_name=v)
                if k == 'street_1':
                    verified_street_1 = Field(street_1=v)
                if k == 'street_2':
                    verified_street_2 = Field(street_2=v)
                if k == 'zip_code':
                    verified_zip_code = Field(zip_code=v)
                if k == 'state':
                    verified_state = Field(state=v)
            except ValidationError as ve:
                print('not yet')
                return ve
#
# class Field(BaseModel):
#     """ This class ensures that any included input will fit within Channergy field space constraints. """
#     first_name: Optional[str]
#     last_name: Optional[str]
#     inmate_id: Optional[str]
#     inmate_id_second: Optional[str]
#     facility_name: Optional[str]
#     street_1: Optional[str]
#     street_2: Optional[str]
#     zip_code: Optional[str]
#     state: Optional[str]


required_fields(first_name='joe')

listed = [1, 2, 3]
n = 1
print(listed[n])